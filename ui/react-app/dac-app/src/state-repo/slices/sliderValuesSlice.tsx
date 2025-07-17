import { createSlice, type PayloadAction } from "@reduxjs/toolkit";
interface NumberArrayState {
    items: number[];
}
const initialState: NumberArrayState = {
    items: [],
};
export const sliderValuesSlice = createSlice({
    name: "sliderValues",
    initialState,
    reducers: {
        setSliderValues: (state, action) => {
            state.items = action.payload
        },
        updateSliderValue: (state, action: PayloadAction<{ index: number; value: number }>) => {
            const { index, value } = action.payload;
            state.items[index] = value;
        },
        addSliderValue: (state, action: PayloadAction<number>) => {
            state.items.push(action.payload);
        }
    }
});
export const { setSliderValues, updateSliderValue, addSliderValue } = sliderValuesSlice.actions;
export default sliderValuesSlice.reducer;