
import DacTabs from './DacTabs';
import DspTabs from './DspTabs';
import SystemTabs from './SystemTabs';
import { IconPhoto, IconMessageCircle, IconSettings } from '@tabler/icons-react';
import {
    Tabs
} from '@chakra-ui/react';


export default function Tab() {
    return (
        <Tabs.Root lazyMount unmountOnExit defaultValue="DacSettings">
            <Tabs.List>
                <Tabs.Trigger value="DacSettings">Dac Settings</Tabs.Trigger>
                <Tabs.Trigger value="DspSettings">Dsp Settings</Tabs.Trigger>
                <Tabs.Trigger value="SystemSettings">System Settings</Tabs.Trigger>
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
    );
}
