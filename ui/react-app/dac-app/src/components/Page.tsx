
import React from "react";
import { Button } from "@radix-ui/themes";
import { useSelector } from "react-redux";
import { ClientType } from "../utils/types";
import { Box, HStack, VStack } from "@chakra-ui/react";
import { IconArrowLeft } from "@tabler/icons-react";
function Page({ items }: { items: React.ReactNode[] }) {
   const clientType = useSelector((state: { clientType: { value: ClientType } }) => state.clientType.value);

   if (clientType == ClientType.WEB) {
      return <VStack>
         {items}
      </VStack>;
   }
   else {
      let btnOnClick;
      items.forEach(x => {
         if (x.props?.text == "Back") {
            btnOnClick = x.props?.onClick;
         }
      });
      return (<div style={{ "place-items": "center", "display": "flex" }}>
         <Button onClick={btnOnClick} ><IconArrowLeft /></Button>
         <Box height="200px"
            overflowX="auto"
            overflowY="auto"
            width="500px"
            style={{ "place-items": "center", "display": "flex" }}>

            <HStack>
               {items}
            </HStack>
         </Box>
      </div>);
   }
}
export default Page