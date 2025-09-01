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
