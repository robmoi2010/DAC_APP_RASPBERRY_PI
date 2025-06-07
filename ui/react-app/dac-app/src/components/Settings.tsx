import DataRow from "./DataRow";
import Header from "./header";
import PaddingRow from "./PaddingRow";
export const settingsComponents = (setActivePage) => {
    return [
        <Header text="Settings" />,
        <PaddingRow />,
        <DataRow onClick={() => setActivePage("DacSettings")} text="DacSettings" type={1} active={false} />,
        <DataRow onClick={() => setActivePage("DspSettings")} text="DspSettings" type={1} active={false} />,
        <DataRow onClick={() => setActivePage("GeneralSettings")} text="GeneralSettings" type={1} active={false} />,
        <DataRow onClick={() => setActivePage("Home")} text="Back" type={2} active={false} />,
    ];
}