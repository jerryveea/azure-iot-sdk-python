# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FaultInjectionConnectionProperties(Model):
    """FaultInjectionConnectionProperties.

    :param action: Possible values include: 'None', 'CloseAll', 'Periodic'
    :type action: str or ~protocol.models.enum
    :param block_duration_in_minutes:
    :type block_duration_in_minutes: int
    """

    _attribute_map = {
        "action": {"key": "action", "type": "str"},
        "block_duration_in_minutes": {"key": "blockDurationInMinutes", "type": "int"},
    }

    def __init__(self, **kwargs):
        super(FaultInjectionConnectionProperties, self).__init__(**kwargs)
        self.action = kwargs.get("action", None)
        self.block_duration_in_minutes = kwargs.get("block_duration_in_minutes", None)
