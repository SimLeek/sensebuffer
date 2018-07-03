# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: velocitysense.proto

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
  name='velocitysense.proto',
  package='VelocitySense',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13velocitysense.proto\x12\rVelocitySense\x1a\x1fgoogle/protobuf/timestamp.proto\"\xae\x01\n\x0eVelocityQuanta\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12>\n\x07profile\x18\x02 \x01(\x0b\x32-.VelocitySense.VelocityQuanta.VelocityProfile\x1a\x32\n\x0fVelocityProfile\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"=\n\x0bVelocityLog\x12.\n\x07quantas\x18\x01 \x03(\x0b\x32\x1d.VelocitySense.VelocityQuantab\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_VELOCITYQUANTA_VELOCITYPROFILE = _descriptor.Descriptor(
  name='VelocityProfile',
  full_name='VelocitySense.VelocityQuanta.VelocityProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='VelocitySense.VelocityQuanta.VelocityProfile.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='VelocitySense.VelocityQuanta.VelocityProfile.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='VelocitySense.VelocityQuanta.VelocityProfile.z', index=2,
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
  serialized_start=196,
  serialized_end=246,
)

_VELOCITYQUANTA = _descriptor.Descriptor(
  name='VelocityQuanta',
  full_name='VelocitySense.VelocityQuanta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='VelocitySense.VelocityQuanta.time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profile', full_name='VelocitySense.VelocityQuanta.profile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_VELOCITYQUANTA_VELOCITYPROFILE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=246,
)


_VELOCITYLOG = _descriptor.Descriptor(
  name='VelocityLog',
  full_name='VelocitySense.VelocityLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quantas', full_name='VelocitySense.VelocityLog.quantas', index=0,
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
  serialized_start=248,
  serialized_end=309,
)

_VELOCITYQUANTA_VELOCITYPROFILE.containing_type = _VELOCITYQUANTA
_VELOCITYQUANTA.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_VELOCITYQUANTA.fields_by_name['profile'].message_type = _VELOCITYQUANTA_VELOCITYPROFILE
_VELOCITYLOG.fields_by_name['quantas'].message_type = _VELOCITYQUANTA
DESCRIPTOR.message_types_by_name['VelocityQuanta'] = _VELOCITYQUANTA
DESCRIPTOR.message_types_by_name['VelocityLog'] = _VELOCITYLOG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VelocityQuanta = _reflection.GeneratedProtocolMessageType('VelocityQuanta', (_message.Message,), dict(

  VelocityProfile = _reflection.GeneratedProtocolMessageType('VelocityProfile', (_message.Message,), dict(
    DESCRIPTOR = _VELOCITYQUANTA_VELOCITYPROFILE,
    __module__ = 'velocitysense_pb2'
    # @@protoc_insertion_point(class_scope:VelocitySense.VelocityQuanta.VelocityProfile)
    ))
  ,
  DESCRIPTOR = _VELOCITYQUANTA,
  __module__ = 'velocitysense_pb2'
  # @@protoc_insertion_point(class_scope:VelocitySense.VelocityQuanta)
  ))
_sym_db.RegisterMessage(VelocityQuanta)
_sym_db.RegisterMessage(VelocityQuanta.VelocityProfile)

VelocityLog = _reflection.GeneratedProtocolMessageType('VelocityLog', (_message.Message,), dict(
  DESCRIPTOR = _VELOCITYLOG,
  __module__ = 'velocitysense_pb2'
  # @@protoc_insertion_point(class_scope:VelocitySense.VelocityLog)
  ))
_sym_db.RegisterMessage(VelocityLog)


# @@protoc_insertion_point(module_scope)
