
import { useDispatch, useSelector } from "react-redux";
import DataRow from "../DataRow";
import Header from "../Header";
import PaddingRow from "../PaddingRow";
import Page from "../Page";
import { useNavigate } from "react-router-dom";
import { setIndexUrlMap } from "../../state-repo/slices/indexUrlMap";
import { useEffect } from "react";


const ThdCompensation = () => {
    const navigate = useNavigate();
    const index = useSelector((state:{ navigationIndex: { value: number } }) => state.navigationIndex.value);
    const dispatch = useDispatch();
    useEffect(() => {
        const indexMap = [
            { index: 0, url: "/SecondOrderCompensation" },
            { index: 1, url: "/ThirdOrderCompensation" },
            { index: 2, url: "/DacSettings" },];
        dispatch(setIndexUrlMap(indexMap));
    }, []);

    const components = [
        <Header text="Thd Compensation" />,
        < PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/SecondOrderCompensation")} text="2ND Order" type={1} active={index == 0} description=""/>,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/ThirdOrderCompensation")} text="3RD Order" type={1} active={index == 1} description=""/>,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/DacSettings")} text="Back" type={2} active={index == 2} description=""/>,
    ];
    return <Page items={components} />
}

export default ThdCompensation;