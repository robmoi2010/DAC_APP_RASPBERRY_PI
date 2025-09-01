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
import { sendGet, sendPut } from "../utils/RestClient";
import Config from "../configs/Config.json";
export const getFilters = () => {
    return sendGet(Config["BASE_URL"] + "dac/filters");
}
export const getVolumeDisableStatus = () => {
    return sendGet(Config["BASE_URL"] + "dac/volume/status");
}
export const updateFilter = (data: string) => {
    return sendPut(Config["BASE_URL"] + "dac/filters", data);
}
export const updateVolumeStatus = (data: string) => {
    return sendPut(Config["BASE_URL"] + "dac/volume/status", data);
}
export const getDacModes = () => {
    return sendGet(Config["BASE_URL"] + "dac/dac_modes");
}
export const updateDacMode = (data: string) => {
    return sendPut(Config["BASE_URL"] + "dac/dac_modes", data);
}
export const getVolumeModes = () => {
    return sendGet(Config["BASE_URL"] + "dac/volume_modes");
}
export const updateVolumeModes = (data: string) => {
    return sendPut(Config["BASE_URL"] + "dac/volume_modes", data);
}
export const getSecondOrderStatus = () => {
    return sendGet(Config["BASE_URL"] + "dac/thd_compensation/second_order/status");
}
export const updateSecondOrderStatus = (data: string) => {
    return sendPut(Config["BASE_URL"] + "dac/thd_compensation/second_order/status", data);
}
export const getThirdOrderStatus = () => {
    return sendGet(Config["BASE_URL"] + "dac/thd_compensation/third_order/status");
}
export const updateThirdOrderStatus = (data: string) => {
    return sendPut(Config["BASE_URL"] + "dac/thd_compensation/third_order/status", data);
}
export const  getOversamplingStatus = async () => {
    return sendGet(Config["BASE_URL"] + "dac/oversampling/status");
}
export const updateOversamplingStatus = async (data: string) => {
    return sendPut(Config["BASE_URL"] + "dac/oversampling/status", data);
}

export const  getDpllBandwidth = async () => {
    return sendGet(Config["BASE_URL"] + "dac/dpll_bandwidth");
}
export const updateDpllBandwidth = async (data: string) => {
    return sendPut(Config["BASE_URL"] + "dac/dpll_bandwidth", data);
}