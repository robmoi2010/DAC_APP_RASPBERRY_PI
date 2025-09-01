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
import { Box, Tabs } from '@chakra-ui/react';
import VolumeDevice from '../system/VolumeDevice';
import VolumeAlgorithm from '../system/VolumeAlgorithm';
import SoundModes from '../system/SoundModes';
import { IconFunction, IconGauge, IconSettings } from '@tabler/icons-react';
import { getVolumeRamp, updateVolumeRamp } from '../../services/SystemService';
import DynamicSwitch from '../DynamicSwitch';
const SystemTabs = () => {
    return (
        <Tabs.Root lazyMount unmountOnExit defaultValue="VolumeDevice" orientation="vertical">
            <Tabs.List>
                <Tabs.Trigger value="VolumeDevice"><IconGauge />Volume Device</Tabs.Trigger>
                <Tabs.Trigger value="VolumeAlgorithm"><IconFunction />Volume Algorithm</Tabs.Trigger>
                <Tabs.Trigger value="SoundModes"><IconSettings />Sound Modes</Tabs.Trigger>
                <Tabs.Trigger value="VolumeRamp"><IconSettings />Volume Ramp</Tabs.Trigger>
            </Tabs.List>
            <Tabs.Content value="VolumeDevice">
                <Box
                    height="500px"
                    width="800px"
                    overflowY="auto"
                    p={4}
                >
                    <VolumeDevice />
                </Box>
            </Tabs.Content>
            <Tabs.Content value="VolumeAlgorithm">
                <Box
                    height="500px"
                    overflowY="auto"
                    width="800px"
                    p={4}
                >
                    <VolumeAlgorithm />
                </Box>
            </Tabs.Content>
            <Tabs.Content value="SoundModes">
                <Box
                    height="500px"
                    overflowY="auto"
                    width="800px"
                    p={4}
                >
                    <SoundModes />
                </Box>
            </Tabs.Content>
            <Tabs.Content value="VolumeRamp">
                <Box
                    height="500px"
                    overflowY="auto"
                    width="800px"
                    p={4}
                >
                    <DynamicSwitch id={SystemTabs.name + "volumeramp"} dataFunction={getVolumeRamp} updateFunction={updateVolumeRamp} tooltipText="Volume ramp on/off" />
                </Box>
            </Tabs.Content>
        </Tabs.Root>);
}
export default SystemTabs;