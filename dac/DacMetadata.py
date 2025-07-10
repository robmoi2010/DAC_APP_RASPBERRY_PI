import asyncio
import json
import time

from fastapi import WebSocket
from model.model import ResponseModel
from services.utils.ws_connection_manager import WS_TYPE, WSConnectionManager
from registry.register import register


@register
class DacMetadata:
    def __init__(self, ws_connection_manager: WSConnectionManager):
        self.ws_connection_manager = ws_connection_manager
        self.polling = False

    async def add_ws_connection(self, websocket: WebSocket):
        await self.ws_connection_manager.connect(WS_TYPE.HOME_DATA, websocket)

    def poll_audio_metadata(self):
        self.polling = True
        # future optimization, check pll lock status first before reading spdif data to ensure that data is read only when the dac locks on to the audio clock signal
        while True:
            metadata = self.get_audio_stream_metadata()
            list = []
            list.append(
                ResponseModel(
                    key="0", value=metadata.get("sample_rate"), display_name="SR"
                )
            )
            list.append(
                ResponseModel(
                    key="1", value=metadata.get("bit_depth"), display_name="bits"
                )
            )
            data = [r.model_dump() for r in list]
            asyncio.run(
                self.ws_connection_manager.send_data(
                    WS_TYPE.HOME_DATA, json.dumps(data)
                )
            )
            time.sleep(5)

    def get_audio_stream_metadata(self):
        metadata = {}
        sample_rate = None
        bit_depth = None
        # set reg 136 to byte 3(5d) for sample rate

        # read reg 251 for sample rate payload
        sample_rate = 0b00000000
        # set reg 136 to byte 4(5d) for bit depth

        # read reg 251 for bit depth
        bit_depth = 0b00001010

        metadata["sample_rate"] = self.decode_sample_rate(sample_rate)
        metadata["bit_depth"] = self.decode_bit_depth(bit_depth)
        return metadata

    def decode_sample_rate(self, rate_data):
        str_data = format(rate_data, "08b")
        val = str_data[4:]
        if val == "0000":
            return "44.1k"
        elif val == "0010":
            return "48k"
        elif val == "0011":
            return "32k"
        elif val == "0100":
            return "22.05k"
        elif val == "0110":
            return "24k"
        elif val == "1000":
            return "88.2k"
        elif val == "1010":
            return "96k"
        elif val == "1100":
            return "176.4k"
        elif val == "1110":
            return "192k"
        else:
            return ""

    def decode_bit_depth(self, depth_data):
        str_data = format(depth_data, "08b")
        word_field_size = str_data[7:]
        val = str_data[4:7]
        if word_field_size == "0":
            if val == "100":
                return "23-bits"
            elif val == "010":
                return "22-bits"
            elif val == "110":
                return "21-bits"
            elif val == "001":
                return "20-bits"
            elif val == "101":
                return "24-bits"
        if word_field_size == "1":
            if val == "100":
                return "19-bits"
            elif val == "010":
                return "18-bits"
            elif val == "110":
                return "17-bits"
            elif val == "001":
                return "16-bits"
            elif val == "101":
                return "20-bits"

        return ""

    def polling_started(self):
        return self.polling
