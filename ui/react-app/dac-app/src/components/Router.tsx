import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './Home'
import Settings from './Settings';
import RemoteNavigation from './system/RemoteNavigation';
import DacSettings from './dac/DacSettings';
import SystemSettings from './system/SystemSettings';
import DspSettings from './dsp/DspSettings';
import Filters from './dac/Filters';
import VolumeSettings from './dac/VolumeSettings';
import DacModes from './dac/DacModes';
import VolumeModes from './dac/VolumeModes';
import ThdCompensation from './dac/ThdCompensation';
import SecondOrderCompensation from './dac/SecondOrderCompensation';
import ThirdOrderCompensation from './dac/ThirdOrderCompensation';
import Input from './dsp/Input';
import Output from './dsp/Output';
import MainsOutput from './dsp/MainsOutput';
import SubwooferOutput from './dsp/SubwooferOutput';
import VolumeDevice from './system/VolumeDevice';
import SoundModes from './system/SoundModes';
import VolumeAlgorithm from './system/VolumeAlgorithm';
import Oversampling from './dac/Oversampling';
function Router() {
    return <BrowserRouter>
        <RemoteNavigation />
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/Settings" element={<Settings />} />
            <Route path="/DacSettings" element={<DacSettings />} />
            <Route path="/DspSettings" element={<DspSettings />} />
            <Route path="/SystemSettings" element={<SystemSettings />} />
            <Route path="/Filters" element={<Filters />} />
            <Route path="/VolumeSettings" element={<VolumeSettings />} />
            <Route path="/DacModes" element={<DacModes />} />
            <Route path="/VolumeModes" element={<VolumeModes />} />
            <Route path="/ThdCompensation" element={<ThdCompensation />} />
            <Route path="/SecondOrderCompensation" element={<SecondOrderCompensation />} />
            <Route path="/ThirdOrderCompensation" element={<ThirdOrderCompensation />} />
            <Route path="/Input" element={<Input />} />
            <Route path="/Output" element={<Output />} />
            <Route path="/MainsOutput" element={<MainsOutput />} />
            <Route path="/SubwooferOutput" element={<SubwooferOutput />} />
            <Route path="/VolumeDevice" element={<VolumeDevice />} />
            <Route path="/SoundModes" element={<SoundModes />} />
            <Route path="/VolumeAlgorithm" element={<VolumeAlgorithm />} />
            <Route path="/Oversampling" element={<Oversampling />} />
            <Route path="*" element={<Home />} />
        </Routes>
    </BrowserRouter>;
}
export default Router; 