"""Xiaomi aqara contact sensor device."""

from zigpy.profiles import zha
from zigpy.zcl.clusters.general import Groups, Identify, OnOff

from zhaquirks.const import (
    DEVICE_TYPE,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODELS_INFO,
    NODE_DESCRIPTOR,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
    SKIP_CONFIGURATION,
    BatterySize,
)
from zhaquirks.xiaomi import (
    LUMI,
    XIAOMI_NODE_DESC,
    BasicCluster,
    DeviceTemperatureCluster,
    XiaomiPowerConfiguration,
    XiaomiQuickInitDevice,
)

OPEN_CLOSE_DEVICE_TYPE = 0x5F01
XIAOMI_CLUSTER_ID = 0xFFFF


class MagnetAQ2(XiaomiQuickInitDevice):
    """Xiaomi contact sensor device."""

    def __init__(self, *args, **kwargs):
        """Init."""
        self.battery_size = BatterySize.CR1632
        super().__init__(*args, **kwargs)

    signature = {
        #  <SimpleDescriptor endpoint=1 profile=260 device_type=24321
        #  device_version=1
        #  input_clusters=[0, 3, 65535, 6]
        #  output_clusters=[0, 4, 65535]>
        MODELS_INFO: [(LUMI, "lumi.sensor_magnet.aq2")],
        NODE_DESCRIPTOR: XIAOMI_NODE_DESC,
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: OPEN_CLOSE_DEVICE_TYPE,
                INPUT_CLUSTERS: [
                    BasicCluster.cluster_id,
                    Identify.cluster_id,
                    XIAOMI_CLUSTER_ID,
                    OnOff.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    BasicCluster.cluster_id,
                    Groups.cluster_id,
                    XIAOMI_CLUSTER_ID,
                ],
            }
        },
    }
    replacement = {
        SKIP_CONFIGURATION: True,
        ENDPOINTS: {
            1: {
                INPUT_CLUSTERS: [
                    BasicCluster,
                    Identify.cluster_id,
                    XiaomiPowerConfiguration,
                    DeviceTemperatureCluster,
                    XIAOMI_CLUSTER_ID,
                ],
                OUTPUT_CLUSTERS: [
                    BasicCluster,
                    Groups.cluster_id,
                    OnOff.cluster_id,
                    XIAOMI_CLUSTER_ID,
                ],
            }
        },
    }
