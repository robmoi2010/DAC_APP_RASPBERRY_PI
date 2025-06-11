
import { useDispatch, useSelector } from "react-redux";
import DataRow from "../DataRow";
import Header from "../header";
import PaddingRow from "../PaddingRow";
import Page from "../Page";
import { useNavigate, type NavigateFunction } from "react-router-dom";
import { setIndexUrlMap } from "../../state-repo/slices/indexUrlMap";
import { type ReactElement, useEffect } from "react";
import { getVolumeModes, updateVolumeModes } from "../../services/DacService";
import type { indexMapType, responseDataType } from "../../utils/types";
import { setComponentsData } from "../../state-repo/slices/dynamicComponentsDataSlice";


const VolumeModes = () => {
    const navigate: NavigateFunction = useNavigate();
    const index = useSelector((state) => state.navigationIndex.value);
    const selectedIndex = useSelector((state) => state.selectedIndex.value);
    const componentsData = useSelector((state) => state.dynamicComponentsData.value);
    const dispatch = useDispatch();
    useEffect(() => {
        const indexMap: indexMapType[] = [];
        const components: responseDataType[] = [];
        indexMap.push({ index: 0, url: "" });
        indexMap.push({ index: 1, url: "" });
        indexMap.push({ index: 2, url: "/DacSettings" });
        dispatch(setIndexUrlMap(indexMap))
        const status = getVolumeModes();
        let disabled = false;
        status.then(data => {
            console.log(data);
            disabled = data.value;
        });
        const enableVal = ((disabled) ? "0" : "1");
        const disableVal = ((disabled) ? "1" : "0");
        components.push({ key: "0", value: enableVal, display_name: "Mute" });
        components.push({ key: "1", value: disableVal, display_name: "Enable/DIsable Volume" });
        dispatch(setComponentsData(components));
    }, []);

    useEffect(() => {
        console.log(selectedIndex);
        if (selectedIndex != -1) {
            handleSelection(selectedIndex);
        }
    }, [selectedIndex]);
    return <Page items={generateComponents(componentsData, index, navigate)} />
}
const generateComponents = (data: responseDataType[], index: number, navigate: NavigateFunction) => {
    const components: ReactElement[] = [];
    components.push(<Header text="Volume Settings" />);
    components.push(<PaddingRow />);
    data.forEach(x => {
        components.push(<DataRow selected={x?.value == "1"} onClick={() => handleSelection(x.key)} text={x?.display_name} type={1} active={index == x?.key} />);
        components.push(<PaddingRow />);
    });
    components.push(<DataRow selected={false} onClick={() => navigate("/DacSettings")} text="Back" type={2} active={index == data.length} />);
    return components;
}
const handleSelection = (selection: number) => {
    const data = { key: selection, value: selection };
    updateVolumeModes(JSON.stringify(data));
}


export default VolumeModes;