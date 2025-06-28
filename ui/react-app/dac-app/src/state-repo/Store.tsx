import { configureStore } from "@reduxjs/toolkit";
import volumeReducer from "./slices/volumeSlice";
import homeDataReducer from "./slices/homeDataSlice";
import webSocketReducer from "./slices/webSocketSlice";
import navigationIndexReducer from "./slices/navigationIndex";
import indexUrlMapReducer from "./slices/indexUrlMap";
import dynamicComponentsDataSlice from "./slices/dynamicComponentsDataSlice";
import selectedIndexSlice from "./slices/selectedIndexSlice";
export default configureStore({
    reducer:
    {
        volume: volumeReducer,
        homeData: homeDataReducer,
        messages: webSocketReducer,
        lastMessage: webSocketReducer,
        navigationIndex: navigationIndexReducer,
        indexUrlMap: indexUrlMapReducer,
        dynamicComponentsData: dynamicComponentsDataSlice,
        selectedIndex: selectedIndexSlice
    }
});