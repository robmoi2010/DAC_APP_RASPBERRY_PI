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