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