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