# This file adds code completion to the auto-generated gyroscopesense_pb2 file.

from .gyroscopesense_pb2 import GyroscopeQuanta, GyroscopeLog
from .common_proto import _TimeStamp

from typing import List, Callable, Union

class _GyroscopeProfile( object ):
    gx = 0
    gy = 0
    gz = 0

class _GyroscopeQuanta( object ):
    profiles = _GyroscopeProfile() # type: _GyroscopeProfile
    time = _TimeStamp() # type: _TimeStamp

GyroscopeQuanta = GyroscopeQuanta # type: Callable[[],_GyroscopeQuanta]

class _GyroscopeLog( object ):
    class QuantasList(list):
        def add(self):  # type: (...)->_GyroscopeQuanta
            return self[0]
    quantas = QuantasList() # type: Union[List[_GyroscopeQuanta],QuantasList]

    def ParseFromString(self, string):
        return self

    def SerializeToString(self):
        return ""

GyroscopeLog = GyroscopeLog # type: Callable[[],_GyroscopeLog]