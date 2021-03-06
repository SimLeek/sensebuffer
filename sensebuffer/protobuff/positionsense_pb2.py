# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: positionsense.proto

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
  name='positionsense.proto',
  package='PositiionSense',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13positionsense.proto\x12\x0ePositiionSense\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb1\x01\n\x0ePositionQuanta\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12@\n\x07profile\x18\x02 \x01(\x0b\x32/.PositiionSense.PositionQuanta.PositiionProfile\x1a\x33\n\x10PositiionProfile\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\">\n\x0bPositionLog\x12/\n\x07quantas\x18\x01 \x03(\x0b\x32\x1e.PositiionSense.PositionQuantab\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_POSITIONQUANTA_POSITIIONPROFILE = _descriptor.Descriptor(
  name='PositiionProfile',
  full_name='PositiionSense.PositionQuanta.PositiionProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='PositiionSense.PositionQuanta.PositiionProfile.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='PositiionSense.PositionQuanta.PositiionProfile.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='PositiionSense.PositionQuanta.PositiionProfile.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
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
  serialized_start=199,
  serialized_end=250,
)

_POSITIONQUANTA = _descriptor.Descriptor(
  name='PositionQuanta',
  full_name='PositiionSense.PositionQuanta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='PositiionSense.PositionQuanta.time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profile', full_name='PositiionSense.PositionQuanta.profile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_POSITIONQUANTA_POSITIIONPROFILE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=250,
)


_POSITIONLOG = _descriptor.Descriptor(
  name='PositionLog',
  full_name='PositiionSense.PositionLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quantas', full_name='PositiionSense.PositionLog.quantas', index=0,
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
  serialized_start=252,
  serialized_end=314,
)

_POSITIONQUANTA_POSITIIONPROFILE.containing_type = _POSITIONQUANTA
_POSITIONQUANTA.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_POSITIONQUANTA.fields_by_name['profile'].message_type = _POSITIONQUANTA_POSITIIONPROFILE
_POSITIONLOG.fields_by_name['quantas'].message_type = _POSITIONQUANTA
DESCRIPTOR.message_types_by_name['PositionQuanta'] = _POSITIONQUANTA
DESCRIPTOR.message_types_by_name['PositionLog'] = _POSITIONLOG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PositionQuanta = _reflection.GeneratedProtocolMessageType('PositionQuanta', (_message.Message,), dict(

  PositiionProfile = _reflection.GeneratedProtocolMessageType('PositiionProfile', (_message.Message,), dict(
    DESCRIPTOR = _POSITIONQUANTA_POSITIIONPROFILE,
    __module__ = 'positionsense_pb2'
    # @@protoc_insertion_point(class_scope:PositiionSense.PositionQuanta.PositiionProfile)
    ))
  ,
  DESCRIPTOR = _POSITIONQUANTA,
  __module__ = 'positionsense_pb2'
  # @@protoc_insertion_point(class_scope:PositiionSense.PositionQuanta)
  ))
_sym_db.RegisterMessage(PositionQuanta)
_sym_db.RegisterMessage(PositionQuanta.PositiionProfile)

PositionLog = _reflection.GeneratedProtocolMessageType('PositionLog', (_message.Message,), dict(
  DESCRIPTOR = _POSITIONLOG,
  __module__ = 'positionsense_pb2'
  # @@protoc_insertion_point(class_scope:PositiionSense.PositionLog)
  ))
_sym_db.RegisterMessage(PositionLog)


# @@protoc_insertion_point(module_scope)
