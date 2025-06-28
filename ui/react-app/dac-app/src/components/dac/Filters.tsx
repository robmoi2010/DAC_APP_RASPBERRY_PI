
import { useDispatch, useSelector } from "react-redux";
import DataRow from "../DataRow";
import Header from "../header";
import PaddingRow from "../PaddingRow";
import Page from "../Page";
import { useNavigate, type NavigateFunction } from "react-router-dom";
import { getFilters, updateFilter } from "../../services/DacService";
import { type ReactElement, useEffect } from "react";
import { type responseDataType } from "../../utils/types";
import type { Dispatch } from "redux";
import { loadDynamicData } from "../../utils/dataUtil";
import { setComponentsData } from "../../state-repo/slices/dynamicComponentsDataSlice";

const Filters = () => {
    const navigate = useNavigate();
    const index = useSelector((state) => state.navigationIndex.value);
    const selectedIndex = useSelector((state) => state.selectedIndex.value);
    const componentsData = useSelector((state) => state.dynamicComponentsData.value);
    const dispatch = useDispatch();
    //initial data load
    useEffect(() => {
        loadDynamicData(getFilters(), dispatch, "/DacSettings");
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
    components.push(<Header text="Filters" />);
    components.push(<PaddingRow />);
    data.forEach(x => {
        components.push(<DataRow selected={x?.value == "1"} onClick={() => dataSelection(Number(x?.key), dispatch)} text={x?.display_name} type={1} active={index == Number(x?.key)} />);
        components.push(<PaddingRow />);
    });
    components.push(<DataRow selected={false} onClick={() => navigate("/DacSettings")} text="Back" type={2} active={index == data.length} />);
    return components;
}
const dataSelection = (selection: number, dispatch: Dispatch) => {
    updateFilter(JSON.stringify({ key: "" + selection, value: "" + selection })).then(
        data => {
            dispatch(setComponentsData(data));
        }
    );
}



export default Filters;