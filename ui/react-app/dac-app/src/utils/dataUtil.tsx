import type { Dispatch } from "redux";
import type { indexMapType, responseDataType } from "./types";
import { setIndexUrlMap } from "../state-repo/slices/indexUrlMap";
import { setComponentsData } from "../state-repo/slices/dynamicComponentsDataSlice";

export const loadDynamicData = (dataFunction: Promise<responseDataType[]>, dispatch: Dispatch, backUrl: string) => {
    dataFunction.then(data => {
        const indexMap: indexMapType[] = [];
        data.forEach(x => {
            const r: indexMapType = { index: Number(x?.key), url: "" };
            indexMap.push(r);
        });
        indexMap.push({ index: indexMap.length, url: backUrl });
        dispatch(setIndexUrlMap(indexMap));
        dispatch(setComponentsData(data));
    });
}
