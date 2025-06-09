import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './Home'
import Settings from './Settings';
import RemoteNavigation from './general/RemoteNavigation';
function Router() {
    return <BrowserRouter>
       <RemoteNavigation />
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/Settings" element={<Settings />} />
            <Route path="*" element={<Home />} />
        </Routes>
    </BrowserRouter>;
}
export default Router; 