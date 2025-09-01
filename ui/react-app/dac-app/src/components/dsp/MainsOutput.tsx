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
import { useDispatch, useSelector } from "react-redux";
import DataRow from "../DataRow";
import Header from "../Header";
import PaddingRow from "../PaddingRow";
import Page from "../Page";
import { useNavigate, type NavigateFunction } from "react-router-dom";
import { type ReactElement, useEffect } from "react";
import { type responseDataType } from "../../utils/types";
import type { Dispatch } from "redux";
import { loadDynamicData } from "../../utils/dataUtil";
import { setComponentsData } from "../../state-repo/slices/dynamicComponentsDataSlice";
import { getMainsOutputOptions, updateMainsOutput } from "../../services/DspService";

const MainsOutput = () => {
    const navigate = useNavigate();
    const index = useSelector((state:{ navigationIndex: { value: number } }) => state.navigationIndex.value);
    const selectedIndex = useSelector((state:{ selectedIndex: { value: number } }) => state.selectedIndex.value);
    const componentsData = useSelector((state:{ dynamicComponentsData: { value: [] } }) => state.dynamicComponentsData.value);
    const dispatch = useDispatch();
    //initial data load
    useEffect(() => {
        //clear previous data if present before fetching new data
        dispatch(setComponentsData([]));
        loadDynamicData(getMainsOutputOptions(), dispatch, "/Output");
    }, []);
    //capture selected index update and send value to server
    useEffect(() => {
        if (selectedIndex != -1) {
            dataSelection(selectedIndex, dispatch);
        }
    }, [selectedIndex, dispatch]);
    return <Page items={generateComponents(componentsData, index, navigate, dispatch)} />
}
const generateComponents = (data: responseDataType[], index: number, navigate: NavigateFunction, dispatch: Dispatch) => {
    const components: ReactElement[] = [];
    components.push(<Header text="Select Mains Output" />);
    components.push(<PaddingRow />);
    data.forEach(x => {
        components.push(<DataRow selected={x?.value == "1"} onClick={() => dataSelection(Number(x?.key), dispatch)} text={x?.display_name} type={1} active={index == Number(x?.key)} description={x?.description}/>);
        components.push(<PaddingRow />);
    });
    components.push(<DataRow selected={false} onClick={() => navigate("/Output")} text="Back" type={2} active={index == data.length} description=""/>);
    return components;
}
const dataSelection = (selection: number, dispatch: Dispatch) => {
    updateMainsOutput(JSON.stringify({ key: "" + selection, value: "" + selection })).then(
        data => {
            dispatch(setComponentsData(data));
        }
    );
}
export default MainsOutput;