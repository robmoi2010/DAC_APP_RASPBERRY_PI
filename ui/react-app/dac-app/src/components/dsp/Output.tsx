
import { useDispatch, useSelector } from "react-redux";
import DataRow from "../DataRow";
import Header from "../header";
import PaddingRow from "../PaddingRow";
import Page from "../Page";
import { useNavigate } from "react-router-dom";
import { setIndexUrlMap } from "../../state-repo/slices/indexUrlMap";


const Output = () => {
    const navigate = useNavigate();
    const index = useSelector((state) => state.navigationIndex.value);
    const dispatch = useDispatch();
    const indexMap = useSelector((state) => state.indexUrlMap.value)
    const indexMap2 = [
        { index: 0, url: "/MainsOutput" },
        { index: 1, url: "/SubwooferOutput" },
        { index: 2, url: "/DspSettings" }
    ];
    if (indexMap[0]?.url != indexMap2[0].url) {
        dispatch(setIndexUrlMap(indexMap2));
    }
    const components = [
        <Header text="Dsp Settings" />,
        < PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/MainsOutput")} text="Mains Output" type={1} active={index == 0} />,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/SubwooferOutput")} text="Subwoofer Output" type={1} active={index == 1} />,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/DspSettings")} text="Back" type={2} active={index == 2} />,
    ];
    return <Page items={components} />
}

export default Output;