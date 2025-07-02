
import Filters from '../dac/Filters';
import DacModes from '../dac/DacModes';
import VolumeModes from '../dac/VolumeModes';
import { Box, Fieldset, Tabs } from '@chakra-ui/react';
import DynamicSwitch from '../DynamicSwitch';
import { IconVolume, IconSettings, IconFilter, IconWaveSine, IconStairsUp } from '@tabler/icons-react';
import { getOversamplingStatus, getSecondOrderStatus, getThirdOrderStatus, getVolumeDisableStatus, updateOversamplingStatus, updateSecondOrderStatus, updateThirdOrderStatus, updateVolumeStatus } from '../../services/DacService';

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
            <div>
                <Tabs.Content value="VolumeSettings">
                    <Box
                        height="500px"
                        overflowY="auto"
                        width="800px"
                        p={4}
                    >
                        <DynamicSwitch index={0} dataFunction={getVolumeDisableStatus} updateFunction={updateVolumeStatus} tooltipText="Dac volume on/off" />
                    </Box>
                </Tabs.Content>
                <Tabs.Content value="Filters">
                    <Box
                        height="500px"
                        overflowY="auto"
                        width="800px"
                        p={4}
                    >
                        <Filters />
                    </Box>
                </Tabs.Content>
                <Tabs.Content value="DacModes">
                    <Box
                        height="500px"
                        overflowY="auto"
                        width="800px"
                        p={4}
                    >
                        <DacModes />
                    </Box>
                </Tabs.Content>
                <Tabs.Content value="VolumeModes">
                    <Box
                        height="500px"
                        overflowY="auto"
                        width="800px"
                        p={4}
                    >
                        <VolumeModes />
                    </Box>
                </Tabs.Content>
                <Tabs.Content value="ThdCompensation">
                    <Box
                        height="500px"
                        overflowY="auto"
                        width="800px"
                        p={4}
                    >
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
                    </Box>
                </Tabs.Content>
                <Tabs.Content value="Oversampling">
                    <Box
                        height="500px"
                        overflowY="auto"
                        width="800px"
                        p={4}
                    >
                        <DynamicSwitch index={0} dataFunction={getOversamplingStatus} updateFunction={updateOversamplingStatus} tooltipText="Oversampling on/off" />
                    </Box>
                </Tabs.Content >
            </div>
        </Tabs.Root >
    );
}
export default DacTabs;