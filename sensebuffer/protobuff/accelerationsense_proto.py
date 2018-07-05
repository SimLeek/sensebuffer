# This file adds code completion to the auto-generated accelerationsense_pb2 file.

from .accelerationsense_pb2 import AccelerationQuanta, AccelerationLog
from .common_proto import _TimeStamp

from typing import List, Callable, Union

class _AccelerationProfile( object ):
    ax = 0
    ay = 0
    az = 0

class _AccelerationQuanta( object ):
    profiles = _AccelerationProfile() # type: _AccelerationProfile
    time = _TimeStamp() # type: _TimeStamp

AccelerationQuanta = AccelerationQuanta # type: Callable[[],_AccelerationQuanta]

class _AccelerationLog( object ):
    class QuantasList(list):
        def add(self):  # type: (...)->_AccelerationQuanta
            return self[0]
    quantas = QuantasList() # type: Union[List[_AccelerationQuanta],QuantasList]

    def ParseFromString(self, string):
        return self

    def SerializeToString(self):
        return ""

AccelerationLog = AccelerationLog # type: Callable[[],_AccelerationLog]