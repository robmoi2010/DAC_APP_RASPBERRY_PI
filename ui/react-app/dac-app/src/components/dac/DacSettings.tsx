/*
 * Copyright (C) 2025 Robert Moi, Goglotek LTD
 *
 *  This file is part of the DAC_APPLICATION System.
 *
 *  The DAC_APPLICATION System is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  The DAC_APPLICATION is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with the DAC_APPLICATION. If not, see <https://www.gnu.org/licenses/>
 */
import { useDispatch, useSelector } from "react-redux";
import DataRow from "../DataRow";
import Header from "../Header";
import PaddingRow from "../PaddingRow";
import Page from "../Page";
import { useNavigate } from "react-router-dom";
import { setIndexUrlMap } from "../../state-repo/slices/indexUrlMap";
import { useEffect } from "react";


const DacSettings = () => {
    const navigate = useNavigate();
    const index = useSelector((state:{ navigationIndex: { value: number } }) => state.navigationIndex.value);
    const dispatch = useDispatch();
    useEffect(() => {
        const indexMap = [
            { index: 0, url: "/VolumeSettings" },
            { index: 1, url: "/Filters" },
            { index: 2, url: "/DacModes" },
            { index: 3, url: "/VolumeModes" },
            { index: 4, url: "/ThdCompensation" },
            { index: 5, url: "/Oversampling" },
            { index: 6, url: "/Settings" },];
        dispatch(setIndexUrlMap(indexMap));
    }, []);

    const components = [
        <Header text="Dac Settings" />,
        < PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/VolumeSettings")} text="Volume Settings" type={1} active={index == 0} description=""/>,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/Filters")} text="Filters" type={1} active={index == 1} description=""/>,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/DacModes")} text="DAC Modes" type={1} active={index == 2} description=""/>,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/VolumeModes")} text="Volume Mode" type={1} active={index == 3} description=""/>,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/ThdCompensation")} text="THD Compensation" type={1} active={index == 4} description=""/>,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/Oversampling")} text="Oversampling" type={1} active={index == 5} description=""/>,
        <PaddingRow />,
        <DataRow selected={false} onClick={() => navigate("/Settings")} text="Back" type={2} active={index == 6} description=""/>,
    ];
    return <Page items={components} />
}

export default DacSettings;