
import { useDispatch, useSelector } from "react-redux";
import DataRow from "../DataRow";
import Header from "../Header";
import PaddingRow from "../PaddingRow";
import Page from "../Page";
import { useNavigate, type NavigateFunction } from "react-router-dom";
import { setIndexUrlMap } from "../../state-repo/slices/indexUrlMap";
import { type ReactElement, useEffect } from "react";
import { getVolumeDisableStatus, updateVolumeStatus } from "../../services/DacService";
import type { indexMapType, responseDataType } from "../../utils/types";
import { setComponentsData } from "../../state-repo/slices/dynamicComponentsDataSlice";
import type { Dispatch } from "redux";


const VolumeSettings = () => {
    const navigate: NavigateFunction = useNavigate();
    const index = useSelector((state:{ navigationIndex: { value: number } }) => state.navigationIndex.value);
    const selectedIndex = useSelector((state:{ selectedIndex: { value: number } }) => state.selectedIndex.value);
    const componentsData = useSelector((state:{ dynamicComponentsData: { value: [] } }) => state.dynamicComponentsData.value);
    const dispatch = useDispatch();
    useEffect(() => {
        const indexMap: indexMapType[] = [];
        indexMap.push({ index: 0, url: "" });
        indexMap.push({ index: 1, url: "" });
        indexMap.push({ index: 2, url: "/DacSettings" });
        dispatch(setIndexUrlMap(indexMap))
        const status = getVolumeDisableStatus();
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
    components.push(<Header text="Volume Settings" />);
    components.push(<PaddingRow />);
    data.forEach(x => {
        components.push(<DataRow selected={x?.value == "1"} onClick={() => handleSelection(Number(x.key), dispatch)} text={x?.display_name} type={1} active={index == Number(x?.key)} description={x?.description} />);
        components.push(<PaddingRow />);
    });
    components.push(<DataRow selected={false} onClick={() => navigate("/DacSettings")} text="Back" type={2} active={index == data.length} description=""/>);
    return components;
}
const handleSelection = (selection: number, dispatch: Dispatch) => {
    const data = { key: "" + selection, value: "" + selection };
    const response = updateVolumeStatus(JSON.stringify(data))
    processData(response, dispatch);
}
const processData = (data: Promise<responseDataType>, dispatch: Dispatch) => {
    const components: responseDataType[] = [];
    data.then(dt => {
        components.push({ key: "0", value: (dt.value == "1") ? "0" : "1", display_name: "Enable", description:"" });
        components.push({ key: "1", value: (dt.value == "0") ? "0" : "1", display_name: "Disable",description:"" });
        dispatch(setComponentsData(components));
    });
}


export default VolumeSettings;