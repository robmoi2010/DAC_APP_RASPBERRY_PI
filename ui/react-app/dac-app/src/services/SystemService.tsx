import Config from '../configs/Config.json'
import { sendGet } from '../utils/RestClient'
export async function getHomeData() {
    return await sendGet(Config["BASE_URL"] + "system/home");
}