import { createSlice } from "@reduxjs/toolkit";

const indexUrlMapSlice = createSlice({
    name: 'indexUrlMap',
    initialState: {
        value: [],
    },
    reducers: {
        setIndexUrlMap: (state, action) => {
            state.value = action.payload
        }
    }
});

export const { setIndexUrlMap } = indexUrlMapSlice.actions;
export default indexUrlMapSlice.reducer;