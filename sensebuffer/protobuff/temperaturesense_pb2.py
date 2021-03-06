# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temperaturesense.proto

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
  name='temperaturesense.proto',
  package='TemperatureSense',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16temperaturesense.proto\x12\x10TemperatureSense\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa7\x01\n\x11TemperatureQuanta\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12G\n\x07profile\x18\x02 \x01(\x0b\x32\x36.TemperatureSense.TemperatureQuanta.TemperatureProfile\x1a\x1f\n\x12TemperatureProfile\x12\t\n\x01\x63\x18\x03 \x01(\x02\"F\n\x0eTemperatureLog\x12\x34\n\x07quantas\x18\x01 \x03(\x0b\x32#.TemperatureSense.TemperatureQuantab\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_TEMPERATUREQUANTA_TEMPERATUREPROFILE = _descriptor.Descriptor(
  name='TemperatureProfile',
  full_name='TemperatureSense.TemperatureQuanta.TemperatureProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c', full_name='TemperatureSense.TemperatureQuanta.TemperatureProfile.c', index=0,
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
  serialized_end=245,
)

_TEMPERATUREQUANTA = _descriptor.Descriptor(
  name='TemperatureQuanta',
  full_name='TemperatureSense.TemperatureQuanta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='TemperatureSense.TemperatureQuanta.time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profile', full_name='TemperatureSense.TemperatureQuanta.profile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TEMPERATUREQUANTA_TEMPERATUREPROFILE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=245,
)


_TEMPERATURELOG = _descriptor.Descriptor(
  name='TemperatureLog',
  full_name='TemperatureSense.TemperatureLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quantas', full_name='TemperatureSense.TemperatureLog.quantas', index=0,
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
  serialized_start=247,
  serialized_end=317,
)

_TEMPERATUREQUANTA_TEMPERATUREPROFILE.containing_type = _TEMPERATUREQUANTA
_TEMPERATUREQUANTA.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TEMPERATUREQUANTA.fields_by_name['profile'].message_type = _TEMPERATUREQUANTA_TEMPERATUREPROFILE
_TEMPERATURELOG.fields_by_name['quantas'].message_type = _TEMPERATUREQUANTA
DESCRIPTOR.message_types_by_name['TemperatureQuanta'] = _TEMPERATUREQUANTA
DESCRIPTOR.message_types_by_name['TemperatureLog'] = _TEMPERATURELOG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TemperatureQuanta = _reflection.GeneratedProtocolMessageType('TemperatureQuanta', (_message.Message,), dict(

  TemperatureProfile = _reflection.GeneratedProtocolMessageType('TemperatureProfile', (_message.Message,), dict(
    DESCRIPTOR = _TEMPERATUREQUANTA_TEMPERATUREPROFILE,
    __module__ = 'temperaturesense_pb2'
    # @@protoc_insertion_point(class_scope:TemperatureSense.TemperatureQuanta.TemperatureProfile)
    ))
  ,
  DESCRIPTOR = _TEMPERATUREQUANTA,
  __module__ = 'temperaturesense_pb2'
  # @@protoc_insertion_point(class_scope:TemperatureSense.TemperatureQuanta)
  ))
_sym_db.RegisterMessage(TemperatureQuanta)
_sym_db.RegisterMessage(TemperatureQuanta.TemperatureProfile)

TemperatureLog = _reflection.GeneratedProtocolMessageType('TemperatureLog', (_message.Message,), dict(
  DESCRIPTOR = _TEMPERATURELOG,
  __module__ = 'temperaturesense_pb2'
  # @@protoc_insertion_point(class_scope:TemperatureSense.TemperatureLog)
  ))
_sym_db.RegisterMessage(TemperatureLog)


# @@protoc_insertion_point(module_scope)
