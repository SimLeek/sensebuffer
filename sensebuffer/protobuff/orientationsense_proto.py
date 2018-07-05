# This file adds code completion to the auto-generated orientationsense_pb2 file.

from .orientationsense_pb2 import OrientationQuanta, OrientationLog
from .common_proto import _TimeStamp

from typing import List, Callable, Union

class _OrientationProfile( object ):
    ox = 0
    oy = 0
    oz = 0

class _OrientationQuanta( object ):
    profiles = _OrientationProfile() # type: _OrientationProfile
    time = _TimeStamp() # type: _TimeStamp

OrientationQuanta = OrientationQuanta # type: Callable[[],_OrientationQuanta]

class _OrientationLog( object ):
    class QuantasList(list):
        def add(self):  # type: (...)->_OrientationQuanta
            return self[0]
    quantas = QuantasList() # type: Union[List[_OrientationQuanta],QuantasList]

    def ParseFromString(self, string):
        return self

    def SerializeToString(self):
        return ""

OrientationLog = OrientationLog # type: Callable[[],_OrientationLog]