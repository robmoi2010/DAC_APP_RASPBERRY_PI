import { ClientType } from "../utils/types";
import { useSelector } from "react-redux";
import { Button, CardRoot, CardBody, Heading, Text, Center, CardHeader, CardFooter } from "@chakra-ui/react"

type props = {
   onClick: (() => void) | undefined,
   text: string,
   type: number,
   selected: boolean,
   active: boolean,
   description: string

}
function DataRow({ onClick, text, type, selected, active, description }: props) {
   const clientType = useSelector((state: { clientType: { value: ClientType } }) => state.clientType.value);
   if (clientType == ClientType.DEVICE) {
      if (type != 2) {
         return (
            <CardRoot width="200px" height="200px" overflow="hidden" onClick={onClick} size="lg" variant="elevated"
               border={selected || active ? "1px solid" : "none"} borderColor={selected ? "red" : (active) ? "blue" : "gray"}
               boxShadow={active ? 'md' : 'sm'}
               _focus={{ outline: 'none', boxShadow: 'outline' }}
               cursor="pointer"
               _hover={{ borderColor: 'blue.300' }}
            >
               <CardBody color="fg.muted">
                  <Center w="100%" h="100%">
                     <Text
                        textAlign="center"
                        overflowWrap="break-word"
                        whiteSpace="normal"
                     >
                        {text}
                     </Text>
                  </Center>
               </CardBody>
            </CardRoot>
         );
      }
   }
   else {
      if (type != 2) { //any type apart from back button should be displayed
         return (
            <CardRoot size="md" minW="500px" variant="elevated" border={selected ? "1px solid" : "none"} borderColor={selected ? "red" : "gray"}>
               <CardHeader>
                  <Heading size="md">{text}</Heading>
               </CardHeader>
               <CardBody color="fg.muted">
                  {description}
               </CardBody>
               <CardFooter justifyContent="flex-end">
                  <Button variant="outline" disabled={selected} onClick={onClick}>Select</Button>
               </CardFooter>
            </CardRoot>
         );
      }
   }

}
export default DataRow