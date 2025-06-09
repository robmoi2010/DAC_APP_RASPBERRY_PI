import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import useWebSocket from "react-use-websocket";
import { decrement, increment, setIndex } from "../../state-repo/slices/navigationIndex";
import Config from '../../configs/Config.json';
import { useNavigate } from "react-router-dom";
const RemoteNavigation = () => {
    const index = useSelector((state) => state.navigationIndex.value);
    const dispatch = useDispatch();
    const totalItems = useSelector((state) => state.totalItems.value);
    const navigate = useNavigate();
    const nextUrl = useSelector((state) => state.nextUrl.value);
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
                    dispatch(setIndex(totalItems));
                }
                else {
                    dispatch(decrement());
                }
            }
            if (code == "DOWN") {
                if (index >= totalItems - 1) {
                    dispatch(setIndex(0));
                }
                else {
                    dispatch(increment());
                }
            }
            if (code == "OK") {
                navigate(nextUrl);
            }

        }

    }, [lastMessage]);
    return null;
}
export default RemoteNavigation;