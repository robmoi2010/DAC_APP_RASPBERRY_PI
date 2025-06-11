
import { useDispatch, useSelector } from "react-redux";
import DataRow from "../DataRow";
import Header from "../header";
import PaddingRow from "../PaddingRow";
import Page from "../Page";
import { useNavigate, type NavigateFunction } from "react-router-dom";
import { setIndexUrlMap } from "../../state-repo/slices/indexUrlMap";
import { type ReactElement, useEffect } from "react";
import { getDacModes, updateDacMode } from "../../services/DacService";
import type { indexMapType, responseDataType } from "../../utils/types";
import { setComponentsData } from "../../state-repo/slices/dynamicComponentsDataSlice";


const DacModes = () => {
    const navigate: NavigateFunction = useNavigate();
    const index = useSelector((state) => state.navigationIndex.value);
    const selectedIndex = useSelector((state) => state.selectedIndex.value);
    const componentsData = useSelector((state) => state.dynamicComponentsData.value);
    const dispatch = useDispatch();
    useEffect(() => {
        const indexMap: indexMapType[] = [];
        const modes = getDacModes();
        modes.then(data => {
            data.forEach(d => {
                indexMap.push({ index: d.key, url: "" });
            });
            indexMap.push({ index: 2, url: "/DacSettings" });
            dispatch(setIndexUrlMap(indexMap))
            dispatch(setComponentsData(data));
        });
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
    components.push(<Header text="Dac Modes" />);
    components.push(<PaddingRow />);
    data.forEach(x => {
        components.push(<DataRow selected={x?.value == "1"} onClick={() => handleSelection(Number(x.key))} text={x?.display_name} type={1} active={index == Number(x?.key)} />);
        components.push(<PaddingRow />);
    });
    components.push(<DataRow selected={false} onClick={() => navigate("/DacSettings")} text="Back" type={2} active={index == data.length} />);
    return components;
}
const handleSelection = (selection: number) => {
    const data = { key: selection, value: selection };
    updateDacMode(JSON.stringify(data));
}


export default DacModes;