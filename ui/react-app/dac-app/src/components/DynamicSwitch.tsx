import type { Dispatch } from "redux";
import type { responseDataType } from "../utils/types";
import { Switch } from "@chakra-ui/react/switch";
import { Tooltip } from "../components/ui/tooltip";
import { useDispatch, useSelector } from "react-redux";
import { addSwitchChecked, updateSwitchChecked } from "../state-repo/slices/switchCheckedSlice";
import { useEffect } from "react";
import type { CheckedChangeDetails } from "@zag-js/switch";
type Props = {
    dataFunction: () => Promise<responseDataType>;
    updateFunction: (data: string) => Promise<responseDataType>;
    tooltipText: string;
    index: number; //for multiple switches on same page, differentiates checked states
};
const DynamicSwitch = ({ dataFunction, updateFunction, tooltipText, index }: Props) => {
    const switchChecked = useSelector((state: { switchChecked: { items: boolean[] } }) => state.switchChecked.items);
    const dispatch = useDispatch();
    useEffect(() => {
        dataFunction().then(data => {
            if (switchChecked.length - 1 >= index) {
                dispatch(updateSwitchChecked({ index: index, value: data.value == "1" }));
            }
            else {
                dispatch(addSwitchChecked(data.value == "1"));
            }
        });
    }, []);
    return (
        <Tooltip content={tooltipText}>
            <Switch.Root colorPalette="green" checked={switchChecked[index]} onCheckedChange={(e) => handleChange(dispatch, e, updateFunction, index)}>
                <Switch.HiddenInput />
                <Switch.Control />
                <Switch.Label>{switchChecked[index] ? "Deactivate" : "Activate"}</Switch.Label>
            </Switch.Root>
        </Tooltip>
    );
}
const handleChange = (dispatch: Dispatch, e: CheckedChangeDetails, updateFunction: (data: string) => Promise<responseDataType>, index: number) => {
    const selection = e.checked ? "1" : "0"
    const data = { key: "" + selection, value: "" + selection };
    updateFunction(JSON.stringify(data)).then(dt => {
        dispatch(updateSwitchChecked({ index: index, value: dt.value == "1" }));
    });
}
export default DynamicSwitch;