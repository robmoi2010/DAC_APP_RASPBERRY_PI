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
import React, { type ReactElement } from "react";
import { Button } from "@radix-ui/themes";
import { useSelector } from "react-redux";
import { ClientType } from "../utils/types";
import { Box, HStack, VStack, Center } from "@chakra-ui/react";
import { IconArrowLeft } from "@tabler/icons-react";
import DataRow from "./DataRow";
type propsType = {
   text: string;
   onClick: () => void;
}

function Page({ items }: { items: ReactElement<propsType>[] }) {

   const clientType = useSelector(
      (state: { clientType: { value: ClientType } }) => state.clientType.value
   );

   if (clientType === ClientType.WEB) {
      return <VStack>{items}</VStack>;
   }

   let btnOnClick;
   const processedItems: ReactElement[] = [];
   let id = 0;
   items.forEach(x => {
      if (React.isValidElement(x) && x.props?.text === "Back") {
         btnOnClick = x.props.onClick;
      }
      console.log(getElementName(x))
      if (getElementName(x) === DataRow.name) {
         processedItems.push(x);
         id++;
      }
   });

   return (
      <HStack overflowX="auto">
         <Button onClick={btnOnClick}>
            <IconArrowLeft />
         </Button>
         <Center height="500px" width="800px" overflowX="auto"
            overflowY="hidden"
         >
            <HStack>{processedItems}</HStack>
         </Center>
      </HStack>
   );
}
const getElementName = (node: React.ReactNode): string | undefined => {
   if (!React.isValidElement(node)) {
      return;
   }

   const type = node.type;

   // For native HTML elements like 'div', 'span'
   if (typeof type === "string") return type;

   // For functional or class components
   if (typeof type === "function") {
      return type.displayName || type.name || "Anonymous";
   }

   return "Unknown";
}


export default Page;
