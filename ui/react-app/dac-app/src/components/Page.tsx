
import React from "react";
import { Table } from "@radix-ui/themes";
function Page(props)
{
   const tr:React.ReactNode[]=[]
   let key=0;
   props.items.forEach(x=>{
      tr.push(<Table.Row key={key}><Table.Cell>{x}</Table.Cell></Table.Row>);
      key++
   })
   return <Table.Root><Table.Body>{tr}</Table.Body></Table.Root>;
}
export default Page