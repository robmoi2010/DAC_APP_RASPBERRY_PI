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
