import Config from '../configs/Config.json'
import { sendGet } from '../utils/RestClient'
export function getHomeData() {
    return sendGet(Config["BASE_URL"] + "system/home").then(data => { return data; });
}