# This file adds code completion to the auto-generated wifisense_pb2 file.

from .velocitysense_pb2 import VelocityQuanta, VelocityLog
from .common_proto import _TimeStamp

from typing import List, Callable, Union

class _VelocityProfile( object ):
    vx = 0
    vy = 0
    vz = 0

class _VelocityQuanta( object ):
    profiles = _VelocityProfile() # type: _VelocityProfile
    time = _TimeStamp() # type: _TimeStamp

VelocityQuanta = VelocityQuanta # type: Callable[[],_VelocityQuanta]

class _VelocityLog( object ):
    class QuantasList(list):
        def add(self):  # type: (...)->_VelocityQuanta
            return self[0]
    quantas = QuantasList() # type: Union[List[_VelocityQuanta],QuantasList]

    def ParseFromString(self, string):
        return self

    def SerializeToString(self):
        return ""

VelocityLog = VelocityLog # type: Callable[[],_VelocityLog]