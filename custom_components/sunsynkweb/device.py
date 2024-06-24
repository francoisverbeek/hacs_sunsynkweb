from dataclasses import dataclass
from typing import Any

from homeassistant.helpers.device_registry import DeviceInfo

from .const import (
    ACCUMULATED_BATTERY_CHARGE,
    ACCUMULATED_BATTERY_DISCHARGE,
    ACCUMULATED_GRID_EXPORT,
    ACCUMULATED_GRID_IMPORT,
    ACCUMULATED_LOAD,
    ACCUMULATED_PV_ENERGY,
    BATTERY_POWER,
    DOMAIN,
    GRID_POWER,
    LOAD_POWER,
    PV_CURRENT,
    PV_POWER,
    PV_VOLTAGE,
    SENSORS_PER_KEY,
    STATE_OF_CHARGE,
)


@dataclass
class SunsynkDevice:
    """A device for a sunsynk entity."""

    id: int
    api_avatar: Any
    name = "undefined"
    sensor_types = (
        ACCUMULATED_PV_ENERGY,
        ACCUMULATED_LOAD,
        ACCUMULATED_GRID_IMPORT,
        ACCUMULATED_GRID_EXPORT,
        ACCUMULATED_BATTERY_CHARGE,
        ACCUMULATED_BATTERY_DISCHARGE,
    )

    @property
    def device_info(self):
        """Generate device info."""
        return DeviceInfo(
            identifiers={(DOMAIN, str(self.id))},
            name=f"{self.name}_{self.id}",
            manufacturer="Sunsynk",
        )

    def sensors(self, coordinator):
        """Generate sensors for this device."""
        from .sensor import SunSynkApiSensor

        for sensor_type in self.sensor_types:
            yield SunSynkApiSensor(
                description=SENSORS_PER_KEY[sensor_type],
                coordinator=coordinator,
                id=self.id,
                device_info=self.device_info,
                api_avatar=self.api_avatar,
            )


@dataclass
class InstallationDevice(SunsynkDevice):
    """A device for an installation."""

    name: str = "installation"
    sensor_types = (
        ACCUMULATED_PV_ENERGY,
        ACCUMULATED_LOAD,
        ACCUMULATED_GRID_IMPORT,
        ACCUMULATED_GRID_EXPORT,
        ACCUMULATED_BATTERY_CHARGE,
        ACCUMULATED_BATTERY_DISCHARGE,
        BATTERY_POWER,
        LOAD_POWER,
        GRID_POWER,
        PV_POWER,
        STATE_OF_CHARGE,
    )


@dataclass
class PlantDevice(SunsynkDevice):
    """A device for a plant."""

    name: str = "plant"
    sensor_types = (
        ACCUMULATED_PV_ENERGY,
        ACCUMULATED_LOAD,
        ACCUMULATED_GRID_IMPORT,
        ACCUMULATED_GRID_EXPORT,
        ACCUMULATED_BATTERY_CHARGE,
        ACCUMULATED_BATTERY_DISCHARGE,
        BATTERY_POWER,
        LOAD_POWER,
        GRID_POWER,
        PV_POWER,
        STATE_OF_CHARGE,
    )


@dataclass
class InverterDevice(SunsynkDevice):
    """A device for an inverter."""

    name = "inverter"


@dataclass
class PVString(SunsynkDevice):
    """A device for a pv string."""

    name = "pv_string"
    sensor_types = (PV_POWER, PV_VOLTAGE, PV_CURRENT)
