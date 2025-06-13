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
    console.log(data);
    return sendPut(Config["BASE_URL"] + "dac/thd_compensation/second_order/status", data);
}
export const getThirdOrderStatus = () => {
    return sendGet(Config["BASE_URL"] + "dac/thd_compensation/third_order/status");
}
export const updateThirdOrderStatus = (data: string) => {
    console.log(data);
    return sendPut(Config["BASE_URL"] + "dac/thd_compensation/third_order/status", data);
}