
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