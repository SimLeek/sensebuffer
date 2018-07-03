# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orientationsense.proto

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
  name='orientationsense.proto',
  package='OrientationSense',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16orientationsense.proto\x12\x10OrientationSense\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc0\x01\n\x11OrientationQuanta\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12G\n\x07profile\x18\x02 \x01(\x0b\x32\x36.OrientationSense.OrientationQuanta.OrientationProfile\x1a\x38\n\x12OrientationProfile\x12\n\n\x02ox\x18\x01 \x01(\x02\x12\n\n\x02oy\x18\x02 \x01(\x02\x12\n\n\x02oz\x18\x03 \x01(\x02\"F\n\x0eOrientationLog\x12\x34\n\x07quantas\x18\x01 \x03(\x0b\x32#.OrientationSense.OrientationQuantab\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_ORIENTATIONQUANTA_ORIENTATIONPROFILE = _descriptor.Descriptor(
  name='OrientationProfile',
  full_name='OrientationSense.OrientationQuanta.OrientationProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ox', full_name='OrientationSense.OrientationQuanta.OrientationProfile.ox', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oy', full_name='OrientationSense.OrientationQuanta.OrientationProfile.oy', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oz', full_name='OrientationSense.OrientationQuanta.OrientationProfile.oz', index=2,
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
  serialized_start=214,
  serialized_end=270,
)

_ORIENTATIONQUANTA = _descriptor.Descriptor(
  name='OrientationQuanta',
  full_name='OrientationSense.OrientationQuanta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='OrientationSense.OrientationQuanta.time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profile', full_name='OrientationSense.OrientationQuanta.profile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ORIENTATIONQUANTA_ORIENTATIONPROFILE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=270,
)


_ORIENTATIONLOG = _descriptor.Descriptor(
  name='OrientationLog',
  full_name='OrientationSense.OrientationLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quantas', full_name='OrientationSense.OrientationLog.quantas', index=0,
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
  serialized_start=272,
  serialized_end=342,
)

_ORIENTATIONQUANTA_ORIENTATIONPROFILE.containing_type = _ORIENTATIONQUANTA
_ORIENTATIONQUANTA.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ORIENTATIONQUANTA.fields_by_name['profile'].message_type = _ORIENTATIONQUANTA_ORIENTATIONPROFILE
_ORIENTATIONLOG.fields_by_name['quantas'].message_type = _ORIENTATIONQUANTA
DESCRIPTOR.message_types_by_name['OrientationQuanta'] = _ORIENTATIONQUANTA
DESCRIPTOR.message_types_by_name['OrientationLog'] = _ORIENTATIONLOG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrientationQuanta = _reflection.GeneratedProtocolMessageType('OrientationQuanta', (_message.Message,), dict(

  OrientationProfile = _reflection.GeneratedProtocolMessageType('OrientationProfile', (_message.Message,), dict(
    DESCRIPTOR = _ORIENTATIONQUANTA_ORIENTATIONPROFILE,
    __module__ = 'orientationsense_pb2'
    # @@protoc_insertion_point(class_scope:OrientationSense.OrientationQuanta.OrientationProfile)
    ))
  ,
  DESCRIPTOR = _ORIENTATIONQUANTA,
  __module__ = 'orientationsense_pb2'
  # @@protoc_insertion_point(class_scope:OrientationSense.OrientationQuanta)
  ))
_sym_db.RegisterMessage(OrientationQuanta)
_sym_db.RegisterMessage(OrientationQuanta.OrientationProfile)

OrientationLog = _reflection.GeneratedProtocolMessageType('OrientationLog', (_message.Message,), dict(
  DESCRIPTOR = _ORIENTATIONLOG,
  __module__ = 'orientationsense_pb2'
  # @@protoc_insertion_point(class_scope:OrientationSense.OrientationLog)
  ))
_sym_db.RegisterMessage(OrientationLog)


# @@protoc_insertion_point(module_scope)