
import { useDispatch, useSelector } from "react-redux";
import DataRow from "../DataRow";
import Header from "../Header";
import PaddingRow from "../PaddingRow";
import Page from "../Page";
import { useNavigate } from "react-router-dom";
import { setIndexUrlMap } from "../../state-repo/slices/indexUrlMap";
import { useEffect } from "react";


const DspSettings = () => {
    const navigate = useNavigate();
    const index = useSelector((state:{ navigationIndex: { value: number } }) => state.navigationIndex.value);
    const dispatch = useDispatch();
    useEffect(() => {
        const indexMap = [
            { index: 0, url: "/Input" },
            { index: 1, url: "/Output" },
            { index: 2, url: "/Settings" }
        ];

        dispatch(setIndexUrlMap(indexMap));

    }, []);
    const components = [
        <Header text="Dsp Settings" />,
        < PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/Input")} text="Input" type={1} active={index == 0} description=""/>,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/Output")} text="Output" type={1} active={index == 1} description=""/>,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/Settings")} text="Back" type={2} active={index == 2} description=""/>,
    ];
    return <Page items={components} />
}

export default DspSettings;