# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: security/v1beta1/authorization.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from type.v1beta1 import selector_pb2 as type_dot_v1beta1_dot_selector__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='security/v1beta1/authorization.proto',
  package='istio.security.v1beta1',
  syntax='proto3',
  serialized_options=_b('Z\035istio.io/api/security/v1beta1'),
  serialized_pb=_b('\n$security/v1beta1/authorization.proto\x12\x16istio.security.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1btype/v1beta1/selector.proto\"\xdd\x01\n\x13\x41uthorizationPolicy\x12\x36\n\x08selector\x18\x01 \x01(\x0b\x32$.istio.type.v1beta1.WorkloadSelector\x12+\n\x05rules\x18\x02 \x03(\x0b\x32\x1c.istio.security.v1beta1.Rule\x12\x42\n\x06\x61\x63tion\x18\x03 \x01(\x0e\x32\x32.istio.security.v1beta1.AuthorizationPolicy.Action\"\x1d\n\x06\x41\x63tion\x12\t\n\x05\x41LLOW\x10\x00\x12\x08\n\x04\x44\x45NY\x10\x01\"\x89\x02\n\x04Rule\x12/\n\x04\x66rom\x18\x01 \x03(\x0b\x32!.istio.security.v1beta1.Rule.From\x12+\n\x02to\x18\x02 \x03(\x0b\x32\x1f.istio.security.v1beta1.Rule.To\x12/\n\x04when\x18\x03 \x03(\x0b\x32!.istio.security.v1beta1.Condition\x1a\x36\n\x04\x46rom\x12.\n\x06source\x18\x01 \x01(\x0b\x32\x1e.istio.security.v1beta1.Source\x1a:\n\x02To\x12\x34\n\toperation\x18\x01 \x01(\x0b\x32!.istio.security.v1beta1.Operation\"\xc6\x01\n\x06Source\x12\x12\n\nprincipals\x18\x01 \x03(\t\x12\x16\n\x0enot_principals\x18\x05 \x03(\t\x12\x1a\n\x12request_principals\x18\x02 \x03(\t\x12\x1e\n\x16not_request_principals\x18\x06 \x03(\t\x12\x12\n\nnamespaces\x18\x03 \x03(\t\x12\x16\n\x0enot_namespaces\x18\x07 \x03(\t\x12\x11\n\tip_blocks\x18\x04 \x03(\t\x12\x15\n\rnot_ip_blocks\x18\x08 \x03(\t\"\x97\x01\n\tOperation\x12\r\n\x05hosts\x18\x01 \x03(\t\x12\x11\n\tnot_hosts\x18\x05 \x03(\t\x12\r\n\x05ports\x18\x02 \x03(\t\x12\x11\n\tnot_ports\x18\x06 \x03(\t\x12\x0f\n\x07methods\x18\x03 \x03(\t\x12\x13\n\x0bnot_methods\x18\x07 \x03(\t\x12\r\n\x05paths\x18\x04 \x03(\t\x12\x11\n\tnot_paths\x18\x08 \x03(\t\"A\n\tCondition\x12\x10\n\x03key\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x0e\n\x06values\x18\x02 \x03(\t\x12\x12\n\nnot_values\x18\x03 \x03(\tB\x1fZ\x1distio.io/api/security/v1beta1b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,type_dot_v1beta1_dot_selector__pb2.DESCRIPTOR,])



_AUTHORIZATIONPOLICY_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='istio.security.v1beta1.AuthorizationPolicy.Action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALLOW', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DENY', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=319,
  serialized_end=348,
)
_sym_db.RegisterEnumDescriptor(_AUTHORIZATIONPOLICY_ACTION)


_AUTHORIZATIONPOLICY = _descriptor.Descriptor(
  name='AuthorizationPolicy',
  full_name='istio.security.v1beta1.AuthorizationPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='selector', full_name='istio.security.v1beta1.AuthorizationPolicy.selector', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rules', full_name='istio.security.v1beta1.AuthorizationPolicy.rules', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='istio.security.v1beta1.AuthorizationPolicy.action', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AUTHORIZATIONPOLICY_ACTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=348,
)


_RULE_FROM = _descriptor.Descriptor(
  name='From',
  full_name='istio.security.v1beta1.Rule.From',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='istio.security.v1beta1.Rule.From.source', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=502,
  serialized_end=556,
)

_RULE_TO = _descriptor.Descriptor(
  name='To',
  full_name='istio.security.v1beta1.Rule.To',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='istio.security.v1beta1.Rule.To.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=558,
  serialized_end=616,
)

_RULE = _descriptor.Descriptor(
  name='Rule',
  full_name='istio.security.v1beta1.Rule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from', full_name='istio.security.v1beta1.Rule.from', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to', full_name='istio.security.v1beta1.Rule.to', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='when', full_name='istio.security.v1beta1.Rule.when', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RULE_FROM, _RULE_TO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=351,
  serialized_end=616,
)


_SOURCE = _descriptor.Descriptor(
  name='Source',
  full_name='istio.security.v1beta1.Source',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='principals', full_name='istio.security.v1beta1.Source.principals', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_principals', full_name='istio.security.v1beta1.Source.not_principals', index=1,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_principals', full_name='istio.security.v1beta1.Source.request_principals', index=2,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_request_principals', full_name='istio.security.v1beta1.Source.not_request_principals', index=3,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='namespaces', full_name='istio.security.v1beta1.Source.namespaces', index=4,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_namespaces', full_name='istio.security.v1beta1.Source.not_namespaces', index=5,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip_blocks', full_name='istio.security.v1beta1.Source.ip_blocks', index=6,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_ip_blocks', full_name='istio.security.v1beta1.Source.not_ip_blocks', index=7,
      number=8, type=9, cpp_type=9, label=3,
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
  serialized_start=619,
  serialized_end=817,
)


