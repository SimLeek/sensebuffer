# This file adds code completion to the auto-generated camerasense_pb2 file.

from .camerasense_pb2 import CameraQuanta, CameraLog
from .common_proto import _TimeStamp

from typing import List, Callable, Union

class _CameraProfile( object ):
    width = 0
    height = 0
    camera_image = bytearray()

class _CameraQuanta( object ):
    profiles = _CameraProfile() # type: _CameraProfile
    time = _TimeStamp() # type: _TimeStamp

CameraQuanta = CameraQuanta # type: Callable[[],_CameraQuanta]

class _CameraLog( object ):
    class QuantasList(list):
        def add(self):  # type: (...)->_CameraQuanta
            return self[0]
    quantas = QuantasList() # type: Union[List[_CameraQuanta],QuantasList]

    def ParseFromString(self, string):
        return self

    def SerializeToString(self):
        return ""

CameraLog = CameraLog # type: Callable[[],_CameraLog]