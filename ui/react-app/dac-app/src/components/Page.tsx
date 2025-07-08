
import React from "react";
import { Button, Table } from "@radix-ui/themes";
import { useSelector } from "react-redux";
import { ClientType } from "../utils/types";
import { Box } from "@chakra-ui/react";
import { IconArrowLeft } from "@tabler/icons-react";
function Page({ items }: { items: React.ReactNode[] }) {
   const clientType = useSelector((state: { clientType: { value: ClientType } }) => state.clientType.value);

   if (clientType == ClientType.WEB) {
      const tr: React.ReactNode[] = []
      let key = 0;
      items.forEach(x => {
         tr.push(<Table.Row key={key}><Table.Cell>{x}</Table.Cell></Table.Row>);
         key++
      })
      return <Table.Root><Table.Body>{tr}</Table.Body></Table.Root>;
   }
   else {
      let btnOnClick;
      const td: React.ReactNode[] = []
      items.forEach(x => {
         td.push(<Table.Cell>{x}</Table.Cell>);
         if (x.props?.text == "Back") {
            btnOnClick = x.props?.onClick;
         }
      })
      const row = <Table.Row key={0}>{td}</Table.Row>;
      return (<div style={{ "place-items": "center", "display": "flex" }}>
         <Button onClick={btnOnClick} ><IconArrowLeft /></Button>
         <Box height="200px"
            overflowX="auto"
            overflowY="auto"
            width="500px"
            style={{ "place-items": "center", "display": "flex" }}>

            <Table.Root>
               <Table.Body>{row}</Table.Body>
            </Table.Root>
         </Box>
      </div>);
   }
}
export default Page