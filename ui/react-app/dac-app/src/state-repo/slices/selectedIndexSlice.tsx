import { createSlice } from "@reduxjs/toolkit";
export const selectedIndexSlice = createSlice({
    name: "selectedIndex",
    initialState:
    {
        value: -1,
    },
    reducers: {
        setSelectedIndex: (state, action) => {
            state.value = action.payload
        }
    }
});
export const { setSelectedIndex } = selectedIndexSlice.actions;
export default selectedIndexSlice.reducer;