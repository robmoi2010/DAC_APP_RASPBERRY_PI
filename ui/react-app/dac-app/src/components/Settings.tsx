
import { useDispatch, useSelector } from "react-redux";
import DataRow from "./DataRow";
import Header from "./header";
import PaddingRow from "./PaddingRow";
import Page from "./Page";
import { useNavigate } from "react-router-dom";
import { useEffect } from "react";
import { setTotalItems } from "../state-repo/slices/totalIemsSlice";
import { setNextUrl } from "../state-repo/slices/nextUrl";
const Settings = () => {
    const navigate = useNavigate();
    const index = useSelector((state) => state.navigationIndex.value);
    const dispatch = useDispatch();

    // set total items that will be displayed by the component
    dispatch(setTotalItems(4));
    //listen for changes in index state and update url
    useEffect(() => {
        let url = "";
        switch (index) {
            case 0: {
                url = "/DacSettings";
                break;
            }
            case 1: {
                url = "/DspSettings";
                break;
            }
            case 2: {
                url = "/GeneralSettings";
                break;
            }
            case 3: {
                url = "/Home";
                break;
            }
        }
        dispatch(setNextUrl(url));
    }, [index]);

    const components = [
        <Header text="Settings" />,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/DacSettings")} text="DacSettings" type={1} active={index == 0} />,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/DspSettings")} text="DspSettings" type={1} active={index == 1} />,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/GeneralSettings")} text="GeneralSettings" type={1} active={index == 2} />,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/Home")} text="Back" type={2} active={index == 3} />,
    ];
    return <Page items={components} />
}

export default Settings;