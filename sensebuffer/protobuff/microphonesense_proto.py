# This file adds code completion to the auto-generated microphonesense_pb2 file.

from .microphonesense_pb2 import MicrophoneQuanta, MicrophoneLog
from .common_proto import _TimeStamp

from typing import List, Callable, Union

class _MicrophoneProfile( object ):
    total_time = 0
    num_samples = 0
    bit_depth = 0
    mic_samples = bytearray()

class _MicrophoneQuanta( object ):
    profiles = _MicrophoneProfile() # type: _MicrophoneProfile
    time = _TimeStamp() # type: _TimeStamp

MicrophoneQuanta = MicrophoneQuanta # type: Callable[[],_MicrophoneQuanta]

class _MicrophoneLog( object ):
    class QuantasList(list):
        def add(self):  # type: (...)->_MicrophoneQuanta
            return self[0]
    quantas = QuantasList() # type: Union[List[_MicrophoneQuanta],QuantasList]

    def ParseFromString(self, string):
        return self

    def SerializeToString(self):
        return ""

MicrophoneLog = MicrophoneLog # type: Callable[[],_MicrophoneLog]