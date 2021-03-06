# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pressuresense.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pressuresense.proto',
  package='PressureSense',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13pressuresense.proto\x12\rPressureSense\x1a\x1fgoogle/protobuf/timestamp.proto\"\x9a\x01\n\x0ePressureQuanta\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12>\n\x07profile\x18\x02 \x01(\x0b\x32-.PressureSense.PressureQuanta.PressureProfile\x1a\x1e\n\x0fPressureProfile\x12\x0b\n\x03mpa\x18\x01 \x01(\x02\"=\n\x0bPressureLog\x12.\n\x07quantas\x18\x01 \x03(\x0b\x32\x1d.PressureSense.PressureQuantab\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_PRESSUREQUANTA_PRESSUREPROFILE = _descriptor.Descriptor(
  name='PressureProfile',
  full_name='PressureSense.PressureQuanta.PressureProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mpa', full_name='PressureSense.PressureQuanta.PressureProfile.mpa', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=196,
  serialized_end=226,
)

_PRESSUREQUANTA = _descriptor.Descriptor(
  name='PressureQuanta',
  full_name='PressureSense.PressureQuanta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='PressureSense.PressureQuanta.time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profile', full_name='PressureSense.PressureQuanta.profile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PRESSUREQUANTA_PRESSUREPROFILE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=226,
)


_PRESSURELOG = _descriptor.Descriptor(
  name='PressureLog',
  full_name='PressureSense.PressureLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quantas', full_name='PressureSense.PressureLog.quantas', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=228,
  serialized_end=289,
)

_PRESSUREQUANTA_PRESSUREPROFILE.containing_type = _PRESSUREQUANTA
_PRESSUREQUANTA.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PRESSUREQUANTA.fields_by_name['profile'].message_type = _PRESSUREQUANTA_PRESSUREPROFILE
_PRESSURELOG.fields_by_name['quantas'].message_type = _PRESSUREQUANTA
DESCRIPTOR.message_types_by_name['PressureQuanta'] = _PRESSUREQUANTA
DESCRIPTOR.message_types_by_name['PressureLog'] = _PRESSURELOG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PressureQuanta = _reflection.GeneratedProtocolMessageType('PressureQuanta', (_message.Message,), dict(

  PressureProfile = _reflection.GeneratedProtocolMessageType('PressureProfile', (_message.Message,), dict(
    DESCRIPTOR = _PRESSUREQUANTA_PRESSUREPROFILE,
    __module__ = 'pressuresense_pb2'
    # @@protoc_insertion_point(class_scope:PressureSense.PressureQuanta.PressureProfile)
    ))
  ,
  DESCRIPTOR = _PRESSUREQUANTA,
  __module__ = 'pressuresense_pb2'
  # @@protoc_insertion_point(class_scope:PressureSense.PressureQuanta)
  ))
_sym_db.RegisterMessage(PressureQuanta)
_sym_db.RegisterMessage(PressureQuanta.PressureProfile)

PressureLog = _reflection.GeneratedProtocolMessageType('PressureLog', (_message.Message,), dict(
  DESCRIPTOR = _PRESSURELOG,
  __module__ = 'pressuresense_pb2'
  # @@protoc_insertion_point(class_scope:PressureSense.PressureLog)
  ))
_sym_db.RegisterMessage(PressureLog)


# @@protoc_insertion_point(module_scope)
