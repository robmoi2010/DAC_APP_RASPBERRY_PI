
import VolumeSettings from '../dac/VolumeSettings';
import Filters from '../dac/Filters';
import DacModes from '../dac/DacModes';
import VolumeModes from '../dac/VolumeModes';
import { Heading, Tabs } from '@chakra-ui/react';
import DynamicSwitch from '../DynamicSwitch';
import { getOversamplingStatus, getSecondOrderStatus, getThirdOrderStatus, updateOversamplingStatus, updateSecondOrderStatus, updateThirdOrderStatus } from '../../services/DacService';

const DacTabs = () => {
    return (
        <Tabs.Root lazyMount unmountOnExit defaultValue="VolumeSettings" orientation="vertical">
            <Tabs.List>
                <Tabs.Trigger value="VolumeSettings">Volume Settings</Tabs.Trigger>
                <Tabs.Trigger value="Filters">Filters</Tabs.Trigger>
                <Tabs.Trigger value="DacModes">Dac Modes</Tabs.Trigger>
                <Tabs.Trigger value="VolumeModes">Volume Modes</Tabs.Trigger>
                <Tabs.Trigger value="ThdCompensation">Thd Compensation</Tabs.Trigger>
                <Tabs.Trigger value="Oversampling">Oversampling</Tabs.Trigger>
            </Tabs.List>
            <Tabs.Content value="VolumeSettings">
                <VolumeSettings />
            </Tabs.Content>
            <Tabs.Content value="Filters">
                <Filters />
            </Tabs.Content>
            <Tabs.Content value="DacModes">
                <DacModes />
            </Tabs.Content>
            <Tabs.Content value="VolumeModes">
                <VolumeModes />
            </Tabs.Content>
            <Tabs.Content value="ThdCompensation">
                <Heading>Second Order</Heading>
                <DynamicSwitch index={0} dataFunction={getSecondOrderStatus} updateFunction={updateSecondOrderStatus} tooltipText="2nd order on/off" />
                <Heading>Third Order</Heading>
                <DynamicSwitch index={1} dataFunction={getThirdOrderStatus} updateFunction={updateThirdOrderStatus} tooltipText="3rd order on/off" />
            </Tabs.Content>
            <Tabs.Content value="Oversampling">
                <DynamicSwitch index={0} dataFunction={getOversamplingStatus} updateFunction={updateOversamplingStatus} tooltipText="Oversampling on/off" />
            </Tabs.Content>
        </Tabs.Root>
    );
}
export default DacTabs;