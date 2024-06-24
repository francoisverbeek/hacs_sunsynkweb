"""Sensors for the sunsynk web api."""

import decimal
import logging
from typing import Any

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import SunsynkConfigEntry
from .coordinator import SunsynkUpdateCoordinator
from .device import InstallationDevice, InverterDevice, PlantDevice, PVString

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: SunsynkConfigEntry,
    async_add_entities: AddEntitiesCallback,  # noqa: F821
) -> None:
    """Set up sensor devices."""
    coordinator: SunsynkUpdateCoordinator = entry.runtime_data
    entities = []
    installation_id = 1  # we only support one installation at this time
    installation = InstallationDevice(installation_id, api_avatar=coordinator.cache)

    entities.extend(installation.sensors(coordinator))
    for plant in coordinator.cache.plants:
        plantdev = PlantDevice(plant.id, api_avatar=plant)
        entities.extend(plantdev.sensors(coordinator))
        for inverter in plant.inverters:
            inverterdev = InverterDevice(int(inverter.sn), api_avatar=inverter)

            entities.extend(inverterdev.sensors(coordinator))
            for stringid, string in inverter.pv_strings.items():
                stringdevice = PVString(
                    int(inverter.sn) + int(stringid), api_avatar=string
                )

                entities.extend(stringdevice.sensors(coordinator=coordinator))
    async_add_entities(entities)


class SunSynkApiSensor(CoordinatorEntity[SunsynkUpdateCoordinator], SensorEntity):
    """Parent class for sunsynk api exposing sensors.

    The sensors expose the sum of the power across all inverters
    for plants that have more than one inverter.
    State of charge is normally shared between inverters, so this will take
    the maximum of the state of charge.
    """

    _attr_has_entity_name = True
    entity_description: SensorEntityDescription

    def __init__(
        self,
        coordinator,
        description: SensorEntityDescription,
        id: int,
        device_info: DeviceInfo,
        api_avatar: Any,
    ) -> None:
        """Initialise the common elements for sunsynk web api sensors."""
        CoordinatorEntity.__init__(self, coordinator, context=coordinator)
        self.coordinator = coordinator
        self._attr_unique_id = f"{description.key}_{id}"
        self.entity_description: SensorEntityDescription = description
        self._attr_device_info = device_info
        self.api_avatar = api_avatar

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self.native_value = decimal.Decimal(
            getattr(self.api_avatar, self.entity_description.key)
        )
        self.async_write_ha_state()
