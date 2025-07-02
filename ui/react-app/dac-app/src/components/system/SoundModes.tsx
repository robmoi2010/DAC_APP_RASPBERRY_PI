
import { useDispatch, useSelector } from "react-redux";
import DataRow from "../DataRow";
import Header from "../Header";
import PaddingRow from "../PaddingRow";
import Page from "../Page";
import { useNavigate, type NavigateFunction } from "react-router-dom";
import { type ReactElement, useEffect } from "react";
import type { responseDataType } from "../../utils/types";
import { loadDynamicData } from "../../utils/dataUtil";
import type { Dispatch } from "redux";
import { setComponentsData } from "../../state-repo/slices/dynamicComponentsDataSlice";
import { getSoundModes, updateSoundMode } from "../../services/SystemService";


const SoundModes = () => {
    const navigate: NavigateFunction = useNavigate();
    const index = useSelector((state:{ navigationIndex: { value: number } }) => state.navigationIndex.value);
    const selectedIndex = useSelector((state:{ selectedIndex: { value: number } }) => state.selectedIndex.value);
    const componentsData = useSelector((state:{ dynamicComponentsData: { value: [] } }) => state.dynamicComponentsData.value);
    const dispatch = useDispatch();
    useEffect(() => {
        //clear previous data if present before fetching new data
        dispatch(setComponentsData([]));
        loadDynamicData(getSoundModes(), dispatch, "/SystemSettings");
    }, []);

    useEffect(() => {
        if (selectedIndex != -1) {
            dataSelection(selectedIndex, dispatch);
        }
    }, [selectedIndex, dispatch]);
    return <Page items={generateComponents(componentsData, index, navigate, dispatch)} />
}
const generateComponents = (data: responseDataType[], index: number, navigate: NavigateFunction, dispatch: Dispatch) => {
    const components: ReactElement[] = [];
    components.push(<Header text="Sound Modes" />);
    components.push(<PaddingRow />);
    data.forEach(x => {
        components.push(<DataRow selected={x?.value == "1"} onClick={() => dataSelection(Number(x.key), dispatch)} text={x?.display_name} type={1} active={index == Number(x?.key)} description={x?.description}/>);
        components.push(<PaddingRow />);
    });
    components.push(<DataRow selected={false} onClick={() => navigate("/SystemSettings")} text="Back" type={2} active={index == data.length} description=""/>);
    return components;
}
const dataSelection = (selection: number, dispatch: Dispatch) => {
    updateSoundMode(JSON.stringify({ key: "" + selection, value: "" + selection })).then(
        data => {
            dispatch(setComponentsData(data));
        }
    );
}


export default SoundModes;