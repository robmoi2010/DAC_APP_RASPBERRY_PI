/*
 * Copyright (C) 2025 Robert Moi, Goglotek LTD
 *
 *  This file is part of the DAC_APPLICATION System.
 *
 *  The DAC_APPLICATION System is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  The DAC_APPLICATION is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with the DAC_APPLICATION. If not, see <https://www.gnu.org/licenses/>
 */
import { HStack, Slider } from "@chakra-ui/react";
import { updateSliderValue } from "../state-repo/slices/sliderValuesSlice";
import type { responseDataType } from "../utils/types";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import type { Dispatch } from "redux";
import { updateSliderValues } from "../state-repo/slices/updateSliderValuesSlice";

type Props = {
    dataFunction?: () => Promise<responseDataType>;
    updateFunction: (data: string) => Promise<responseDataType>;
    tooltipText?: string;
    min: number;
    max: number;
    step: number;
    label: string;
    width: string;
    color: string;
    value?: number;
    id: string;

};
const DynamicSlider = ({ dataFunction, updateFunction, tooltipText, min, max, step, label, width, color, value, id }: Props) => {
    const sliderValue = useSelector((state: { sliderValues: { items: { [key: string]: number } } }) => state.sliderValues.items)[id];
    const shouldUpdateSliderValues = useSelector((state: { updateSliderValues: { items: { [key: string]: boolean } } }) => state.updateSliderValues.items)[id];
    const dispatch = useDispatch();
    useEffect(() => {
        dispatch(updateSliderValues({ key: id, value: true }))
        if (value == null && String(value).length > 0) {
            if (dataFunction != null) {
                dataFunction().then(data => {
                    dispatch(updateSliderValue({ key: id, value: Number(data?.value) }));
                });
            }
        }
        else {
            if (value != null) {
                dispatch(updateSliderValue({ key: id, value: value }));
            }
        }
    }, []);
    useEffect(() => {
        if (shouldUpdateSliderValues) {
            if (value != null) {
                if (value != sliderValue) {
                    dispatch(updateSliderValue({ key: id, value: value }));
                }
            }
        }
        if (sliderValue == value) {//reenable remote update of slider once server value=current slider value
            dispatch(updateSliderValues({ key: id, value: true }))
        }
    }, [value]);
    return (<Slider.Root colorPalette={color} width={width} value={[sliderValue != null ? sliderValue : 0]} onValueChangeEnd={(e) => handleChange(dispatch, e.value, updateFunction, id)} step={step} min={min} max={max} size="lg" onValueChange={(e) => dispatch(updateSliderValue({ key: id, value: e.value[0] }))}>
        <HStack justify="space-between">
            <Slider.Label>{label}</Slider.Label>
            <Slider.ValueText />
        </HStack>
        <Slider.Control>
            <Slider.Track>
                <Slider.Range />
            </Slider.Track>
            <Slider.Thumbs />
        </Slider.Control>
    </Slider.Root>);
}
const handleChange = (dispatch: Dispatch, number: number[], updateFunction: (data: string) => Promise<responseDataType>, id: string) => {
    const data = { key: "" + number[0], value: "" + number[0] };
    dispatch(updateSliderValues({ key: id, value: false }));
    updateFunction(JSON.stringify(data)).then(dt => {
        dispatch(updateSliderValue({ key: id, value: Number(dt.value) }))
    }
    );
}
export default DynamicSlider;