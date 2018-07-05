# This file adds code completion to the auto-generated compasssense_pb2 file.

from .compasssense_pb2 import CompassQuanta, CompassLog
from .common_proto import _TimeStamp

from typing import List, Callable, Union

class _CompassProfile( object ):
    mx = 0
    my = 0
    mz = 0

class _CompassQuanta( object ):
    profiles = _CompassProfile() # type: _CompassProfile
    time = _TimeStamp() # type: _TimeStamp

CompassQuanta = CompassQuanta # type: Callable[[],_CompassQuanta]

class _CompassLog( object ):
    class QuantasList(list):
        def add(self):  # type: (...)->_CompassQuanta
            return self[0]
    quantas = QuantasList() # type: Union[List[_CompassQuanta],QuantasList]

    def ParseFromString(self, string):
        return self

    def SerializeToString(self):
        return ""

CompassLog = CompassLog # type: Callable[[],_CompassLog]