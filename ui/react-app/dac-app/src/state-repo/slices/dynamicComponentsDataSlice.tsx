import { createSlice } from "@reduxjs/toolkit";

const dynamicComponentsDataSlice = createSlice({
    name: 'dynamicComponentsData',
    initialState: {
        value: [],
    },
    reducers: {
        setComponentsData: (state, action) => {
            state.value = action.payload
        }
    }
});

export const { setComponentsData } = dynamicComponentsDataSlice.actions;
export default dynamicComponentsDataSlice.reducer;