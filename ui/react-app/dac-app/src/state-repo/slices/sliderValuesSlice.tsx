import { createSlice, type PayloadAction } from "@reduxjs/toolkit";
interface MapState {
    items: { [key: string]: number };
}
const initialState: MapState = {
    items: {}
};
export const sliderValuesSlice = createSlice({
    name: "sliderValues",
    initialState,
    reducers: {
        updateSliderValue: (state, action: PayloadAction<{ key: string; value: number }>) => {
            const { key, value } = action.payload;
            state.items[key] = value;
        },
    }
});
export const { updateSliderValue } = sliderValuesSlice.actions;
export default sliderValuesSlice.reducer;