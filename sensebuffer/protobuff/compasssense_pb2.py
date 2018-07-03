# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: compasssense.proto

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
  name='compasssense.proto',
  package='CompassSense',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12\x63ompasssense.proto\x12\x0c\x43ompassSense\x1a\x1fgoogle/protobuf/timestamp.proto\"\xac\x01\n\rCompassQuanta\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12;\n\x07profile\x18\x02 \x01(\x0b\x32*.CompassSense.CompassQuanta.CompassProfile\x1a\x34\n\x0e\x43ompassProfile\x12\n\n\x02mx\x18\x01 \x01(\x02\x12\n\n\x02my\x18\x02 \x01(\x02\x12\n\n\x02mz\x18\x03 \x01(\x02\":\n\nCompassLog\x12,\n\x07quantas\x18\x01 \x03(\x0b\x32\x1b.CompassSense.CompassQuantab\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_COMPASSQUANTA_COMPASSPROFILE = _descriptor.Descriptor(
  name='CompassProfile',
  full_name='CompassSense.CompassQuanta.CompassProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mx', full_name='CompassSense.CompassQuanta.CompassProfile.mx', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='my', full_name='CompassSense.CompassQuanta.CompassProfile.my', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mz', full_name='CompassSense.CompassQuanta.CompassProfile.mz', index=2,
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
  serialized_start=190,
  serialized_end=242,
)

_COMPASSQUANTA = _descriptor.Descriptor(
  name='CompassQuanta',
  full_name='CompassSense.CompassQuanta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='CompassSense.CompassQuanta.time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profile', full_name='CompassSense.CompassQuanta.profile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COMPASSQUANTA_COMPASSPROFILE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=242,
)


_COMPASSLOG = _descriptor.Descriptor(
  name='CompassLog',
  full_name='CompassSense.CompassLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quantas', full_name='CompassSense.CompassLog.quantas', index=0,
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
  serialized_start=244,
  serialized_end=302,
)

_COMPASSQUANTA_COMPASSPROFILE.containing_type = _COMPASSQUANTA
_COMPASSQUANTA.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_COMPASSQUANTA.fields_by_name['profile'].message_type = _COMPASSQUANTA_COMPASSPROFILE
_COMPASSLOG.fields_by_name['quantas'].message_type = _COMPASSQUANTA
DESCRIPTOR.message_types_by_name['CompassQuanta'] = _COMPASSQUANTA
DESCRIPTOR.message_types_by_name['CompassLog'] = _COMPASSLOG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CompassQuanta = _reflection.GeneratedProtocolMessageType('CompassQuanta', (_message.Message,), dict(

  CompassProfile = _reflection.GeneratedProtocolMessageType('CompassProfile', (_message.Message,), dict(
    DESCRIPTOR = _COMPASSQUANTA_COMPASSPROFILE,
    __module__ = 'compasssense_pb2'
    # @@protoc_insertion_point(class_scope:CompassSense.CompassQuanta.CompassProfile)
    ))
  ,
  DESCRIPTOR = _COMPASSQUANTA,
  __module__ = 'compasssense_pb2'
  # @@protoc_insertion_point(class_scope:CompassSense.CompassQuanta)
  ))
_sym_db.RegisterMessage(CompassQuanta)
_sym_db.RegisterMessage(CompassQuanta.CompassProfile)

CompassLog = _reflection.GeneratedProtocolMessageType('CompassLog', (_message.Message,), dict(
  DESCRIPTOR = _COMPASSLOG,
  __module__ = 'compasssense_pb2'
  # @@protoc_insertion_point(class_scope:CompassSense.CompassLog)
  ))
_sym_db.RegisterMessage(CompassLog)


# @@protoc_insertion_point(module_scope)
