
import { useDispatch, useSelector } from "react-redux";
import DataRow from "../DataRow";
import Header from "../Header";
import PaddingRow from "../PaddingRow";
import Page from "../Page";
import { useNavigate } from "react-router-dom";
import { setIndexUrlMap } from "../../state-repo/slices/indexUrlMap";
import { useEffect } from "react";


const SystemSettings = () => {
    const navigate = useNavigate();
    const index = useSelector((state:{ navigationIndex: { value: number } }) => state.navigationIndex.value);
    const dispatch = useDispatch();
    useEffect(() => {
        const indexMap = [
            { index: 0, url: "/VolumeDevice" },
            { index: 1, url: "/VolumeAlgorithm" },
            { index: 2, url: "/SoundModes" },
            { index: 3, url: "/Settings" }
        ];
        dispatch(setIndexUrlMap(indexMap));
    }, []);
    const components = [
        <Header text="System Settings" />,
        < PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/VolumeDevice")} text="Volume Device" type={1} active={index == 0} description=""/>,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/VolumeAlgorithm")} text="Volume Algorithm" type={1} active={index == 1} description=""/>,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/SoundModes")} text="Sound Modes" type={1} active={index == 2} description=""/>,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/Settings")} text="Back" type={2} active={index == 3} description=""/>,
    ];
    return <Page items={components} />
}

export default SystemSettings;