import { Tabs } from '@chakra-ui/react';
import VolumeDevice from '../system/VolumeDevice';
import VolumeAlgorithm from '../system/VolumeAlgorithm';
import SoundModes from '../system/SoundModes';
import { IconFunction, IconGauge, IconSettings } from '@tabler/icons-react';
const SystemTabs = () => {
    return (
        <Tabs.Root lazyMount unmountOnExit defaultValue="VolumeDevice" orientation="vertical">
            <Tabs.List>
                <Tabs.Trigger value="VolumeDevice"><IconGauge />Volume Device</Tabs.Trigger>
                <Tabs.Trigger value="VolumeAlgorithm"><IconFunction />Volume Algorithm</Tabs.Trigger>
                <Tabs.Trigger value="SoundModes"><IconSettings />Sound Modes</Tabs.Trigger>
            </Tabs.List>
            <Tabs.Content value="VolumeDevice">
                <VolumeDevice />
            </Tabs.Content>
            <Tabs.Content value="VolumeAlgorithm">
                <VolumeAlgorithm />
            </Tabs.Content>
            <Tabs.Content value="SoundModes">
                <SoundModes />
            </Tabs.Content>
        </Tabs.Root>);
}
export default SystemTabs;