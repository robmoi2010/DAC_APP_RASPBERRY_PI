
import DacTabs from './DacTabs';
import DspTabs from './DspTabs';
import SystemTabs from './SystemTabs';
import { IconCpu, IconAdjustments, IconSettings, IconArrowLeft } from '@tabler/icons-react';
import {
    Button,
    Tabs,
} from '@chakra-ui/react';
import { useNavigate } from 'react-router-dom';


export default function Tab() {
    const navigate = useNavigate();
    return (<div>
        <Button variant='outline' onClick={() => navigate("/Home")} ><IconArrowLeft /></Button>
            <Tabs.Root lazyMount unmountOnExit defaultValue="DacSettings" fitted={true}>
                <Tabs.List>
                    <Tabs.Trigger value="DacSettings"><IconCpu />Dac Settings</Tabs.Trigger>
                    <Tabs.Trigger value="DspSettings"><IconAdjustments />Dsp Settings</Tabs.Trigger>
                    <Tabs.Trigger value="SystemSettings"><IconSettings />System Settings</Tabs.Trigger>
                </Tabs.List>
                <Tabs.Content value="DacSettings">
                        <DacTabs />
                </Tabs.Content>
                <Tabs.Content value="DspSettings">
                        <DspTabs />
                </Tabs.Content>
                <Tabs.Content value="SystemSettings">
                        <SystemTabs /> 
                </Tabs.Content>
            </Tabs.Root>
    </div>
    );
}
