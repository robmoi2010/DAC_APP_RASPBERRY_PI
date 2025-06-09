import { configureStore } from "@reduxjs/toolkit";
import volumeReducer from "./slices/volumeSlice";
import homeDataReducer from "./slices/homeDataSlice";
import webSocketReducer from "./slices/webSocketSlice";
import navigationIndexReducer from "./slices/navigationIndex";
import totalItemsReducer from "./slices/totalIemsSlice";
import nextUrlReducer from "./slices/nextUrl"
export default configureStore({
    reducer:
    {
        volume: volumeReducer,
        homeData: homeDataReducer,
        messages: webSocketReducer,
        lastMessage: webSocketReducer,
        navigationIndex: navigationIndexReducer,
        totalItems: totalItemsReducer,
        nextUrl: nextUrlReducer
    }
});