_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='istio.security.v1beta1.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hosts', full_name='istio.security.v1beta1.Operation.hosts', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_hosts', full_name='istio.security.v1beta1.Operation.not_hosts', index=1,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ports', full_name='istio.security.v1beta1.Operation.ports', index=2,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_ports', full_name='istio.security.v1beta1.Operation.not_ports', index=3,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='methods', full_name='istio.security.v1beta1.Operation.methods', index=4,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_methods', full_name='istio.security.v1beta1.Operation.not_methods', index=5,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paths', full_name='istio.security.v1beta1.Operation.paths', index=6,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_paths', full_name='istio.security.v1beta1.Operation.not_paths', index=7,
      number=8, type=9, cpp_type=9, label=3,
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
  serialized_start=820,
  serialized_end=971,
)


_CONDITION = _descriptor.Descriptor(
  name='Condition',
  full_name='istio.security.v1beta1.Condition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='istio.security.v1beta1.Condition.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='istio.security.v1beta1.Condition.values', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_values', full_name='istio.security.v1beta1.Condition.not_values', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=973,
  serialized_end=1038,
)

_AUTHORIZATIONPOLICY.fields_by_name['selector'].message_type = type_dot_v1beta1_dot_selector__pb2._WORKLOADSELECTOR
_AUTHORIZATIONPOLICY.fields_by_name['rules'].message_type = _RULE
_AUTHORIZATIONPOLICY.fields_by_name['action'].enum_type = _AUTHORIZATIONPOLICY_ACTION
_AUTHORIZATIONPOLICY_ACTION.containing_type = _AUTHORIZATIONPOLICY
_RULE_FROM.fields_by_name['source'].message_type = _SOURCE
_RULE_FROM.containing_type = _RULE
_RULE_TO.fields_by_name['operation'].message_type = _OPERATION
_RULE_TO.containing_type = _RULE
_RULE.fields_by_name['from'].message_type = _RULE_FROM
_RULE.fields_by_name['to'].message_type = _RULE_TO
_RULE.fields_by_name['when'].message_type = _CONDITION
DESCRIPTOR.message_types_by_name['AuthorizationPolicy'] = _AUTHORIZATIONPOLICY
DESCRIPTOR.message_types_by_name['Rule'] = _RULE
DESCRIPTOR.message_types_by_name['Source'] = _SOURCE
DESCRIPTOR.message_types_by_name['Operation'] = _OPERATION
DESCRIPTOR.message_types_by_name['Condition'] = _CONDITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuthorizationPolicy = _reflection.GeneratedProtocolMessageType('AuthorizationPolicy', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORIZATIONPOLICY,
  '__module__' : 'security.v1beta1.authorization_pb2'
  # @@protoc_insertion_point(class_scope:istio.security.v1beta1.AuthorizationPolicy)
  })
_sym_db.RegisterMessage(AuthorizationPolicy)

Rule = _reflection.GeneratedProtocolMessageType('Rule', (_message.Message,), {

  'From' : _reflection.GeneratedProtocolMessageType('From', (_message.Message,), {
    'DESCRIPTOR' : _RULE_FROM,
    '__module__' : 'security.v1beta1.authorization_pb2'
    # @@protoc_insertion_point(class_scope:istio.security.v1beta1.Rule.From)
    })
  ,

  'To' : _reflection.GeneratedProtocolMessageType('To', (_message.Message,), {
    'DESCRIPTOR' : _RULE_TO,
    '__module__' : 'security.v1beta1.authorization_pb2'
    # @@protoc_insertion_point(class_scope:istio.security.v1beta1.Rule.To)
    })
  ,
  'DESCRIPTOR' : _RULE,
  '__module__' : 'security.v1beta1.authorization_pb2'
  # @@protoc_insertion_point(class_scope:istio.security.v1beta1.Rule)
  })
_sym_db.RegisterMessage(Rule)
_sym_db.RegisterMessage(Rule.From)
_sym_db.RegisterMessage(Rule.To)

Source = _reflection.GeneratedProtocolMessageType('Source', (_message.Message,), {
  'DESCRIPTOR' : _SOURCE,
  '__module__' : 'security.v1beta1.authorization_pb2'
  # @@protoc_insertion_point(class_scope:istio.security.v1beta1.Source)
  })
_sym_db.RegisterMessage(Source)

Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), {
  'DESCRIPTOR' : _OPERATION,
  '__module__' : 'security.v1beta1.authorization_pb2'
  # @@protoc_insertion_point(class_scope:istio.security.v1beta1.Operation)
  })
_sym_db.RegisterMessage(Operation)

Condition = _reflection.GeneratedProtocolMessageType('Condition', (_message.Message,), {
  'DESCRIPTOR' : _CONDITION,
  '__module__' : 'security.v1beta1.authorization_pb2'
  # @@protoc_insertion_point(class_scope:istio.security.v1beta1.Condition)
  })
_sym_db.RegisterMessage(Condition)


DESCRIPTOR._options = None
_CONDITION.fields_by_name['key']._options = None
# @@protoc_insertion_point(module_scope)
