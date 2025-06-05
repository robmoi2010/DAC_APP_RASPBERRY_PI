import Page from './Page';
import DataRow from './DataRow';
import Header from './header';
import { getHomeData } from '../services/SystemService';
import { useState, useEffect } from 'react';
import { VolumeGauge } from './VolumeGauge';
import Config from '../configs/Config.json';

function Home() {
   const [data, setData] = useState(null);      // Holds fetched data
   const [loading, setLoading] = useState(true); // Optional loading flag
   useEffect(() => {
      const fetchData = async () => {
         const dt = await getHomeData();
         setData(dt);        //  Causes re-render
         setLoading(false);
      };

      fetchData();
      const intervalId = setInterval(fetchData, Config["VOLUME_POLL_MILLIS"]); // fetch every 50ms

      return () => clearInterval(intervalId); // cleanup on unmount
   }, []);

   if (loading) return <p>Loading...</p>;
   let row = "";
   let volume;
   data.forEach(d => {
      if (d.key == "CURRENT_VOLUME") {
         volume = d.value;
      }
      else {
         row += d.display_name;
         row += ":";
         row += d.value;
         row += "   ";
      }
   });
   const components = [
      <Header text="Home" />,
      <DataRow text={row} />,
      <VolumeGauge volume={volume} />
   ];
   return <Page items={components} />;

}
export default Home