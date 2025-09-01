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
import { setIndexUrlMap } from "../../state-repo/slices/indexUrlMap";
import { type ReactElement, useEffect } from "react";
import { getThirdOrderStatus, updateThirdOrderStatus } from "../../services/DacService";
import type { indexMapType, responseDataType } from "../../utils/types";
import { setComponentsData } from "../../state-repo/slices/dynamicComponentsDataSlice";
import type { Dispatch } from "redux";


const ThirdOrderCompensation = () => {
    const navigate: NavigateFunction = useNavigate();
    const index = useSelector((state:{ navigationIndex: { value: number } }) => state.navigationIndex.value);
    const selectedIndex = useSelector((state:{ selectedIndex: { value: number } }) => state.selectedIndex.value);
    const componentsData = useSelector((state:{ dynamicComponentsData: { value: [] } }) => state.dynamicComponentsData.value);
    const dispatch = useDispatch();
    useEffect(() => {
        const indexMap: indexMapType[] = [];
        indexMap.push({ index: 0, url: "" });
        indexMap.push({ index: 1, url: "" });
        indexMap.push({ index: 2, url: "/ThdCompensation" });
        dispatch(setIndexUrlMap(indexMap))
        const status = getThirdOrderStatus();
        processData(status, dispatch);
    }, []);

    useEffect(() => {
        if (selectedIndex != -1) {
            handleSelection(selectedIndex, dispatch);
        }
    }, [selectedIndex, dispatch]);
    return <Page items={generateComponents(componentsData, index, navigate, dispatch)} />
}
const generateComponents = (data: responseDataType[], index: number, navigate: NavigateFunction, dispatch: Dispatch) => {
    const components: ReactElement[] = [];
    components.push(<Header text="3RD Order Compensation" />);
    components.push(<PaddingRow />);
    data.forEach(x => {
        components.push(<DataRow selected={x?.value == "1"} onClick={() => handleSelection(Number(x.key), dispatch)} text={x?.display_name} type={1} active={index == Number(x?.key)} description={x?.description} />);
        components.push(<PaddingRow />);
    });
    components.push(<DataRow selected={false} onClick={() => navigate("/ThdCompensation")} text="Back" type={2} active={index == data.length} description=""/>);
    return components;
}
const handleSelection = (selection: number, dispatch: Dispatch) => {
    const data = { key: "" + selection, value: "" + selection };
    const response = updateThirdOrderStatus(JSON.stringify(data))
    processData(response, dispatch);
}
const processData = (data: Promise<responseDataType>, dispatch: Dispatch) => {
    const components: responseDataType[] = [];
    data.then(dt => {
        components.push({ key: "0", value: (dt.value == "1") ? "1" : "0", display_name: "Enable", description:"" });
        components.push({ key: "1", value: (dt.value == "0") ? "1" : "0", display_name: "Disable", description:"" });
        dispatch(setComponentsData(components));
    });
}


export default ThirdOrderCompensation;