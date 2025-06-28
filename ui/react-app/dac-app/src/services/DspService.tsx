import { sendGet, sendPut } from "../utils/RestClient";
import Config from "../configs/Config.json";
export const getInputOptions = () => {
    return sendGet(Config["BASE_URL"] + "dsp/input");
}
export const updateInput = (data: string) => {
    return sendPut(Config["BASE_URL"] + "dsp/input", data);
}
export const getMainsOutputOptions = () => {
    return sendGet(Config["BASE_URL"] + "dsp/output/mains");
}
export const updateMainsOutput = (data: string) => {
    return sendPut(Config["BASE_URL"] + "dsp/output/mains", data);
}
export const getSubwooferOutputOptions = () => {
    return sendGet(Config["BASE_URL"] + "dsp/output/subwoofer");
}
export const updateSubwooferOutput = (data: string) => {
    return sendPut(Config["BASE_URL"] + "dsp/output/subwoofer", data);
}