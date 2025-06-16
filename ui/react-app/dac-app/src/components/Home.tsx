import { VolumeGauge } from './VolumeGauge';
import DataRow from './DataRow';
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
import Header from './header';
import VolumeSlider from './VolumeSlider';

const Home = () => {
   const volume = useSelector((state) => state.volume.value);
   const homeData = useSelector((state) => state.homeData.value);
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
               if (d.key.trim() == "CURRENT_VOLUME" || d.key.trim() == "CURRENT_MUSES_VOLUME") {
                  dispatch(setVolume(d.value));
               }
               else {
                  row += d.display_name;
                  row += ":";
                  row += d.value;
                  row += "   ";
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
            if (d.key.trim() == "CURRENT_VOLUME" || d.key.trim() == "CURRENT_MUSES_VOLUME") {
               dispatch(setVolume(d.value));
            }
            else {
               genDt += d.display_name;
               genDt += ": ";
               genDt += d.value;
            }
         });
         if (genDt != "") {
            dispatch(setHomeData(genDt));
         }
      }

   }, [lastMessage, dispatch]);

   const components = [
      <PaddingRow />,
      <Header text={homeData} />,
      <PaddingRow />,
      <VolumeGauge volume={volume} />,
      <PaddingRow />,
      <VolumeSlider />,
      <PaddingRow />,
      <DataRow selected={false} onClick={() => navigate("/Settings")} text="Settings" type={1} active={false} />
   ];
   return <Page items={components} />;
}
export default Home;