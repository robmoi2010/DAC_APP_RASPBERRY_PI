
import { useDispatch, useSelector } from "react-redux";
import DataRow from "../DataRow";
import Header from "../header";
import PaddingRow from "../PaddingRow";
import Page from "../Page";
import { useNavigate } from "react-router-dom";
import { setIndexUrlMap } from "../../state-repo/slices/indexUrlMap";
import { useEffect } from "react";


const DacSettings = () => {
    const navigate = useNavigate();
    const index = useSelector((state) => state.navigationIndex.value);
    const dispatch = useDispatch();
    useEffect(() => {
        const indexMap = [
            { index: 0, url: "/VolumeSettings" },
            { index: 1, url: "/Filters" },
            { index: 2, url: "/DacModes" },
            { index: 3, url: "/VolumeMode" },
            { index: 4, url: "/ThdCompensation" },
            { index: 5, url: "/Settings" },];
        dispatch(setIndexUrlMap(indexMap));
    }, []);

    const components = [
        <Header text="Dac Settings" />,
        < PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/VolumeSettings")} text="Volume Settings" type={1} active={index == 0} />,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/Filters")} text="Filters" type={1} active={index == 1} />,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/DacModes")} text="DAC Modes" type={1} active={index == 2} />,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/VolumeMode")} text="Volume Mode" type={1} active={index == 3} />,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/ThdCompensation")} text="THD Compensation" type={1} active={index == 4} />,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/Settings")} text="Back" type={2} active={index == 5} />,
    ];
    return <Page items={components} />
}

export default DacSettings;