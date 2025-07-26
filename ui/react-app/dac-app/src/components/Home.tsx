import { VolumeGauge } from './VolumeGauge';
import PaddingRow from './PaddingRow';
import { useDispatch, useSelector } from 'react-redux';
import { decreaseVolume, getHomeData, increaseVolume, updateVolume } from '../services/SystemService';
import { setVolume } from '../state-repo/slices/volumeSlice';
import { memo, useEffect } from 'react';
import { setHomeData } from '../state-repo/slices/homeDataSlice';
import useWebSocket from 'react-use-websocket';
import { addMessage } from '../state-repo/slices/webSocketSlice';
import Config from '../configs/Config.json';
import { useNavigate } from 'react-router-dom';
import { setIndexUrlMap } from '../state-repo/slices/indexUrlMap';
import { ClientType } from '../utils/types';
import { Box, Button, HStack, VStack } from '@chakra-ui/react';
import DynamicSlider from './DynamicSlider';
import { IconMinus, IconPlus } from '@tabler/icons-react';


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
            const newData = processWsHomeData(homeData, genDt);
            if (newData.trim() != homeData.trim()) {
               dispatch(setHomeData(newData));
            }
         }
      }

   }, [lastMessage]);

   const components = [
      <VStack>
         <div>{homeData}</div>
         <VolumeGaugeMemo volume={volume} />
         <HStack>
            <Button onClick={() => handleBtnVolume(0, volume, 1)} variant='outline'><IconMinus /></Button>
            <VolumeSlider volume={volume} />
            <Button onClick={() => handleBtnVolume(1, volume, 1)} variant='outline'><IconPlus /></Button>
         </HStack>
         <Button variant="outline" style={{ 'width': '600px' }} onClick={() => navigate(handleSettingsOnclick(clientType))}>Settings</Button>
      </VStack>
   ];
   return <Box>{components}</Box>;
}
const VolumeGaugeMemo = memo(({ volume }: { volume: number }) => {
   return <VolumeGauge volume={volume} />;
}, (prevProps, nextProps) => {
   return prevProps.volume === nextProps.volume;
});
const VolumeSlider = memo(({ volume }: { volume: number }) => {
   return <DynamicSlider id={Home.name + "0"} value={volume} color="green" width="500px" label="Volume" min={0} max={100} step={1} updateFunction={updateVolume} tooltipText="set volume" />
}, (prevProps, nextProps) => {
   return prevProps.volume === nextProps.volume;
});
const handleSettingsOnclick = (clientType: ClientType): string => {
   if (clientType == ClientType.DEVICE) {
      return "/Settings";
   }
   else {
      return "/Tabs";
   }
}
const handleBtnVolume = async (direction: number, volume: number, step: number) => {
   //direction: 0 decrease 1 increase
   if (direction == 0) {
      let ret: number;
      ret = await decreaseVolume().then(data => {
         return Number(data?.value);
      })
      if (ret <= 0) {
         return;
      }
      while (ret > volume - step) {
         ret = await decreaseVolume().then(data => {
            return Number(data?.value);
         })
      }
   }
   else {
      let ret: number;
      ret = await increaseVolume().then(data => {
         return Number(data?.value);
      })
      if (ret >= 100) {
         return;
      }
      while (ret < volume + step) {
         ret = await increaseVolume().then(data => {
            return Number(data?.value);
         })
      }
   }
}
const processWsHomeData = (homeData: string, wsData: string) => {
   if (wsData == null || wsData.length == 0) {
      return homeData;
   }
   let ret = "";
   homeData = homeData.trim()
   const data: string[] = wsData.split("\n");
   const hd: string[] = homeData.includes(" ") ? homeData.split(" ") : [homeData];
   hd.forEach((d: string) => {
      const key = d.split(":")[0];
      let i;
      let has = false;
      for (i = 0; i < data.length; i++) {
         if (data[i].includes(key)) {
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
export default Home;