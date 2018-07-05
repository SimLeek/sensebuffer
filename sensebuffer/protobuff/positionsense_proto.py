# This file adds code completion to the auto-generated positionsense_pb2 file.

from .positionsense_pb2 import PositionQuanta, PositionLog
from .common_proto import _TimeStamp

from typing import List, Callable, Union

class _PositionProfile( object ):
    x = 0
    y = 0
    z = 0

class _PositionQuanta( object ):
    profiles = _PositionProfile() # type: _PositionProfile
    time = _TimeStamp() # type: _TimeStamp

PositionQuanta = PositionQuanta # type: Callable[[],_PositionQuanta]

class _PositionLog( object ):
    class QuantasList(list):
        def add(self):  # type: (...)->_PositionQuanta
            return self[0]
    quantas = QuantasList() # type: Union[List[_PositionQuanta],QuantasList]

    def ParseFromString(self, string):
        return self

    def SerializeToString(self):
        return ""

PositionLog = PositionLog # type: Callable[[],_PositionLog]