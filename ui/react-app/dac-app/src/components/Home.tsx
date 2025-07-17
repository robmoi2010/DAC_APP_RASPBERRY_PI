import { VolumeGauge } from './VolumeGauge';
import PaddingRow from './PaddingRow';
import { useDispatch, useSelector } from 'react-redux';
import Page from './Page';
import { getHomeData } from '../services/SystemService';
import { setVolume } from '../state-repo/slices/volumeSlice';
import { useEffect } from 'react';
import { setHomeData } from '../state-repo/slices/homeDataSlice';
import useWebSocket from 'react-use-websocket';
import { addMessage } from '../state-repo/slices/webSocketSlice';
import Config from '../configs/Config.json';
import { useNavigate } from 'react-router-dom';
import { setIndexUrlMap } from '../state-repo/slices/indexUrlMap';
import VolumeSlider from './VolumeSlider';
import { ClientType } from '../utils/types';
import { Box, Button } from '@chakra-ui/react';


const Home = () => {
   const volume = useSelector((state: { volume: { value: number } }) => state.volume.value);
   const homeData = useSelector((state: { homeData: { value: string } }) => state.homeData.value);
   const clientType = useSelector((state: { clientType: { value: ClientType } }) => state.clientType.value);
   const dispatch = useDispatch();
   const navigate = useNavigate();

   // initial data load to display
   useEffect(() => {
      const indexMap = [
         { index: 0, url: "/Settings" }];
      dispatch(setIndexUrlMap(indexMap));
      const dt = getHomeData();
      dt.then(data => {
         let row = "";
         if (data != null) {
            data.forEach(d => {
               if (d.key.trim() == "CURRENT_VOLUME") {
                  dispatch(setVolume(d.value));
               }
               else {
                  row += d.display_name;
                  row += ":";
                  row += d.value;
                  row += " ";
               }
            });
         }
         if (row != "") {
            dispatch(setHomeData(row));
         }
      });
   }, []);
   // setup websocket for asynchronous update of ui data
   const { lastMessage } = useWebSocket(
      Config["WS_URL"],
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
         dispatch(addMessage(data));
         let genDt = "";
         data.forEach(d => {
            if (d.key.trim() == "CURRENT_VOLUME") {
               dispatch(setVolume(d.value));
            }
            else {
               genDt += d.display_name;
               genDt += ":";
               genDt += d.value;
               genDt += "\n";
            }
         });
         if (genDt != "") {
            dispatch(setHomeData(processWsHomeData(homeData, genDt)));
         }
      }

   }, [lastMessage, dispatch]);

   const components = [
      <PaddingRow />,
      <div style={{ paddingLeft: "120px" }}>{homeData}</div>,
      <PaddingRow />,
      <div style={{ paddingLeft: '125px' }}>
         <VolumeGauge volume={volume} />
         <PaddingRow />
         <VolumeSlider volume={volume} />
      </div>,
      <PaddingRow />,
      <Button variant="outline" style={{ 'width': '500px' }} onClick={() => navigate(handleSettingsOnclick(clientType))}>Settings</Button>
   ];
   return <Box>{components}</Box>;
}
const handleSettingsOnclick = (clientType: ClientType): string => {
   if (clientType == ClientType.DEVICE) {
      return "/Settings";
   }
   else {
      return "/Tabs";
   }
}
const processWsHomeData = (homeData: string, wsData: string) => {
   if (wsData == null || wsData.length == 0) {
      return homeData;
   }
   let ret = "";
   homeData=homeData.trim()
   const data: string[] = wsData.split("\n");
   const hd: string[] = contains(" ", homeData) ? homeData.split(" ") : [homeData];
   hd.forEach((d: string) => {
      const key = d.split(":")[0];
      let i;
      let has = false;
      for (i = 0; i < data.length; i++) {
         if (contains(key.trim(), data[i].trim())) {
            has = true;
            ret += data[i] + " ";
            data[i] = "";
            break;
         }
      }
      if (!has) {
         ret += d + " "
      }
   });
   data.forEach(l => {
      if (l != "") {
         ret += l + " ";
      }
   });
   return ret.trim();
}
const contains = (key: string, data: string) => {//trim key and data at the calling function.
   let i = 0;
   let j = 0;
   let match = false
   while (i < key.length) {
      if (j >= data.length) {
         break;
      }
      if (key.charAt(i) == data.charAt(j)) {
         match = true;
         i++;
      }
      else {
         match = false;
         i = 0;
      }
      if (match && i >= key.length) {
         return true;
      }
      j++;
   }
   return false;

}
export default Home;