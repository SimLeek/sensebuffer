# This file adds code completion to the auto-generated rotationsense_pb2 file.

from .rotationsense_pb2 import RotationQuanta, RotationLog
from .common_proto import _TimeStamp

from typing import List, Callable, Union

class _RotationProfile( object ):
    rx = 0
    ry = 0
    rz = 0

class _RotationQuanta( object ):
    profiles = _RotationProfile() # type: _RotationProfile
    time = _TimeStamp() # type: _TimeStamp

RotationQuanta = RotationQuanta # type: Callable[[],_RotationQuanta]

class _RotationLog( object ):
    class QuantasList(list):
        def add(self):  # type: (...)->_RotationQuanta
            return self[0]
    quantas = QuantasList() # type: Union[List[_RotationQuanta],QuantasList]

    def ParseFromString(self, string):
        return self

    def SerializeToString(self):
        return ""

RotationLog = RotationLog # type: Callable[[],_RotationLog]