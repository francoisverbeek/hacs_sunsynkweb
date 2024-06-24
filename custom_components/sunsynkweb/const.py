"""Constants for the Sunsynk Inverter Web integration."""

from homeassistant.components.sensor import SensorEntityDescription
from homeassistant.components.sensor.const import SensorDeviceClass, SensorStateClass
from homeassistant.const import (
    PERCENTAGE,
    UnitOfElectricCurrent,
    UnitOfElectricPotential,
    UnitOfEnergy,
    UnitOfPower,
)

DOMAIN = "sunsynkweb"
BATTERY_POWER = "battery_power"
LOAD_POWER = "load_power"
GRID_POWER = "grid_power"
PV_POWER = "pv_power"
STATE_OF_CHARGE = "state_of_charge"
ACCUMULATED_PV_ENERGY = "acc_pv"
ACCUMULATED_LOAD = "acc_load"
ACCUMULATED_GRID_IMPORT = "acc_grid_import"
ACCUMULATED_GRID_EXPORT = "acc_grid_export"
ACCUMULATED_BATTERY_CHARGE = "acc_battery_charge"
ACCUMULATED_BATTERY_DISCHARGE = "acc_battery_discharge"
PV_VOLTAGE = "voltage"
PV_CURRENT = "amperage"


SENSORS = [
    SensorEntityDescription(  # ""A gauge for battery power."""
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        key=BATTERY_POWER,
        translation_key=BATTERY_POWER,
    ),
    SensorEntityDescription(  # A gauge for the load on all inverters."
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        key=LOAD_POWER,
        translation_key=LOAD_POWER,
    ),
    SensorEntityDescription(  # ""A gauge for the load to or from the grid."""
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        key=GRID_POWER,
        translation_key=GRID_POWER,
    ),
    SensorEntityDescription(  # ""A gauge for the power from generator (typically solar panels)."""
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        key=PV_POWER,
        translation_key=PV_POWER,
    ),
    SensorEntityDescription(  # ""A gauge to track batter charge."""
        device_class=SensorDeviceClass.BATTERY,
        native_unit_of_measurement=PERCENTAGE,
        key=STATE_OF_CHARGE,
        translation_key=STATE_OF_CHARGE,
    ),
    SensorEntityDescription(  # ""Accumulated energy generated (typically by solar panels)."""
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        key=ACCUMULATED_PV_ENERGY,
        translation_key=ACCUMULATED_PV_ENERGY,
        suggested_display_precision=2,
    ),
    SensorEntityDescription(  # ""Total energy consumed through the inverters."""
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        key=ACCUMULATED_LOAD,
        translation_key=ACCUMULATED_LOAD,
        suggested_display_precision=2,
    ),
    SensorEntityDescription(  # ""Total energy imported from the grid."""
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        key=ACCUMULATED_GRID_IMPORT,
        translation_key=ACCUMULATED_GRID_IMPORT,
        suggested_display_precision=2,
    ),
    SensorEntityDescription(  # ""Total energy exported to the grid."""
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        key=ACCUMULATED_GRID_EXPORT,
        translation_key=ACCUMULATED_GRID_EXPORT,
        suggested_display_precision=2,
    ),
    SensorEntityDescription(  # ""Total energy injected into the batteries."""
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        key=ACCUMULATED_BATTERY_CHARGE,
        translation_key=ACCUMULATED_BATTERY_CHARGE,
        suggested_display_precision=2,
    ),
    SensorEntityDescription(  # ""Total energy provided by the batteries."""
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        key=ACCUMULATED_BATTERY_DISCHARGE,
        translation_key=ACCUMULATED_BATTERY_DISCHARGE,
        suggested_display_precision=2,
    ),
    SensorEntityDescription(  # String voltage
        device_class=SensorDeviceClass.VOLTAGE,
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        key=PV_VOLTAGE,
        translation_key=PV_VOLTAGE,
        suggested_display_precision=2,
    ),
    SensorEntityDescription(  # String amperage
        device_class=SensorDeviceClass.CURRENT,
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        key=PV_CURRENT,
        translation_key=PV_CURRENT,
        suggested_display_precision=2,
    ),
]

SENSORS_PER_KEY = {s.key: s for s in SENSORS}
