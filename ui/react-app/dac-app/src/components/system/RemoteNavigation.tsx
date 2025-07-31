import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import useWebSocket from "react-use-websocket";
import { decrement, increment, setIndex } from "../../state-repo/slices/navigationIndex";
import Config from '../../configs/Config.json';
import { useNavigate } from "react-router-dom";
import { setSelectedIndex } from "../../state-repo/slices/selectedIndexSlice";
type indexMap = {
    index: number,
    url: string
}
const RemoteNavigation = () => {
    const index = useSelector((state: { navigationIndex: { value: number } }) => state.navigationIndex.value);
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const indexMap: indexMap[] = useSelector((state: { indexUrlMap: { value: { index: number, url: string }[] } }) => state.indexUrlMap.value);
    // setup websocket for ir remote commands
    const { lastMessage } = useWebSocket(
        Config["IR_REMOTE_WS_URL"],
        {
            share: false,
            shouldReconnect: () => true
        },
    );

    //process data received from websocket
    useEffect(() => {
        if (lastMessage !== null && lastMessage.data !== null) {
            const dat = lastMessage.data;
            const data = JSON.parse(dat);
            const code = data.value;
            console.log(code)
            if (code == "UP") {
                if (index <= 0) {
                    dispatch(setIndex(indexMap.length));
                }
                else {
                    dispatch(decrement());
                }
            }
            if (code == "DOWN") {
                if (index >= indexMap.length - 1) {
                    dispatch(setIndex(0));
                }
                else {
                    dispatch(increment());
                }
            }
            if (code == "OK") {
                const indexBuffer = index;
                // reset index to zero
                dispatch(setIndex(0));
                const value = indexMap.find(m => m.index == indexBuffer);
                if (value?.url != "") {
                    navigate("" + value?.url);
                }
                else {
                    dispatch(setSelectedIndex(indexBuffer))
                }
            }
            if (code == "BACK") {
                dispatch(setIndex(0));
                const value = indexMap[indexMap.length - 1].url;//last item is back url
                navigate("" + value);
            }

        }

    }, [lastMessage]);
    return null;
}
export default RemoteNavigation;