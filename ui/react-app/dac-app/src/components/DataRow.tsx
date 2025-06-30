import { ClientType } from "../utils/types";
import { useSelector } from "react-redux";
import { Button, Card, Heading } from "@chakra-ui/react"


function DataRow({ onClick, text, type, selected, active }) {
   const clientType = useSelector((state: { clientType: { value: ClientType } }) => state.clientType.value);
   if (clientType == ClientType.DEVICE) {
      let styles = { 'width': '500px', 'height': '50px' };
      if (active) {
         styles = { ...styles, 'border': '1px solid black' };
      }
      if (selected) {
         styles = { ...styles, 'color': 'red' };
      }
      if (type == 2)//Back button
      {
         styles = { ...styles, 'width': '100px', 'height': '50px' };
      }
      return <Button variant="outline" style={styles} onClick={onClick}>{text}</Button>
   }
   else {
      if (type != 2) { //any type apart from back button should be displayed
         return (
            <Card.Root size="md" minW="300px" variant="elevated" border={selected?"1px solid":"none"} borderColor={selected?"red":"gray"}>
               <Card.Header>
                  <Heading size="md">{text}</Heading>
               </Card.Header>
               <Card.Body color="fg.muted">
                  Description here
               </Card.Body>
               <Card.Footer justifyContent="flex-end">
                  <Button variant="outline" disabled={selected} onClick={onClick}>Select</Button>
               </Card.Footer>
            </Card.Root>
         );
      }
   }

}
export default DataRow