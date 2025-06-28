import { createSlice } from "@reduxjs/toolkit";
export const volumeSlice = createSlice({
    name: "volume",
    initialState:
    {
        value: 0,
    },
    reducers: {
        setVolume: (state, action) => {
            state.value = action.payload
        }
    }
});
export const { setVolume } = volumeSlice.actions;
export default volumeSlice.reducer;