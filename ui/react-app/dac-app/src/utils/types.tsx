export type indexMapType = {
    index: number;
    url: string
}
export type responseDataType = {
    key: string;
    value: string;
    display_name: string
}
export const ClientType= {
    DEVICE: 0,
    WEB: 1
} as const
export type ClientType = typeof ClientType[keyof typeof ClientType];