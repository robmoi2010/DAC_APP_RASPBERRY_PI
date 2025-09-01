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