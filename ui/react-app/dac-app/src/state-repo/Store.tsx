/*
 * Copyright (C) 2025 Robert Moi, Goglotek LTD
 *
 *  This file is part of the DAC_APPLICATION System.
 *
 *  The DAC_APPLICATION System is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  The DAC_APPLICATION is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with the DAC_APPLICATION. If not, see <https://www.gnu.org/licenses/>
 */
import { configureStore } from "@reduxjs/toolkit";
import volumeReducer from "./slices/volumeSlice";
import homeDataReducer from "./slices/homeDataSlice";
import webSocketReducer from "./slices/webSocketSlice";
import navigationIndexReducer from "./slices/navigationIndex";
import indexUrlMapReducer from "./slices/indexUrlMap";
import dynamicComponentsDataSlice from "./slices/dynamicComponentsDataSlice";
import selectedIndexSlice from "./slices/selectedIndexSlice";
import clientTypeSlice from "./slices/clientTypeSlice";
import switchCheckedSlice from "./slices/switchCheckedSlice";
import sliderValuesSlice from "./slices/sliderValuesSlice";
import updateSliderValuesSlice  from "./slices/updateSliderValuesSlice";
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
        selectedIndex: selectedIndexSlice,
        clientType:clientTypeSlice,
        switchChecked:switchCheckedSlice,
        sliderValues:sliderValuesSlice,
        updateSliderValues:updateSliderValuesSlice
    }
});