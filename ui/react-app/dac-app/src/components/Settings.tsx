
import { useDispatch, useSelector } from "react-redux";
import DataRow from "./DataRow";
import Header from "./Header";
import PaddingRow from "./PaddingRow";
import Page from "./Page";
import { useNavigate } from "react-router-dom";
import { setIndexUrlMap } from "../state-repo/slices/indexUrlMap";
import { useEffect } from "react";
import { Slider } from "@radix-ui/themes/components/slider";


const Settings = () => {
    const navigate = useNavigate();
    const index = useSelector((state:{ navigationIndex: { value: number } }) => state.navigationIndex.value);
    const dispatch = useDispatch();
    useEffect(() => {
        const indexMap = [
            { index: 0, url: "/DacSettings" },
            { index: 1, url: "/DspSettings" },
            { index: 2, url: "/SystemSettings" },
            { index: 3, url: "/Home" }];
        dispatch(setIndexUrlMap(indexMap));
    }, []);
    const components = [
        <Slider min={0} max={100}  onChange={() => { }} />,
        <Header text="Settings" />,
        < PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/DacSettings")} text="Dac Settings" type={1} active={index == 0} description=""/>,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/DspSettings")} text="Dsp Settings" type={1} active={index == 1} description=""/>,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/SystemSettings")} text="System Settings" type={1} active={index == 2} description=""/>,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/Home")} text="Back" type={2} active={index == 3} description="" />,
    ];
    return <Page items={components} />
}

export default Settings;