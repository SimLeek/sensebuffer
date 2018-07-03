# This file adds code completion to the auto-generated wifisense_pb2 file.

from .wifisense_pb2 import WifiQuanta, WifiLog

from typing import List, Callable, Union

class _WifiProfile( object ):
    ssid = ""
    bssid = ""

class _TimeStamp( object ):
    seconds = 0
    nanos = 0

class _WifiQuanta( object ):
    class ProfilesList(list):
        def add(self):  # type: (...)->_WifiProfile
            return self[0]
    profiles = ProfilesList() # type: Union[List[_WifiProfile], ProfilesList]
    time = _TimeStamp() # type: _TimeStamp

WifiQuanta = WifiQuanta # type: Callable[[],_WifiQuanta]

class _WifiLog( object ):
    class QuantasList(list):
        def add(self):  # type: (...)->_WifiQuanta
            return self[0]
    quantas = QuantasList() # type: Union[List[_WifiQuanta],QuantasList]

    def ParseFromString(self, string):
        return self

    def SerializeToString(self):
        return ""

WifiLog = WifiLog # type: Callable[[],_WifiLog]