
import { useDispatch, useSelector } from "react-redux";
import DataRow from "../DataRow";
import Header from "../header";
import PaddingRow from "../PaddingRow";
import Page from "../Page";
import { useNavigate } from "react-router-dom";
import { setIndexUrlMap } from "../../state-repo/slices/indexUrlMap";


const GeneralSettings = () => {
    const navigate = useNavigate();
    const index = useSelector((state) => state.navigationIndex.value);
    const dispatch = useDispatch();
    const indexMap = useSelector((state) => state.indexUrlMap.value)
    const indexMap2 = [
        { index: 0, url: "/VolumeDevice" },
        { index: 1, url: "/VolumeAlgorithm" },
        { index: 2, url: "/SoundModes" },
        { index: 3, url: "/Settings" }
    ];
    if (indexMap[0]?.url != indexMap2[0].url) {
        dispatch(setIndexUrlMap(indexMap2));
    }
    const components = [
        <Header text="General Settings" />,
        < PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/VolumeDevice")} text="Volume Device" type={1} active={index == 0} />,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/VolumeAlgorithm")} text="Volume Algorithm" type={1} active={index == 1} />,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/SoundModes")} text="Sound Modes" type={1} active={index == 2} />,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/Settings")} text="Back" type={2} active={index == 3} />,
    ];
    return <Page items={components} />
}

export default GeneralSettings;