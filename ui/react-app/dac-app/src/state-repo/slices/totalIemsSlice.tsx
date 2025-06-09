import { createSlice } from "@reduxjs/toolkit";
export const totalItemsSlice = createSlice({
    name: "totalItems",
    initialState:
    {
        value: 0,
    },
    reducers: {
        setTotalItems: (state, action) => {
            state.value = action.payload
        }
    }
});
export const { setTotalItems } = totalItemsSlice.actions;
export default totalItemsSlice.reducer;