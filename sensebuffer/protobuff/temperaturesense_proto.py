# This file adds code completion to the auto-generated wifisense_pb2 file.

from .temperaturesense_pb2 import TemperatureQuanta, TemperatureLog
from .common_proto import _TimeStamp

from typing import List, Callable, Union

class _TemperatureProfile( object ):
    c = 0

class _TemperatureQuanta( object ):
    profiles = _TemperatureProfile() # type: _TemperatureProfile
    time = _TimeStamp() # type: _TimeStamp

TemperatureQuanta = TemperatureQuanta # type: Callable[[],_TemperatureQuanta]

class _TemperatureLog( object ):
    class QuantasList(list):
        def add(self):  # type: (...)->_TemperatureQuanta
            return self[0]
    quantas = QuantasList() # type: Union[List[_TemperatureQuanta],QuantasList]

    def ParseFromString(self, string):
        return self

    def SerializeToString(self):
        return ""

TemperatureLog = TemperatureLog # type: Callable[[],_TemperatureLog]