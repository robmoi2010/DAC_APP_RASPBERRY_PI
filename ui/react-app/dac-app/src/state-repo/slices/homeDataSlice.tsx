import { createSlice } from "@reduxjs/toolkit";

export const homeDataSlice = createSlice({
    name: "homeData",
    initialState:
    {
        value: "",
    },
    reducers: {
        setHomeData: (state, action) => {
            state.value = action.payload
        }
    }
});
export const { setHomeData } = homeDataSlice.actions;
export default homeDataSlice.reducer;