import { createSlice, type PayloadAction } from "@reduxjs/toolkit";
interface MapState {
    items: { [key: string]: boolean };
}
const initialState: MapState = {
    items: {}
};
export const updateSliderValuesSlice = createSlice({
    name: "updateSliderValues",
    initialState,
    reducers: {
        updateSliderValues: (state, action: PayloadAction<{ key: string; value: boolean }>) => {
            const { key, value } = action.payload;
            state.items[key] = value;
        },
    }
});
export const { updateSliderValues } = updateSliderValuesSlice.actions;
export default updateSliderValuesSlice.reducer;