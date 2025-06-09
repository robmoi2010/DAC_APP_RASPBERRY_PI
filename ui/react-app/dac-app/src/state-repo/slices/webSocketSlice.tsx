import { createSlice } from '@reduxjs/toolkit';

const webSocketSlice = createSlice({
  name: 'websocket',
  initialState: {
    messages: [],
    lastMessage: null,
  },
  reducers: {
    addMessage: (state, action) => {
      state.messages.push(action.payload);
      state.lastMessage = action.payload;
    },
    clearMessages: (state) => {
      state.messages = [];
      state.lastMessage = null;
    },
  },
});

export const { addMessage, clearMessages } = webSocketSlice.actions;
export default webSocketSlice.reducer;