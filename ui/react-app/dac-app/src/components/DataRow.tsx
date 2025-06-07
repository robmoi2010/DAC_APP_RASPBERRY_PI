import { Button } from "@radix-ui/themes"

const variant = "ghost";
const color = "red";
const size = "2";
const radius = "none";

function DataRow({ onClick, text, type, active }) {
   return <Button onClick={onClick} variant={variant} color={color} size={size} radius={radius}>{text}</Button>
}
export default DataRow