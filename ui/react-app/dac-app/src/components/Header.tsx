import { Badge } from "@radix-ui/themes"
function Header({ text }: { text: string }) {
    return <Badge>{text}</Badge>
}
export default Header