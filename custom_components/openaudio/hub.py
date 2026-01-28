"""Hub for OpenAudio"""
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo

from .openaudio import OpenAudioClient

from .const import DOMAIN, LOGGER


class OpenAudioHub:
    """Hub class for OpenAudio"""

    def __init__(
        self,
        hass: HomeAssistant,
        ip_address: str,
    ) -> None:
        self._hass = hass
        self._ip_address = ip_address
        self.openaudios = {}
        self.group_inputs = {}
        self.client = None
        self._server_device_id = None

    async def verify_connection(self) -> bool:
        """Test if we can connect to the host."""
        client = OpenAudioClient()
        if await client.can_connect_to_openaudio(self._ip_address):
            self.client = client
            return True
        else:
            return False

    async def get_devices(self):
        """Test if we can authenticate to the host."""
        return await self.client.get_devices(self._ip_address)

    async def initialize(self):
        """Initialize hub"""
        self._server_device_id = await self.client.get_server_device_id(
            self._ip_address)

    async def get_connection_info(self):
        """Get connection info"""
        return await self.client.get_device_connection_info(
            self._ip_address, self._server_device_id
        )

    async def _get_devices_info(self):
        """Get devices info"""
        return await self.client.get_devices_info(
            self._ip_address
        )

    async def _get_zones_ids(self):
        """Get zones"""
        zones = await self.client.get_zones(self._ip_address)
        return zones["zone_ids"]
    
    async def _get_zones_info(self):
        """Get zones"""
        zones = await self.client.get_zones_info(self._ip_address)
        return zones

    async def _get_zone_config(self, zone_id: str):
        """Get zone config"""
        return await self.client.get_zone_config(
            self._ip_address, zone_id
        )

    async def set_zone_input(self, zone_id: str, input):
        """Set zone inputs"""
        return await self.client.set_zone_input(
            self._ip_address, zone_id, input
        )
    
    async def set_zone_volume(self,zone_id: str, volume: int):
        """Set zone volume"""
        return await self.client.set_zone_volume(
            self._ip_address, zone_id, volume
        )

    async def _get_input_ids(self):
        """Get inputs"""
        inputs = await self.client.get_inputs(self._ip_address)
        return inputs["input_ids"]
    
    async def _get_input_info(self):
        """Get inputs"""
        inputs = await self.client.get_inputs_info(self._ip_address)
        return inputs

    async def _get_input_config(self, input_id: str):
        """Get input config"""
        return await self.client.get_input_config(
            self._ip_address, input_id
        )

    async def _get_available_inputs(self, input_id: str):
        """Get available inputs"""
        return await self.client.get_available_inputs(
            self._ip_address, input_id
        )
    
    async def set_input_type(self, input_id: str, type: str):
        """Set input type"""
        return await self.client.set_input_type(
            self._ip_address, input_id, type
        )

    async def set_input_volume(self, input_id: str, volume: int):
        """Set the volume for a specific input (0-100)."""
        return await self.client.set_input_volume(
            self._ip_address, input_id, volume
        )

    async def set_input_enabled(self, input_id: str, enabled: bool):
        """Enable or disable a specific input."""
        return await self.client.enable_input(
            self._ip_address, input_id, enabled
        )   

    async def fetch_data(self):
        if self.client is None:
            can_connect = await self.verify_connection()
            if not can_connect:
                LOGGER.error("Could not connect to OpenAudio")
                return

        return await self._fetch_data_v3()

    async def _fetch_data_v3(self):
        """Get the data from OpenAudio"""
        devices = await self._get_devices_info()
        #LOGGER.debug("OpenAudio devices info: %s", devices)

        for device in devices:
            if self.openaudios.get(device["device_id"]) is None:
                self.openaudios[device["device_id"]] = OpenAudioDevice(self)
                LOGGER.debug("Initialized OpenAudioDevice for %s", device["device_id"])
            
            self.openaudios[device["device_id"]].update(device)

        zones = await self._get_zones_info()
        #LOGGER.debug("OpenAudio zone info: %s", zones)

        input_device_id = ""

        for z in zones:
            zone_id_parts = z["zone_id"].split("-")
            parts_size = len(zone_id_parts)
            zone_device_id = ""
            for i in range(parts_size - 1):
                if i == 0:
                    zone_device_id = zone_id_parts[i]
                else:
                    zone_device_id += "-" + zone_id_parts[i]
            input_device_id = zone_device_id
            if self.openaudios.get(zone_device_id) is not None:
                openaudio = self.openaudios[zone_device_id]
                openaudio.zones[z["zone_id"]] = z


        inputs = await self._get_input_info()
        #LOGGER.debug("OpenAudio input info: %s", inputs)

        for input_id in inputs["input_ids"]:
            if self.openaudios.get(input_device_id) is not None:
                LOGGER.debug("OpenAudio set input: %s", input_id)
                amp = self.openaudios[input_device_id]

                input_config = await self._get_input_config(input_id)
                LOGGER.debug("OpenAudio input config: %s", input_config)
                amp.inputs[input_id] = input_config
                self.group_inputs[input_id] = f"Source {input_id}"
            else:
                LOGGER.debug("OpenAudio get input_id is NONE")
        #LOGGER.debug("----> group input %s", self.group_inputs)

class OpenAudioDevice:
    """HA device for OpenAudio"""

    def update(self, device_info) -> None:
        """Update device information"""
        self._device_id = device_info["device_id"]
        self.config = device_info["config"]
        self.connection_info = device_info["connection"]
        self.device_metrics = device_info["metrics"]
        self.device_attributes = device_info["attributes"]
        self.uid_base = self.device_attributes["serial_number"]
        self.zones = {}
        self.inputs = {}

    def __init__(self, hub: OpenAudioHub) -> None:
        self.hub = hub

    @property
    def device_info(self) -> DeviceInfo:
        """Return device info"""
        name = self.config["name"]
        if name is None or name == "":
            name = self._device_id

        return {
            "identifiers": {(DOMAIN, f"{self.device_attributes['serial_number']}")},
            "name": name,
            "manufacturer": "OpenAudio",
            "sw_version": self.device_attributes["firmware_version"],
        }