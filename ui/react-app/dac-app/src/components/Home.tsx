import Page from './Page';
import DataRow from './DataRow';
import Header from './header';
import { getHomeData } from '../services/SystemService';
import { useState, useEffect } from 'react';
import { VolumeGauge } from './VolumeGauge';
import Config from '../configs/Config.json';
import useWebSocket from 'react-use-websocket';
import PaddingRow from './PaddingRow';
import { settingsComponents } from './Settings';
function Home() {
   const [volumeData, setVolumeData] = useState("");      // Holds fetched data
   const [genData, setGenData] = useState("");
   const [activePage, setActivePage] = useState("Home");

   // initial data load to display
   useEffect(() => {
      const dt = getHomeData();
      dt.then(data => {
         let row = "";
         if (data != null) {
            data.forEach(d => {
               if (d.key == "CURRENT_VOLUME" || d.key == "CURRENT_MUSE_VOLUME") {
                  setVolumeData(d.value)
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
            setGenData(row);
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
      if (lastMessage != null && lastMessage.data != null) {
         const dat = lastMessage.data;
         const data = JSON.parse(dat);
         let genDt = "";
         data.forEach(d => {
            if (d.key == "CURRENT_VOLUME" || d.key == "CURRENT_MUSE_VOLUME") {
               setVolumeData(d.value);
            }
            else {
               genDt += d.display_name;
               genDt += ": ";
               genDt += d.value;
            }
         });
         if (genDt != "") {
            setGenData(genDt);
         }
      }

   }, [lastMessage]);
   let components = null;
   if (activePage == "Home") {
      components = homeComponents(genData, volumeData, setActivePage);
   }
   else if (activePage == "Settings") {
      components = settingsComponents(setActivePage);
   }
   else if (activePage == "DacSettings") {
      components =[];
   }
   return <Page items={components} />;
}
const homeComponents = (genData, volumeData, setActivePage) => {
   return [
      <Header text="Home" />,
      <PaddingRow />,
      <Header text={genData} />,
      <PaddingRow />,
      <VolumeGauge volume={volumeData} />,
      <PaddingRow />,
      <DataRow onClick={() => setActivePage("Settings")} text="Settings" type={1} active={false} />
   ];
}


export default Home