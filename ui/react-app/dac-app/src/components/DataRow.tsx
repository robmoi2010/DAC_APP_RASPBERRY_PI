import { Button} from "@radix-ui/themes"

const variant="ghost";
const color="red";
const size="2";
const radius="none";

function DataRow(props)
{
   return <Button variant={variant} color={color} size={size} radius={radius}>{props.text}</Button>
}
export default DataRow