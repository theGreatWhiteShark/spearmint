# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spearmint.proto

from __future__ import absolute_import
import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='spearmint.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0fspearmint.proto\"\xcc\x01\n\x03Job\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x10\n\x08\x65xpt_dir\x18\x02 \x02(\t\x12\x0c\n\x04name\x18\x03 \x02(\t\x12\x1b\n\x08language\x18\x04 \x02(\x0e\x32\t.Language\x12\x0e\n\x06status\x18\x05 \x01(\t\x12\x19\n\x05param\x18\x06 \x03(\x0b\x32\n.Parameter\x12\x10\n\x08submit_t\x18\x07 \x01(\x04\x12\x0f\n\x07start_t\x18\x08 \x01(\x04\x12\r\n\x05\x65nd_t\x18\t \x01(\x04\x12\r\n\x05value\x18\n \x01(\x01\x12\x10\n\x08\x64uration\x18\x0b \x01(\x01\"L\n\tParameter\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0f\n\x07int_val\x18\x02 \x03(\x03\x12\x0f\n\x07str_val\x18\x03 \x03(\t\x12\x0f\n\x07\x64\x62l_val\x18\x04 \x03(\x01\"\x91\x02\n\nExperiment\x12\x1b\n\x08language\x18\x01 \x02(\x0e\x32\t.Language\x12\x0c\n\x04name\x18\x02 \x02(\t\x12+\n\x08variable\x18\x03 \x03(\x0b\x32\x19.Experiment.ParameterSpec\x1a\xaa\x01\n\rParameterSpec\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04size\x18\x02 \x02(\r\x12,\n\x04type\x18\x03 \x02(\x0e\x32\x1e.Experiment.ParameterSpec.Type\x12\x0f\n\x07options\x18\x04 \x03(\t\x12\x0b\n\x03min\x18\x05 \x01(\x01\x12\x0b\n\x03max\x18\x06 \x01(\x01\"$\n\x04Type\x12\x07\n\x03INT\x10\x01\x12\t\n\x05\x46LOAT\x10\x02\x12\x08\n\x04\x45NUM\x10\x03*A\n\x08Language\x12\n\n\x06MATLAB\x10\x01\x12\n\n\x06PYTHON\x10\x02\x12\t\n\x05SHELL\x10\x03\x12\x07\n\x03MCR\x10\x04\x12\t\n\x05TORCH\x10\x05')
)

_LANGUAGE = _descriptor.EnumDescriptor(
  name='Language',
  full_name='Language',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MATLAB', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PYTHON', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHELL', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MCR', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TORCH', index=4, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=580,
  serialized_end=645,
)
_sym_db.RegisterEnumDescriptor(_LANGUAGE)

Language = enum_type_wrapper.EnumTypeWrapper(_LANGUAGE)
MATLAB = 1
PYTHON = 2
SHELL = 3
MCR = 4
TORCH = 5


_EXPERIMENT_PARAMETERSPEC_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Experiment.ParameterSpec.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INT', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENUM', index=2, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=542,
  serialized_end=578,
)
_sym_db.RegisterEnumDescriptor(_EXPERIMENT_PARAMETERSPEC_TYPE)


_JOB = _descriptor.Descriptor(
  name='Job',
  full_name='Job',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Job.id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expt_dir', full_name='Job.expt_dir', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Job.name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language', full_name='Job.language', index=3,
      number=4, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='Job.status', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='param', full_name='Job.param', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='submit_t', full_name='Job.submit_t', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_t', full_name='Job.start_t', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_t', full_name='Job.end_t', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Job.value', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='Job.duration', index=10,
      number=11, type=1, cpp_type=5, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=224,
)


_PARAMETER = _descriptor.Descriptor(
  name='Parameter',
  full_name='Parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Parameter.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_val', full_name='Parameter.int_val', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='str_val', full_name='Parameter.str_val', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbl_val', full_name='Parameter.dbl_val', index=3,
      number=4, type=1, cpp_type=5, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=302,
)


_EXPERIMENT_PARAMETERSPEC = _descriptor.Descriptor(
  name='ParameterSpec',
  full_name='Experiment.ParameterSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Experiment.ParameterSpec.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='Experiment.ParameterSpec.size', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='Experiment.ParameterSpec.type', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='Experiment.ParameterSpec.options', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min', full_name='Experiment.ParameterSpec.min', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='Experiment.ParameterSpec.max', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXPERIMENT_PARAMETERSPEC_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=408,
  serialized_end=578,
)

_EXPERIMENT = _descriptor.Descriptor(
  name='Experiment',
  full_name='Experiment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='Experiment.language', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Experiment.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variable', full_name='Experiment.variable', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EXPERIMENT_PARAMETERSPEC, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=305,
  serialized_end=578,
)

_JOB.fields_by_name['language'].enum_type = _LANGUAGE
_JOB.fields_by_name['param'].message_type = _PARAMETER
_EXPERIMENT_PARAMETERSPEC.fields_by_name['type'].enum_type = _EXPERIMENT_PARAMETERSPEC_TYPE
_EXPERIMENT_PARAMETERSPEC.containing_type = _EXPERIMENT
_EXPERIMENT_PARAMETERSPEC_TYPE.containing_type = _EXPERIMENT_PARAMETERSPEC
_EXPERIMENT.fields_by_name['language'].enum_type = _LANGUAGE
_EXPERIMENT.fields_by_name['variable'].message_type = _EXPERIMENT_PARAMETERSPEC
DESCRIPTOR.message_types_by_name['Job'] = _JOB
DESCRIPTOR.message_types_by_name['Parameter'] = _PARAMETER
DESCRIPTOR.message_types_by_name['Experiment'] = _EXPERIMENT
DESCRIPTOR.enum_types_by_name['Language'] = _LANGUAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), dict(
  DESCRIPTOR = _JOB,
  __module__ = 'spearmint_pb2'
  # @@protoc_insertion_point(class_scope:Job)
  ))
_sym_db.RegisterMessage(Job)

Parameter = _reflection.GeneratedProtocolMessageType('Parameter', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETER,
  __module__ = 'spearmint_pb2'
  # @@protoc_insertion_point(class_scope:Parameter)
  ))
_sym_db.RegisterMessage(Parameter)

Experiment = _reflection.GeneratedProtocolMessageType('Experiment', (_message.Message,), dict(

  ParameterSpec = _reflection.GeneratedProtocolMessageType('ParameterSpec', (_message.Message,), dict(
    DESCRIPTOR = _EXPERIMENT_PARAMETERSPEC,
    __module__ = 'spearmint_pb2'
    # @@protoc_insertion_point(class_scope:Experiment.ParameterSpec)
    ))
  ,
  DESCRIPTOR = _EXPERIMENT,
  __module__ = 'spearmint_pb2'
  # @@protoc_insertion_point(class_scope:Experiment)
  ))
_sym_db.RegisterMessage(Experiment)
_sym_db.RegisterMessage(Experiment.ParameterSpec)


# @@protoc_insertion_point(module_scope)
