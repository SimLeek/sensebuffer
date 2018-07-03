# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: camerasense.proto

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
  name='camerasense.proto',
  package='CameraSense',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11\x63\x61merasense.proto\x12\x0b\x43\x61meraSense\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc2\x01\n\x0c\x43\x61meraQuanta\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12=\n\x07profile\x18\x02 \x01(\x0b\x32,.CameraSense.CameraQuanta.CameraImageProfile\x1aI\n\x12\x43\x61meraImageProfile\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\x14\n\x0c\x63\x61mera_image\x18\x03 \x01(\x0c\"7\n\tCameraLog\x12*\n\x07quantas\x18\x01 \x03(\x0b\x32\x19.CameraSense.CameraQuantab\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_CAMERAQUANTA_CAMERAIMAGEPROFILE = _descriptor.Descriptor(
  name='CameraImageProfile',
  full_name='CameraSense.CameraQuanta.CameraImageProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='CameraSense.CameraQuanta.CameraImageProfile.width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='CameraSense.CameraQuanta.CameraImageProfile.height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='camera_image', full_name='CameraSense.CameraQuanta.CameraImageProfile.camera_image', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=189,
  serialized_end=262,
)

_CAMERAQUANTA = _descriptor.Descriptor(
  name='CameraQuanta',
  full_name='CameraSense.CameraQuanta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='CameraSense.CameraQuanta.time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profile', full_name='CameraSense.CameraQuanta.profile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CAMERAQUANTA_CAMERAIMAGEPROFILE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=262,
)


_CAMERALOG = _descriptor.Descriptor(
  name='CameraLog',
  full_name='CameraSense.CameraLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quantas', full_name='CameraSense.CameraLog.quantas', index=0,
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
  serialized_start=264,
  serialized_end=319,
)

_CAMERAQUANTA_CAMERAIMAGEPROFILE.containing_type = _CAMERAQUANTA
_CAMERAQUANTA.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CAMERAQUANTA.fields_by_name['profile'].message_type = _CAMERAQUANTA_CAMERAIMAGEPROFILE
_CAMERALOG.fields_by_name['quantas'].message_type = _CAMERAQUANTA
DESCRIPTOR.message_types_by_name['CameraQuanta'] = _CAMERAQUANTA
DESCRIPTOR.message_types_by_name['CameraLog'] = _CAMERALOG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CameraQuanta = _reflection.GeneratedProtocolMessageType('CameraQuanta', (_message.Message,), dict(

  CameraImageProfile = _reflection.GeneratedProtocolMessageType('CameraImageProfile', (_message.Message,), dict(
    DESCRIPTOR = _CAMERAQUANTA_CAMERAIMAGEPROFILE,
    __module__ = 'camerasense_pb2'
    # @@protoc_insertion_point(class_scope:CameraSense.CameraQuanta.CameraImageProfile)
    ))
  ,
  DESCRIPTOR = _CAMERAQUANTA,
  __module__ = 'camerasense_pb2'
  # @@protoc_insertion_point(class_scope:CameraSense.CameraQuanta)
  ))
_sym_db.RegisterMessage(CameraQuanta)
_sym_db.RegisterMessage(CameraQuanta.CameraImageProfile)

CameraLog = _reflection.GeneratedProtocolMessageType('CameraLog', (_message.Message,), dict(
  DESCRIPTOR = _CAMERALOG,
  __module__ = 'camerasense_pb2'
  # @@protoc_insertion_point(class_scope:CameraSense.CameraLog)
  ))
_sym_db.RegisterMessage(CameraLog)


# @@protoc_insertion_point(module_scope)
