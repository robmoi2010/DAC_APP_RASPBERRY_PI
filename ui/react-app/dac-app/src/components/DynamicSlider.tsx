import { addSliderValue, updateSliderValue } from "../state-repo/slices/sliderValuesSlice";
import type { responseDataType } from "../utils/types";
import * as Slider from '@radix-ui/react-slider';
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import type { Dispatch } from "redux";

type Props = {
    dataFunction: () => Promise<responseDataType>;
    updateFunction: (data: string) => Promise<responseDataType>;
    tooltipText: string;
    index: number; //for multiple sliders on same page, differentiates values
    min:number;
    max:number;
    step:number
};
const DynamicSlider = ({ dataFunction, updateFunction, tooltipText, index, min, max, step }: Props) => {
    const sliderValues = useSelector((state: { sliderValues: { items: number[] } }) => state.sliderValues.items);
    const dispatch = useDispatch();
    useEffect(() => {
        dataFunction().then(data => {
            if (sliderValues.length - 1 >= index) {
                dispatch(updateSliderValue({ index: index, value: Number(data?.value) }));
            }
            else {
                dispatch(addSliderValue(Number(data?.value)));
            }
        });
    }, []);
    return (<Slider.Root
        value={[sliderValues[index]]}
        onValueChange={(number) => handleChange(dispatch, number, updateFunction, index)}
        max={max}
        step={step}
        min={min}
        aria-label="Dpll Bandwidth"
        className="relative flex items-center select-none touch-none w-64 h-5"
    >
        <Slider.Track className="bg-gray-300 relative grow rounded-full h-1">
            <Slider.Range className="absolute bg-blue-500 rounded-full h-full" />
        </Slider.Track>
        <Slider.Thumb className="block w-4 h-4 bg-white border border-gray-400 rounded-full shadow hover:bg-gray-100" />
    </Slider.Root>);
}

const handleChange = (dispatch:Dispatch, number: number[], updateFunction: (data: string) => Promise<responseDataType>, index:number) => {
    console.log(number);
    const data = { key: "" + number[0], value: "" + number[0] };
    updateFunction(JSON.stringify(data)).then(dt=>{
          dispatch(updateSliderValue({index:index, value:Number(dt.value)}))
        }
    );
}
export default DynamicSlider;