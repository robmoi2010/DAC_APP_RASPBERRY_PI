/*
 * Copyright (C) 2025 Robert Moi, Goglotek LTD
 *
 *  This file is part of the DAC_APPLICATION System.
 *
 *  The DAC_APPLICATION System is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  The DAC_APPLICATION is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with the DAC_APPLICATION. If not, see <https://www.gnu.org/licenses/>
 */
import Filters from '../dac/Filters';
import DacModes from '../dac/DacModes';
import VolumeModes from '../dac/VolumeModes';
import { Box, Fieldset, Tabs } from '@chakra-ui/react';
import DynamicSwitch from '../DynamicSwitch';
import { IconVolume, IconSettings, IconFilter, IconWaveSine, IconStairsUp, IconLock } from '@tabler/icons-react';
import { getDpllBandwidth, getOversamplingStatus, getSecondOrderStatus, getThirdOrderStatus, getVolumeDisableStatus, updateDpllBandwidth, updateOversamplingStatus, updateSecondOrderStatus, updateThirdOrderStatus, updateVolumeStatus } from '../../services/DacService';
import DynamicSlider from '../DynamicSlider';

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
                <Tabs.Trigger value="DpllBandwidth"><IconLock />Dpll Bandwidth</Tabs.Trigger>
            </Tabs.List>
            <div>
                <Tabs.Content value="VolumeSettings">
                    <Box
                        height="500px"
                        overflowY="auto"
                        width="800px"
                        p={4}
                    >
                        <DynamicSwitch id={DacTabs.name+"volumesettings"} dataFunction={getVolumeDisableStatus} updateFunction={updateVolumeStatus} tooltipText="Dac volume on/off" />
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
                                <DynamicSwitch id={DacTabs.name+"secondorder"} dataFunction={getSecondOrderStatus} updateFunction={updateSecondOrderStatus} tooltipText="2nd order on/off" />
                            </Fieldset.Content>
                        </Fieldset.Root>
                        <Fieldset.Root>
                            <Fieldset.Legend>Third Order</Fieldset.Legend>
                            <Fieldset.Content>
                                <DynamicSwitch id={DacTabs.name+"thirdorder"} dataFunction={getThirdOrderStatus} updateFunction={updateThirdOrderStatus} tooltipText="3rd order on/off" />
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
                        <DynamicSwitch id={DacTabs.name+"oversampling"} dataFunction={getOversamplingStatus} updateFunction={updateOversamplingStatus} tooltipText="Oversampling on/off" />
                    </Box>
                </Tabs.Content >
                <Tabs.Content value="DpllBandwidth">
                    <Box
                        height="500px"
                        overflowY="auto"
                        width="800px"
                        p={4}
                    >
                        <DynamicSlider id={DacTabs.name + "0"} color="green" width="500px" label="Dpll Bandwidth" min={1} max={15} step={1} dataFunction={getDpllBandwidth} updateFunction={updateDpllBandwidth} tooltipText="Dpll bandwidth (1-15)" />
                    </Box>
                </Tabs.Content >
            </div>
        </Tabs.Root >
    );
}
export default DacTabs;