import Config from '../configs/Config.json'
import { sendGet, sendPut } from '../utils/RestClient'
export async function getHomeData() {
    return await sendGet(Config["BASE_URL"] + "system/home");
}
export const getVolumeDevice = () => {
    return sendGet(Config["BASE_URL"] + "system/volume_device");
}
export const updateVolumeDevice = (data: string) => {
    return sendPut(Config["BASE_URL"] + "system/volume_device", data);
}
export const getVolumeAlgorithm = () => {
    return sendGet(Config["BASE_URL"] + "system/volume_algorithm");
}
export const updateVolumeAlgorithm = (data: string) => {
    return sendPut(Config["BASE_URL"] + "system/volume_algorithm", data);
}

export const getSoundModes = () => {
    return sendGet(Config["BASE_URL"] + "system/sound_mode");
}
export const updateSoundMode = (data: string) => {
    return sendPut(Config["BASE_URL"] + "system/sound_mode", data);
}
export const increaseVolume = () => {
    return sendGet(Config["BASE_URL"] + "system/volume/up");
}
export const decreaseVolume = () => {
    return sendGet(Config["BASE_URL"] + "system/volume/down");
}
export const updateVolume = (data: string) => {
    return sendPut(Config["BASE_URL"] + "system/volume", data);
}
export const getVolumeRamp = () => {
    return sendGet(Config["BASE_URL"] + "system/volume_ramp");
}
export const updateVolumeRamp = (data: string) => {
    return sendPut(Config["BASE_URL"] + "system/volume_ramp", data);
}