import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './Home'
import Settings from './Settings';
import RemoteNavigation from './general/RemoteNavigation';
import DacSettings from './dac/DacSettings';
import GeneralSettings from './general/GeneralSettings';
import DspSettings from './dsp/DspSettings';
import Filters from './dac/Filters';
import VolumeSettings from './dac/VolumeSettings';
import DacModes from './dac/DacModes';
function Router() {
    return <BrowserRouter>
        <RemoteNavigation />
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/Settings" element={<Settings />} />
            <Route path="/DacSettings" element={<DacSettings />} />
            <Route path="/DspSettings" element={<DspSettings />} />
            <Route path="/GeneralSettings" element={<GeneralSettings />} />
            <Route path="/Filters" element={<Filters />} />
            <Route path="/VolumeSettings" element={<VolumeSettings />} />
            <Route path="/DacModes" element={<DacModes />} />
            <Route path="*" element={<Home />} />
        </Routes>
    </BrowserRouter>;
}
export default Router; 