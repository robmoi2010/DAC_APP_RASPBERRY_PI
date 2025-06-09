import { createSlice } from "@reduxjs/toolkit";

const nextUrlSlice = createSlice({
    name: 'nextUrl',
    initialState: {
        value: "",
    },
    reducers: {
        setNextUrl: (state, action) => {
            state.value = action.payload
        }
    }
});

export const { setNextUrl } = nextUrlSlice.actions;
export default nextUrlSlice.reducer;