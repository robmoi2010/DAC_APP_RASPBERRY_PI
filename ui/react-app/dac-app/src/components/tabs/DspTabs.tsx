import { Tabs } from '@chakra-ui/react';
import Input from '../dsp/Input';
import MainsOutput from '../dsp/MainsOutput';
import SubwooferOutput from '../dsp/SubwooferOutput';
const DspTabs = () => {
    return (
        <Tabs.Root lazyMount unmountOnExit defaultValue="Input" orientation="vertical">
            <Tabs.List>
                <Tabs.Trigger value="Input">Input</Tabs.Trigger>
                <Tabs.Trigger value="MainOutput">Mains Output</Tabs.Trigger>
                <Tabs.Trigger value="SubwooferOutput">Subwoofer Output</Tabs.Trigger>
            </Tabs.List>
            <Tabs.Content value="Input">
                <Input />
            </Tabs.Content>
            <Tabs.Content value="MainOutput">
                <MainsOutput />
            </Tabs.Content>
            <Tabs.Content value="SubwooferOutput">
                <SubwooferOutput />
            </Tabs.Content>
        </Tabs.Root>
    );
}
export default DspTabs;