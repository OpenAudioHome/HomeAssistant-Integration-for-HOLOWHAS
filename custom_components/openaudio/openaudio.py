"""Module for working with OpenAudio device"""

import aiohttp
import base64
import json

from .exceptions import UnexpectedException
from typing import List

api_version = "v3"

import logging
logger = logging.getLogger(__name__)


class OpenAudioClient:
    """Class for working with OpenAudio device"""

    async def can_connect_to_openaudio(self, ip_address: str):
        """Verify connectivity to a compatible OpenAudio device"""
        logger.debug(f"Verifying connectivity to OpenAudio with ip_address={ip_address}")
        return True


    async def get_devices(self, ip_address: str) -> List[str]:
        """Get device list"""
        logger.debug(f"Invoking get_devices with ip_address={ip_address}")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://{ip_address}/api/{api_version}/devices/") as response:
                    if response.status != 200:
                        logger.error(f"Error getting devices: {response.status}")
                        raise UnexpectedException(response.status)
                    else:
                        text = await response.text()
                        contents = json.loads(text)
                        return contents["device_ids"]
        except aiohttp.ClientError as exc:
            raise UnexpectedException from exc
        
    async def get_devices_info(self, ip_address: str):
        """Get info for all devices"""
        logger.debug(f"Invoking get_devices_info with ip_address={ip_address}")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://{ip_address}/api/{api_version}/devices/info") as response:
                    if response.status != 200:
                        logger.error(f"Error getting devices info: {response.status}")
                        raise UnexpectedException(response.status)
                    else:
                        text = await response.text()
                        contents = json.loads(text)
                        return contents
        except aiohttp.ClientError as exc:
            raise UnexpectedException from exc
        
    async def get_server_device_id(self, ip_address: str):
        """Get server device ID"""
        logger.debug(f"Invoking get_server_device_id with ip_address={ip_address}")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://{ip_address}/api/{api_version}/devices/server") as response:
                    if response.status != 200:
                        logger.error(f"Error getting server device ID: {response.status}")
                        raise UnexpectedException(response.status)
                    else:
                        text = await response.text()
                        contents = json.loads(text)
                        return contents["device_ids"][0] if "device_ids" in contents and len(contents["device_ids"]) > 0 else None
        except aiohttp.ClientError as exc:
            raise UnexpectedException from exc

    async def get_device_connection_info(self, ip_address: str, device_id: str):
        """Get connection information"""
        logger.debug(f"Invoking get_device_connection_info with ip_address={ip_address}, device_id={device_id}")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://{ip_address}/api/{api_version}/devices/{device_id}/connection") as response:
                    if response.status != 200:
                        logger.error(f"Error getting device connection info: {response.status}")
                        raise UnexpectedException(response.status)
                    else:
                        text = await response.text()
                        contents = json.loads(text)
                        return contents
        except aiohttp.ClientError as exc:
            raise UnexpectedException from exc

    async def get_device_attributes(self, ip_address: str, device_id: str):
        """Get device attributes"""
        logger.debug(f"Invoking get_device_attributes with ip_address={ip_address}, device_id={device_id}")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://{ip_address}/api/{api_version}/devices/{device_id}/attributes") as response:
                    if response.status != 200:
                        logger.error(f"Error getting device attributes: {response.status}")
                        raise UnexpectedException(response.status)
                    else:
                        text = await response.text()
                        contents = json.loads(text)
                        return contents
        except aiohttp.ClientError as exc:
            raise UnexpectedException from exc

    async def get_device_config(self, ip_address: str, device_id: str):
        """Get device config"""
        logger.debug(f"Invoking get_device_config with ip_address={ip_address}, device_id={device_id}")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://{ip_address}/api/{api_version}/devices/{device_id}/config") as response:
                    if response.status != 200:
                        logger.error(f"Error getting device config: {response.status}")
                        raise UnexpectedException(response.status)
                    else:
                        text = await response.text()
                        contents = json.loads(text)
                        return contents
        except aiohttp.ClientError as exc:
            raise UnexpectedException from exc

    async def get_device_metrics(self, ip_address: str, device_id: str):
        """Get device metrics"""
        logger.debug(f"Invoking get_device_metrics with ip_address={ip_address}, device_id={device_id}")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://{ip_address}/api/{api_version}/devices/{device_id}/metrics") as response:
                    if response.status != 200:
                        logger.error(f"Error getting device metrics: {response.status}")
                        raise UnexpectedException(response.status)
                    else:
                        text = await response.text()
                        contents = json.loads(text)
                        return contents
        except aiohttp.ClientError as exc:
            raise UnexpectedException from exc

    async def get_zones(self, ip_address: str):
        """Get zone ids"""
        logger.debug(f"Invoking get_zones with ip_address={ip_address}")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://{ip_address}/api/{api_version}/zones") as response:
                    if response.status != 200:
                        logger.error(f"Error getting zones: {response.status}")
                        raise UnexpectedException(response.status)
                    else:
                        text = await response.text()
                        contents = json.loads(text)
                        return contents
        except aiohttp.ClientError as exc:
            raise UnexpectedException from exc
        
    async def get_zones_info(self, ip_address: str):
        """Get zone ids"""
        logger.debug(f"Invoking get_zones with ip_address={ip_address}")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://{ip_address}/api/{api_version}/zones/info") as response:
                    if response.status != 200:
                        logger.error(f"Error getting zones: {response.status}")
                        raise UnexpectedException(response.status)
                    else:
                        text = await response.text()
                        contents = json.loads(text)
                        return contents
        except aiohttp.ClientError as exc:
            raise UnexpectedException from exc

    async def get_zone_config(self, ip_address: str, zone_id: str):
        """Get zone config"""
        logger.debug(f"Invoking get_zone_config with ip_address={ip_address}, zone_id={zone_id}")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://{ip_address}/api/{api_version}/zones/{zone_id}") as response:
                    if response.status != 200:
                        logger.error(f"Error getting zone config: {response.status}")
                        raise UnexpectedException(response.status)
                    else:
                        text = await response.text()
                        contents = json.loads(text)
                        return contents
        except aiohttp.ClientError as exc:
            raise UnexpectedException from exc
        
    async def set_zone_volume(self, ip_address: str, zone_id: str, volume: int):
        """Set zone volume"""
        logger.debug(f"Invoking set_zone_volume with ip_address={ip_address}, zone_id={zone_id}, volume={volume}")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.put(f"http://{ip_address}/api/{api_version}/zones/{zone_id}/volume", json = { "volume": volume}) as response:
                    if response.status != 200:
                        logger.error(f"Error setting zone volume: {response.status}")
                        raise UnexpectedException(response.status)
                    else:
                        logger.debug("OpenAudio set_zone_volume get response 200")
                        return volume
        except aiohttp.ClientError as exc:
            raise UnexpectedException from exc

    async def set_zone_input(self, ip_address: str, zone_id: str, input: str):
        """Set zone input"""
        logger.debug(f"Invoking set_zone_input with ip_address={ip_address}, zone_id={zone_id}, input={input}")
        try:
            input_str = { "input_ids": []}
            if input is not None and len(input)>0:
                input_str = { "input_ids": [input]}
            #logger.debug("--------> input_str: %s", input_str)

            async with aiohttp.ClientSession() as session:
                async with session.put(f"http://{ip_address}/api/{api_version}/zones/{zone_id}/input", json = input_str) as response:
                    if response.status != 200:
                        logger.error(f"Error setting zone input: {response.status}")
                        raise UnexpectedException(response.status)
                    else:
                        logger.debug("OpenAudio set_zone_input get response 200")
                        return str
        except aiohttp.ClientError as exc:
            raise UnexpectedException from exc

    async def get_inputs(self, ip_address: str, class_filter: int = None):
        """Get input ids"""
        logger.debug(f"Invoking get_inputs with ip_address={ip_address}")
        try:
            query_params = ""

            if (class_filter is not None):
                query_params = f"?class_filter={class_filter}"

            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://{ip_address}/api/{api_version}/inputs/{query_params}") as response:
                    if response.status != 200:
                        logger.error(f"Error getting inputs: {response.status}")
                        raise UnexpectedException(response.status)
                    else:
                        text = await response.text()
                        contents = json.loads(text)
                        return contents
        except aiohttp.ClientError as exc:
            raise UnexpectedException from exc
        
    async def get_inputs_info(self, ip_address: str, class_filter: int = None):
        """Get input ids"""
        logger.debug(f"Invoking get_inputs with ip_address={ip_address}")
        try:
            query_params = ""

            if (class_filter is not None):
                query_params = f"?class_filter={class_filter}"

            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://{ip_address}/api/{api_version}/inputs/info{query_params}") as response:
                    if response.status != 200:
                        logger.error(f"Error getting inputs: {response.status}")
                        raise UnexpectedException(response.status)
                    else:
                        text = await response.text()
                        contents = json.loads(text)
                        return contents
        except aiohttp.ClientError as exc:
            raise UnexpectedException from exc
        
    async def get_input_config(self, ip_address: str, input_id: str):
        """Get input config"""
        logger.debug(f"Invoking get_input_config with ip_address={ip_address}, input_id={input_id}")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://{ip_address}/api/{api_version}/inputs/{input_id}") as response:
                    if response.status != 200:
                        logger.error(f"Error getting input config: {response.status}")
                        raise UnexpectedException(response.status)
                    else:
                        text = await response.text()
                        contents = json.loads(text)
                        return contents
        except aiohttp.ClientError as exc:
            raise UnexpectedException from exc
        
    async def get_available_inputs(self, ip_address: str, input_id: str):
        """Get available inputs"""
        logger.debug(f"Invoking get_available_inputs with ip_address={ip_address}, input_id={input_id}")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://{ip_address}/api/{api_version}/inputs/{input_id}/available-types") as response:
                    if response.status != 200:
                        logger.error(f"Error getting available inputs: {response.status}")
                        raise UnexpectedException(response.status)
                    else:
                        text = await response.text()
                        contents = json.loads(text)
                        return contents["available_types"]
        except aiohttp.ClientError as exc:
            raise UnexpectedException from exc

    async def get_input_types(self, ip_address: str, input_id: str):
        """Get input types"""
        logger.debug(f"Invoking get_input_types with ip_address={ip_address}, input_id={input_id}")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://{ip_address}/api/{api_version}/inputs/{input_id}/types") as response:
                    if response.status != 200:
                        logger.error(f"Error getting input types: {response.status}")
                        raise UnexpectedException(response.status)
                    else:
                        text = await response.text()
                        contents = json.loads(text)
                        return contents["available_types"]
        except aiohttp.ClientError as exc:
            raise UnexpectedException from exc

    async def set_input_type(self, ip_address: str, input_id: str, type: str):
        """Set input type"""
        logger.debug(f"Invoking set_input_type with ip_address={ip_address}, input_id={input_id}, type={type}")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.put(f"http://{ip_address}/api/{api_version}/inputs/{input_id}/type", json =  { "type": type }) as response:
                    if response.status != 200:
                        logger.error(f"Error setting input type: {response.status}")
                        raise UnexpectedException(response.status)
                    else:
                        logger.debug("OpenAudio set_input_type get response 200")
                        return str
        except aiohttp.ClientError as exc:
            raise UnexpectedException from exc

    async def set_input_volume(self, ip_address: str, input_id: str, volume: int):
        """Set input volume"""
        logger.debug(f"Invoking set_input_volume with ip_address={ip_address}, input_id={input_id}, volume={volume}")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.put(f"http://{ip_address}/api/{api_version}/inputs/{input_id}/volume", json = { "volume": volume}) as response:
                    if response.status != 200:
                        logger.error(f"Error setting zone volume: {response.status}")
                        raise UnexpectedException(response.status)
                    else:
                        text = await response.text()
                        contents = json.loads(text)
                        return contents
        except aiohttp.ClientError as exc:
            raise UnexpectedException from exc

    async def enable_input(self, ip_address: str, input_id: str, enable: bool):
        """Enable/disable an input"""
        logger.debug(f"Invoking enable_input with ip_address={ip_address}, input_id={input_id}, enable={enable}")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.put(f"http://{ip_address}/api/{api_version}/inputs/{input_id}/enable", json =  { "enable": enable }) as response:
                    if response.status != 200:
                        logger.error(f"Error enabling/disabling input: {response.status}")
                        raise UnexpectedException(response.status)
                    else:
                        text = await response.text()
                        contents = json.loads(text)
                        return contents
        except aiohttp.ClientError as exc:
            raise UnexpectedException from exc
