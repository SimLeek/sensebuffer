# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gyroscopesense.proto

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
  name='gyroscopesense.proto',
  package='GyroscopeSense',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14gyroscopesense.proto\x12\x0eGyroscopeSense\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb6\x01\n\x0fGyroscopeQuanta\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x41\n\x07profile\x18\x02 \x01(\x0b\x32\x30.GyroscopeSense.GyroscopeQuanta.GyroscopeProfile\x1a\x36\n\x10GyroscopeProfile\x12\n\n\x02gx\x18\x01 \x01(\x02\x12\n\n\x02gy\x18\x02 \x01(\x02\x12\n\n\x02gz\x18\x03 \x01(\x02\"@\n\x0cGyroscopeLog\x12\x30\n\x07quantas\x18\x01 \x03(\x0b\x32\x1f.GyroscopeSense.GyroscopeQuantab\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_GYROSCOPEQUANTA_GYROSCOPEPROFILE = _descriptor.Descriptor(
  name='GyroscopeProfile',
  full_name='GyroscopeSense.GyroscopeQuanta.GyroscopeProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gx', full_name='GyroscopeSense.GyroscopeQuanta.GyroscopeProfile.gx', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gy', full_name='GyroscopeSense.GyroscopeQuanta.GyroscopeProfile.gy', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gz', full_name='GyroscopeSense.GyroscopeQuanta.GyroscopeProfile.gz', index=2,
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
  serialized_start=202,
  serialized_end=256,
)

_GYROSCOPEQUANTA = _descriptor.Descriptor(
  name='GyroscopeQuanta',
  full_name='GyroscopeSense.GyroscopeQuanta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='GyroscopeSense.GyroscopeQuanta.time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profile', full_name='GyroscopeSense.GyroscopeQuanta.profile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GYROSCOPEQUANTA_GYROSCOPEPROFILE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=256,
)


_GYROSCOPELOG = _descriptor.Descriptor(
  name='GyroscopeLog',
  full_name='GyroscopeSense.GyroscopeLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quantas', full_name='GyroscopeSense.GyroscopeLog.quantas', index=0,
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
  serialized_start=258,
  serialized_end=322,
)

_GYROSCOPEQUANTA_GYROSCOPEPROFILE.containing_type = _GYROSCOPEQUANTA
_GYROSCOPEQUANTA.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GYROSCOPEQUANTA.fields_by_name['profile'].message_type = _GYROSCOPEQUANTA_GYROSCOPEPROFILE
_GYROSCOPELOG.fields_by_name['quantas'].message_type = _GYROSCOPEQUANTA
DESCRIPTOR.message_types_by_name['GyroscopeQuanta'] = _GYROSCOPEQUANTA
DESCRIPTOR.message_types_by_name['GyroscopeLog'] = _GYROSCOPELOG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GyroscopeQuanta = _reflection.GeneratedProtocolMessageType('GyroscopeQuanta', (_message.Message,), dict(

  GyroscopeProfile = _reflection.GeneratedProtocolMessageType('GyroscopeProfile', (_message.Message,), dict(
    DESCRIPTOR = _GYROSCOPEQUANTA_GYROSCOPEPROFILE,
    __module__ = 'gyroscopesense_pb2'
    # @@protoc_insertion_point(class_scope:GyroscopeSense.GyroscopeQuanta.GyroscopeProfile)
    ))
  ,
  DESCRIPTOR = _GYROSCOPEQUANTA,
  __module__ = 'gyroscopesense_pb2'
  # @@protoc_insertion_point(class_scope:GyroscopeSense.GyroscopeQuanta)
  ))
_sym_db.RegisterMessage(GyroscopeQuanta)
_sym_db.RegisterMessage(GyroscopeQuanta.GyroscopeProfile)

GyroscopeLog = _reflection.GeneratedProtocolMessageType('GyroscopeLog', (_message.Message,), dict(
  DESCRIPTOR = _GYROSCOPELOG,
  __module__ = 'gyroscopesense_pb2'
  # @@protoc_insertion_point(class_scope:GyroscopeSense.GyroscopeLog)
  ))
_sym_db.RegisterMessage(GyroscopeLog)


# @@protoc_insertion_point(module_scope)