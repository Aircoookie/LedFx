import logging
from ledfxcontroller.devices import Device
import voluptuous as vol
import numpy as np
import time
import os
import platform
 
_LOGGER = logging.getLogger(__name__)
 
 
class UdpRgbDevice(Device):
    """ESP8266 UDP device support"""
 
    CONFIG_SCHEMA = vol.Schema({
        vol.Required('host'): str,
        vol.Required('universe', default=1): int,
        vol.Required('universe_size', default=512): int,
        vol.Required('channel_offset', default=1): int,
        vol.Required(vol.Any('pixel_count', 'channel_count')): vol.Coerce(int)
    })
 
    def __init__(self, config):
        self._config = config
        import socket
	# we take these from the config.yaml
        self._ip = self._config['host']
        self._port = self._config['port']
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
    @property
    def pixel_count(self):
        return int(self._config['pixel_count'])
 
    def activate(self):
 
        super().activate()
 
    def deactivate(self):
        super().deactivate()
 
    def flush(self, data):

        p = np.copy(np.clip(data, 0, 255).astype(int))
 
        m = []
        for i in range(len(p)):
          m.append(p[i][0])  # Pixel red value
          m.append(p[i][1])  # Pixel green value
          m.append(p[i][2])  # Pixel blue value
        m = bytes(m)
        self._sock.sendto(m, (self._ip, self._port))
