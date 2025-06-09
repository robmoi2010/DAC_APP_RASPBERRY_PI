import { createSlice } from "@reduxjs/toolkit";
export const navigationIndexSlice = createSlice({
    name: "navigationIndex",
    initialState:
    {
        value: 0,
    },
    reducers: {
        increment: (state) => {
            state.value += 1;
        },
        setIndex: (state, action) => {
            state.value = action.payload;
        },
        decrement: (state) => {
            state.value -= 1;
        }
    }
});
export const { increment, decrement, setIndex } = navigationIndexSlice.actions;
export default navigationIndexSlice.reducer;