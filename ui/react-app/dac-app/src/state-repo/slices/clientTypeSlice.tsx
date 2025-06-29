import { ClientType } from "../../utils/types";
import { createSlice } from "@reduxjs/toolkit";

const clientTypeSlice = createSlice({
    name: 'clientType',
    initialState: {
        value: ClientType.DEVICE,
    },
    reducers: {
        setClientType: (state, action) => {
            state.value = action.payload
        }
    }
});

export const { setClientType } = clientTypeSlice.actions;
export default clientTypeSlice.reducer;