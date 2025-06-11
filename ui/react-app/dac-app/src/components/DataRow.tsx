import { Button } from "@radix-ui/themes"

const variant = "ghost";
const color = "red";
const size = "2";
const radius = "none";

function DataRow({ onClick, text, type, selected, active }) {
   let styles = {};
   if (active) {
      styles = { ...styles, 'border': '1px solid black' };
   }
   if (selected) {
      styles = { ...styles, 'color': 'red' };
   }
   if (type == 2)//Back button
   {
      styles = { ...styles, '': '' };
   }
   return <Button style={styles} onClick={onClick} variant={variant} color={color} size={size} radius={radius}>{text}</Button>

}
export default DataRow