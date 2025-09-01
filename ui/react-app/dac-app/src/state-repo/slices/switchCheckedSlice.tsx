import { createSlice, type PayloadAction } from "@reduxjs/toolkit";
interface MapState {
    items: { [key: string]: boolean };
}
const initialState: MapState = {
    items: {},
};
export const switchCheckedSlice = createSlice({
    name: "switchChecked",
    initialState,
    reducers: {
        updateSwitchChecked: (state, action: PayloadAction<{ key: string; value: boolean }>) => {
            const { key, value } = action.payload;
            state.items[key] = value;
        }
    }
});
export const { updateSwitchChecked } = switchCheckedSlice.actions;
export default switchCheckedSlice.reducer;