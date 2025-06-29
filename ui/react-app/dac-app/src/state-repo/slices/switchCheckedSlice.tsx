import { createSlice, type PayloadAction } from "@reduxjs/toolkit";
interface BoolArrayState {
    items: boolean[];
}
const initialState: BoolArrayState = {
    items: [],
};
export const switchCheckedSlice = createSlice({
    name: "switchChecked",
    initialState,
    reducers: {
        setSwitchChecked: (state, action) => {
            state.items = action.payload
        },
        updateSwitchChecked: (state, action: PayloadAction<{ index: number; value: boolean }>) => {
            const { index, value } = action.payload;
            state.items[index] = value;
        },
        addSwitchChecked: (state, action: PayloadAction<boolean>) => {
            state.items.push(action.payload);
        }
    }
});
export const { setSwitchChecked, updateSwitchChecked, addSwitchChecked } = switchCheckedSlice.actions;
export default switchCheckedSlice.reducer;