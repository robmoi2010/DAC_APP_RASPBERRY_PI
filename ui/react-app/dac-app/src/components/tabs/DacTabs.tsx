
import VolumeSettings from '../dac/VolumeSettings';
import Filters from '../dac/Filters';
import DacModes from '../dac/DacModes';
import VolumeModes from '../dac/VolumeModes';
import { Fieldset, Heading, Tabs } from '@chakra-ui/react';
import DynamicSwitch from '../DynamicSwitch';
import { IconVolume, IconSettings, IconFilter, IconWaveSine, IconStairsUp } from '@tabler/icons-react';
import { getOversamplingStatus, getSecondOrderStatus, getThirdOrderStatus, updateOversamplingStatus, updateSecondOrderStatus, updateThirdOrderStatus } from '../../services/DacService';

const DacTabs = () => {
    return (
        <Tabs.Root lazyMount unmountOnExit defaultValue="VolumeSettings" orientation="vertical">
            <Tabs.List>
                <Tabs.Trigger value="VolumeSettings"><IconVolume />Volume Settings</Tabs.Trigger>
                <Tabs.Trigger value="Filters"><IconFilter />Filters</Tabs.Trigger>
                <Tabs.Trigger value="DacModes"><IconSettings />Dac Modes</Tabs.Trigger>
                <Tabs.Trigger value="VolumeModes"><IconVolume />Volume Modes</Tabs.Trigger>
                <Tabs.Trigger value="ThdCompensation"><IconWaveSine />Thd Compensation</Tabs.Trigger>
                <Tabs.Trigger value="Oversampling"><IconStairsUp />Oversampling</Tabs.Trigger>
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
                <Fieldset.Root>
                    <Fieldset.Legend>Second Order</Fieldset.Legend>
                    <Fieldset.Content>
                        <DynamicSwitch index={0} dataFunction={getSecondOrderStatus} updateFunction={updateSecondOrderStatus} tooltipText="2nd order on/off" />
                    </Fieldset.Content>
                </Fieldset.Root>
                <Fieldset.Root>
                    <Fieldset.Legend>Third Order</Fieldset.Legend>
                    <Fieldset.Content>
                        <DynamicSwitch index={1} dataFunction={getThirdOrderStatus} updateFunction={updateThirdOrderStatus} tooltipText="3rd order on/off" />
                    </Fieldset.Content>
                </Fieldset.Root>
            </Tabs.Content>
            <Tabs.Content value="Oversampling">
                <DynamicSwitch index={0} dataFunction={getOversamplingStatus} updateFunction={updateOversamplingStatus} tooltipText="Oversampling on/off" />
            </Tabs.Content>
        </Tabs.Root>
    );
}
export default DacTabs;