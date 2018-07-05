# This file adds code completion to the auto-generated pressuresense_pb2 file.

from .pressuresense_pb2 import PressureQuanta, PressureLog
from .common_proto import _TimeStamp

from typing import List, Callable, Union

class _PressureProfile( object ):
    mpa = 0

class _PressureQuanta( object ):
    profiles = _PressureProfile() # type: _PressureProfile
    time = _TimeStamp() # type: _TimeStamp

PressureQuanta = PressureQuanta # type: Callable[[],_PressureQuanta]

class _PressureLog( object ):
    class QuantasList(list):
        def add(self):  # type: (...)->_PressureQuanta
            return self[0]
    quantas = QuantasList() # type: Union[List[_PressureQuanta],QuantasList]

    def ParseFromString(self, string):
        return self

    def SerializeToString(self):
        return ""

PressureLog = PressureLog # type: Callable[[],_PressureLog]