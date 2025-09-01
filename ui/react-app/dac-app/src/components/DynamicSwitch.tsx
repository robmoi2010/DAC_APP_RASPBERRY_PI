import type { Dispatch } from "redux";
import type { responseDataType } from "../utils/types";
import { Switch } from "@chakra-ui/react/switch";
import { Tooltip } from "../components/ui/tooltip";
import { useDispatch, useSelector } from "react-redux";
import { updateSwitchChecked } from "../state-repo/slices/switchCheckedSlice";
import { useEffect } from "react";
import type { CheckedChangeDetails } from "@zag-js/switch";
type Props = {
    dataFunction: () => Promise<responseDataType>;
    updateFunction: (data: string) => Promise<responseDataType>;
    tooltipText: string;
    id: string; //unique for each component
};
const DynamicSwitch = ({ dataFunction, updateFunction, tooltipText, id }: Props) => {
    const switchChecked = useSelector((state: { switchChecked: { items: { [key: string]: boolean } } }) => state.switchChecked.items);
    const dispatch = useDispatch();
    useEffect(() => {
        dataFunction().then(data => {
            dispatch(updateSwitchChecked({ key: id, value: data.value == "1" }));
        });
    }, []);
    return (
        <Tooltip content={tooltipText}>
            <Switch.Root colorPalette="green" checked={switchChecked[id]} onCheckedChange={(e) => handleChange(dispatch, e, updateFunction, id)}>
                <Switch.HiddenInput />
                <Switch.Control />
                <Switch.Label>{switchChecked[id] ? "Deactivate" : "Activate"}</Switch.Label>
            </Switch.Root>
        </Tooltip>
    );
}
const handleChange = (dispatch: Dispatch, e: CheckedChangeDetails, updateFunction: (data: string) => Promise<responseDataType>, id: string) => {
    const selection = e.checked ? "1" : "0"
    const data = { key: "" + selection, value: "" + selection };
    updateFunction(JSON.stringify(data)).then(dt => {
        dispatch(updateSwitchChecked({ key: id, value: dt.value == "1" }));
    });
}
export default DynamicSwitch;