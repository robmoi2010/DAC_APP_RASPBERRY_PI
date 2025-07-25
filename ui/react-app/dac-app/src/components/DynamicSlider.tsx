import { HStack, Slider } from "@chakra-ui/react";
import { updateSliderValue } from "../state-repo/slices/sliderValuesSlice";
import type { responseDataType } from "../utils/types";
import { useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import type { Dispatch } from "redux";

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
const DynamicSlider = ({ dataFunction, updateFunction, tooltipText, min, max, step, label, width, color, value,id}: Props) => {
    
    const sliderValue = useSelector((state: { sliderValues: { items: { [key: string]: number } } }) => state.sliderValues.items)[id];
    const dispatch = useDispatch();
    useEffect(() => {
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
        if (value != null) {
            if (value != sliderValue) {
                dispatch(updateSliderValue({ key: id, value: value }));
            }
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
const handleChange = (dispatch: Dispatch, number: number[], updateFunction: (data: string) => Promise<responseDataType>, key: string) => {
    const data = { key: "" + number[0], value: "" + number[0] };
    updateFunction(JSON.stringify(data)).then(dt => {
        dispatch(updateSliderValue({ key: key, value: Number(dt.value) }))
    }
    );
}
export default DynamicSlider;