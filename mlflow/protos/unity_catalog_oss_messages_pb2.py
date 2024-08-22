
import google.protobuf
from packaging.version import Version
if Version(google.protobuf.__version__).major >= 5:
  # -*- coding: utf-8 -*-
  # Generated by the protocol buffer compiler.  DO NOT EDIT!
  # source: unity_catalog_oss_messages.proto
  # Protobuf Python Version: 5.26.0
  """Generated protocol buffer code."""
  from google.protobuf import descriptor as _descriptor
  from google.protobuf import descriptor_pool as _descriptor_pool
  from google.protobuf import symbol_database as _symbol_database
  from google.protobuf.internal import builder as _builder
  # @@protoc_insertion_point(imports)

  _sym_db = _symbol_database.Default()


  from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2
  from . import databricks_pb2 as databricks__pb2


  DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n unity_catalog_oss_messages.proto\x12\x13mlflow.unitycatalog\x1a\x15scalapb/scalapb.proto\x1a\x10\x64\x61tabricks.proto\"\xfd\x01\n\x13RegisteredModelInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61talog_name\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t\x12\x0f\n\x07\x63omment\x18\x05 \x01(\t\x12\x18\n\x10storage_location\x18\x06 \x01(\t\x12\x11\n\tfull_name\x18\t \x01(\t\x12\x12\n\ncreated_at\x18\x0b \x01(\x03\x12\x12\n\ncreated_by\x18\x0c \x01(\t\x12\x12\n\nupdated_at\x18\r \x01(\x03\x12\x12\n\nupdated_by\x18\x0e \x01(\t\x12\n\n\x02id\x18\x12 \x01(\t\x12\x13\n\x0b\x62rowse_only\x18\x15 \x01(\x08\"\xd0\x01\n\x15\x43reateRegisteredModel\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61talog_name\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t\x12\x0f\n\x07\x63omment\x18\x05 \x01(\t\x12\x18\n\x10storage_location\x18\x06 \x01(\t\x1aS\n\x08Response\x12G\n\x15registered_model_info\x18\x01 \x01(\x0b\x32(.mlflow.unitycatalog.RegisteredModelInfo\"K\n\x15\x44\x65leteRegisteredModel\x12\x17\n\tfull_name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\r\n\x05\x66orce\x18\x02 \x01(\x08\x1a\n\n\x08Response\"\x88\x01\n\x12GetRegisteredModel\x12\x17\n\tfull_name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x1aY\n\x08Response\x12M\n\x15registered_model_info\x18\x01 \x01(\x0b\x32(.mlflow.unitycatalog.RegisteredModelInfoB\x04\x80\x87\x19\x01\"\xa2\x01\n\x15UpdateRegisteredModel\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x10\n\x08new_name\x18\x03 \x01(\t\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\x1aS\n\x08Response\x12G\n\x15registered_model_info\x18\x01 \x01(\x0b\x32(.mlflow.unitycatalog.RegisteredModelInfo\"\xc2\x02\n\x10ModelVersionInfo\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61talog_name\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t\x12\x0e\n\x06source\x18\x05 \x01(\t\x12\x0f\n\x07\x63omment\x18\x04 \x01(\t\x12\x0e\n\x06run_id\x18\x06 \x01(\t\x12\x37\n\x06status\x18\x08 \x01(\x0e\x32\'.mlflow.unitycatalog.ModelVersionStatus\x12\x0f\n\x07version\x18\t \x01(\x03\x12\x18\n\x10storage_location\x18\n \x01(\t\x12\x12\n\ncreated_at\x18\x0c \x01(\x03\x12\x12\n\ncreated_by\x18\r \x01(\t\x12\x12\n\nupdated_at\x18\x0e \x01(\x03\x12\x12\n\nupdated_by\x18\x0f \x01(\t\x12\n\n\x02id\x18\x10 \x01(\t\"\xd3\x01\n\x12\x43reateModelVersion\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61talog_name\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t\x12\x0e\n\x06source\x18\x04 \x01(\t\x12\x0e\n\x06run_id\x18\x05 \x01(\t\x12\x0f\n\x07\x63omment\x18\x06 \x01(\t\x1aM\n\x08Response\x12\x41\n\x12model_version_info\x18\x01 \x01(\x0b\x32%.mlflow.unitycatalog.ModelVersionInfo\"D\n\x12\x44\x65leteModelVersion\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x1a\n\n\x08Response\"\x8f\x01\n\x14\x46inalizeModelVersion\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x1aS\n\x08Response\x12G\n\x12model_version_info\x18\x01 \x01(\x0b\x32%.mlflow.unitycatalog.ModelVersionInfoB\x04\x80\x87\x19\x01\"\x8a\x01\n\x0fGetModelVersion\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x1aS\n\x08Response\x12G\n\x12model_version_info\x18\x01 \x01(\x0b\x32%.mlflow.unitycatalog.ModelVersionInfoB\x04\x80\x87\x19\x01\"\x98\x01\n\x12UpdateModelVersion\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\x1aM\n\x08Response\x12\x41\n\x12model_version_info\x18\x01 \x01(\x0b\x32%.mlflow.unitycatalog.ModelVersionInfo*t\n\x12ModelVersionStatus\x12 \n\x1cMODEL_VERSION_STATUS_UNKNOWN\x10\x00\x12\x18\n\x14PENDING_REGISTRATION\x10\x01\x12\x17\n\x13\x46\x41ILED_REGISTRATION\x10\x02\x12\t\n\x05READY\x10\x03\x42\x31\n\'com.databricks.api.proto.managedcatalog\xa0\x01\x01\xe2?\x02\x10\x01')

  _globals = globals()
  _builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
  _builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'unity_catalog_oss_messages_pb2', _globals)
  if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\'com.databricks.api.proto.managedcatalog\240\001\001\342?\002\020\001'
    _globals['_DELETEREGISTEREDMODEL'].fields_by_name['full_name']._loaded_options = None
    _globals['_DELETEREGISTEREDMODEL'].fields_by_name['full_name']._serialized_options = b'\370\206\031\001'
    _globals['_GETREGISTEREDMODEL_RESPONSE'].fields_by_name['registered_model_info']._loaded_options = None
    _globals['_GETREGISTEREDMODEL_RESPONSE'].fields_by_name['registered_model_info']._serialized_options = b'\200\207\031\001'
    _globals['_GETREGISTEREDMODEL'].fields_by_name['full_name']._loaded_options = None
    _globals['_GETREGISTEREDMODEL'].fields_by_name['full_name']._serialized_options = b'\370\206\031\001'
    _globals['_FINALIZEMODELVERSION_RESPONSE'].fields_by_name['model_version_info']._loaded_options = None
    _globals['_FINALIZEMODELVERSION_RESPONSE'].fields_by_name['model_version_info']._serialized_options = b'\200\207\031\001'
    _globals['_GETMODELVERSION_RESPONSE'].fields_by_name['model_version_info']._loaded_options = None
    _globals['_GETMODELVERSION_RESPONSE'].fields_by_name['model_version_info']._serialized_options = b'\200\207\031\001'
    _globals['_MODELVERSIONSTATUS']._serialized_start=1997
    _globals['_MODELVERSIONSTATUS']._serialized_end=2113
    _globals['_REGISTEREDMODELINFO']._serialized_start=99
    _globals['_REGISTEREDMODELINFO']._serialized_end=352
    _globals['_CREATEREGISTEREDMODEL']._serialized_start=355
    _globals['_CREATEREGISTEREDMODEL']._serialized_end=563
    _globals['_CREATEREGISTEREDMODEL_RESPONSE']._serialized_start=480
    _globals['_CREATEREGISTEREDMODEL_RESPONSE']._serialized_end=563
    _globals['_DELETEREGISTEREDMODEL']._serialized_start=565
    _globals['_DELETEREGISTEREDMODEL']._serialized_end=640
    _globals['_DELETEREGISTEREDMODEL_RESPONSE']._serialized_start=480
    _globals['_DELETEREGISTEREDMODEL_RESPONSE']._serialized_end=490
    _globals['_GETREGISTEREDMODEL']._serialized_start=643
    _globals['_GETREGISTEREDMODEL']._serialized_end=779
    _globals['_GETREGISTEREDMODEL_RESPONSE']._serialized_start=690
    _globals['_GETREGISTEREDMODEL_RESPONSE']._serialized_end=779
    _globals['_UPDATEREGISTEREDMODEL']._serialized_start=782
    _globals['_UPDATEREGISTEREDMODEL']._serialized_end=944
    _globals['_UPDATEREGISTEREDMODEL_RESPONSE']._serialized_start=480
    _globals['_UPDATEREGISTEREDMODEL_RESPONSE']._serialized_end=563
    _globals['_MODELVERSIONINFO']._serialized_start=947
    _globals['_MODELVERSIONINFO']._serialized_end=1269
    _globals['_CREATEMODELVERSION']._serialized_start=1272
    _globals['_CREATEMODELVERSION']._serialized_end=1483
    _globals['_CREATEMODELVERSION_RESPONSE']._serialized_start=1406
    _globals['_CREATEMODELVERSION_RESPONSE']._serialized_end=1483
    _globals['_DELETEMODELVERSION']._serialized_start=1485
    _globals['_DELETEMODELVERSION']._serialized_end=1553
    _globals['_DELETEMODELVERSION_RESPONSE']._serialized_start=480
    _globals['_DELETEMODELVERSION_RESPONSE']._serialized_end=490
    _globals['_FINALIZEMODELVERSION']._serialized_start=1556
    _globals['_FINALIZEMODELVERSION']._serialized_end=1699
    _globals['_FINALIZEMODELVERSION_RESPONSE']._serialized_start=1616
    _globals['_FINALIZEMODELVERSION_RESPONSE']._serialized_end=1699
    _globals['_GETMODELVERSION']._serialized_start=1702
    _globals['_GETMODELVERSION']._serialized_end=1840
    _globals['_GETMODELVERSION_RESPONSE']._serialized_start=1616
    _globals['_GETMODELVERSION_RESPONSE']._serialized_end=1699
    _globals['_UPDATEMODELVERSION']._serialized_start=1843
    _globals['_UPDATEMODELVERSION']._serialized_end=1995
    _globals['_UPDATEMODELVERSION_RESPONSE']._serialized_start=1406
    _globals['_UPDATEMODELVERSION_RESPONSE']._serialized_end=1483
  # @@protoc_insertion_point(module_scope)

else:
  # -*- coding: utf-8 -*-
  # Generated by the protocol buffer compiler.  DO NOT EDIT!
  # source: unity_catalog_oss_messages.proto
  """Generated protocol buffer code."""
  from google.protobuf.internal import enum_type_wrapper
  from google.protobuf import descriptor as _descriptor
  from google.protobuf import descriptor_pool as _descriptor_pool
  from google.protobuf import message as _message
  from google.protobuf import reflection as _reflection
  from google.protobuf import symbol_database as _symbol_database
  # @@protoc_insertion_point(imports)

  _sym_db = _symbol_database.Default()


  from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2
  from . import databricks_pb2 as databricks__pb2


  DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n unity_catalog_oss_messages.proto\x12\x13mlflow.unitycatalog\x1a\x15scalapb/scalapb.proto\x1a\x10\x64\x61tabricks.proto\"\xfd\x01\n\x13RegisteredModelInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61talog_name\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t\x12\x0f\n\x07\x63omment\x18\x05 \x01(\t\x12\x18\n\x10storage_location\x18\x06 \x01(\t\x12\x11\n\tfull_name\x18\t \x01(\t\x12\x12\n\ncreated_at\x18\x0b \x01(\x03\x12\x12\n\ncreated_by\x18\x0c \x01(\t\x12\x12\n\nupdated_at\x18\r \x01(\x03\x12\x12\n\nupdated_by\x18\x0e \x01(\t\x12\n\n\x02id\x18\x12 \x01(\t\x12\x13\n\x0b\x62rowse_only\x18\x15 \x01(\x08\"\xd0\x01\n\x15\x43reateRegisteredModel\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61talog_name\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t\x12\x0f\n\x07\x63omment\x18\x05 \x01(\t\x12\x18\n\x10storage_location\x18\x06 \x01(\t\x1aS\n\x08Response\x12G\n\x15registered_model_info\x18\x01 \x01(\x0b\x32(.mlflow.unitycatalog.RegisteredModelInfo\"K\n\x15\x44\x65leteRegisteredModel\x12\x17\n\tfull_name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\r\n\x05\x66orce\x18\x02 \x01(\x08\x1a\n\n\x08Response\"\x88\x01\n\x12GetRegisteredModel\x12\x17\n\tfull_name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x1aY\n\x08Response\x12M\n\x15registered_model_info\x18\x01 \x01(\x0b\x32(.mlflow.unitycatalog.RegisteredModelInfoB\x04\x80\x87\x19\x01\"\xa2\x01\n\x15UpdateRegisteredModel\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x10\n\x08new_name\x18\x03 \x01(\t\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\x1aS\n\x08Response\x12G\n\x15registered_model_info\x18\x01 \x01(\x0b\x32(.mlflow.unitycatalog.RegisteredModelInfo\"\xc2\x02\n\x10ModelVersionInfo\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61talog_name\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t\x12\x0e\n\x06source\x18\x05 \x01(\t\x12\x0f\n\x07\x63omment\x18\x04 \x01(\t\x12\x0e\n\x06run_id\x18\x06 \x01(\t\x12\x37\n\x06status\x18\x08 \x01(\x0e\x32\'.mlflow.unitycatalog.ModelVersionStatus\x12\x0f\n\x07version\x18\t \x01(\x03\x12\x18\n\x10storage_location\x18\n \x01(\t\x12\x12\n\ncreated_at\x18\x0c \x01(\x03\x12\x12\n\ncreated_by\x18\r \x01(\t\x12\x12\n\nupdated_at\x18\x0e \x01(\x03\x12\x12\n\nupdated_by\x18\x0f \x01(\t\x12\n\n\x02id\x18\x10 \x01(\t\"\xd3\x01\n\x12\x43reateModelVersion\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61talog_name\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t\x12\x0e\n\x06source\x18\x04 \x01(\t\x12\x0e\n\x06run_id\x18\x05 \x01(\t\x12\x0f\n\x07\x63omment\x18\x06 \x01(\t\x1aM\n\x08Response\x12\x41\n\x12model_version_info\x18\x01 \x01(\x0b\x32%.mlflow.unitycatalog.ModelVersionInfo\"D\n\x12\x44\x65leteModelVersion\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x1a\n\n\x08Response\"\x8f\x01\n\x14\x46inalizeModelVersion\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x1aS\n\x08Response\x12G\n\x12model_version_info\x18\x01 \x01(\x0b\x32%.mlflow.unitycatalog.ModelVersionInfoB\x04\x80\x87\x19\x01\"\x8a\x01\n\x0fGetModelVersion\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x1aS\n\x08Response\x12G\n\x12model_version_info\x18\x01 \x01(\x0b\x32%.mlflow.unitycatalog.ModelVersionInfoB\x04\x80\x87\x19\x01\"\x98\x01\n\x12UpdateModelVersion\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\x1aM\n\x08Response\x12\x41\n\x12model_version_info\x18\x01 \x01(\x0b\x32%.mlflow.unitycatalog.ModelVersionInfo*t\n\x12ModelVersionStatus\x12 \n\x1cMODEL_VERSION_STATUS_UNKNOWN\x10\x00\x12\x18\n\x14PENDING_REGISTRATION\x10\x01\x12\x17\n\x13\x46\x41ILED_REGISTRATION\x10\x02\x12\t\n\x05READY\x10\x03\x42\x31\n\'com.databricks.api.proto.managedcatalog\xa0\x01\x01\xe2?\x02\x10\x01')

  _MODELVERSIONSTATUS = DESCRIPTOR.enum_types_by_name['ModelVersionStatus']
  ModelVersionStatus = enum_type_wrapper.EnumTypeWrapper(_MODELVERSIONSTATUS)
  MODEL_VERSION_STATUS_UNKNOWN = 0
  PENDING_REGISTRATION = 1
  FAILED_REGISTRATION = 2
  READY = 3


  _REGISTEREDMODELINFO = DESCRIPTOR.message_types_by_name['RegisteredModelInfo']
  _CREATEREGISTEREDMODEL = DESCRIPTOR.message_types_by_name['CreateRegisteredModel']
  _CREATEREGISTEREDMODEL_RESPONSE = _CREATEREGISTEREDMODEL.nested_types_by_name['Response']
  _DELETEREGISTEREDMODEL = DESCRIPTOR.message_types_by_name['DeleteRegisteredModel']
  _DELETEREGISTEREDMODEL_RESPONSE = _DELETEREGISTEREDMODEL.nested_types_by_name['Response']
  _GETREGISTEREDMODEL = DESCRIPTOR.message_types_by_name['GetRegisteredModel']
  _GETREGISTEREDMODEL_RESPONSE = _GETREGISTEREDMODEL.nested_types_by_name['Response']
  _UPDATEREGISTEREDMODEL = DESCRIPTOR.message_types_by_name['UpdateRegisteredModel']
  _UPDATEREGISTEREDMODEL_RESPONSE = _UPDATEREGISTEREDMODEL.nested_types_by_name['Response']
  _MODELVERSIONINFO = DESCRIPTOR.message_types_by_name['ModelVersionInfo']
  _CREATEMODELVERSION = DESCRIPTOR.message_types_by_name['CreateModelVersion']
  _CREATEMODELVERSION_RESPONSE = _CREATEMODELVERSION.nested_types_by_name['Response']
  _DELETEMODELVERSION = DESCRIPTOR.message_types_by_name['DeleteModelVersion']
  _DELETEMODELVERSION_RESPONSE = _DELETEMODELVERSION.nested_types_by_name['Response']
  _FINALIZEMODELVERSION = DESCRIPTOR.message_types_by_name['FinalizeModelVersion']
  _FINALIZEMODELVERSION_RESPONSE = _FINALIZEMODELVERSION.nested_types_by_name['Response']
  _GETMODELVERSION = DESCRIPTOR.message_types_by_name['GetModelVersion']
  _GETMODELVERSION_RESPONSE = _GETMODELVERSION.nested_types_by_name['Response']
  _UPDATEMODELVERSION = DESCRIPTOR.message_types_by_name['UpdateModelVersion']
  _UPDATEMODELVERSION_RESPONSE = _UPDATEMODELVERSION.nested_types_by_name['Response']
  RegisteredModelInfo = _reflection.GeneratedProtocolMessageType('RegisteredModelInfo', (_message.Message,), {
    'DESCRIPTOR' : _REGISTEREDMODELINFO,
    '__module__' : 'unity_catalog_oss_messages_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.RegisteredModelInfo)
    })
  _sym_db.RegisterMessage(RegisteredModelInfo)

  CreateRegisteredModel = _reflection.GeneratedProtocolMessageType('CreateRegisteredModel', (_message.Message,), {

    'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
      'DESCRIPTOR' : _CREATEREGISTEREDMODEL_RESPONSE,
      '__module__' : 'unity_catalog_oss_messages_pb2'
      # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.CreateRegisteredModel.Response)
      })
    ,
    'DESCRIPTOR' : _CREATEREGISTEREDMODEL,
    '__module__' : 'unity_catalog_oss_messages_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.CreateRegisteredModel)
    })
  _sym_db.RegisterMessage(CreateRegisteredModel)
  _sym_db.RegisterMessage(CreateRegisteredModel.Response)

  DeleteRegisteredModel = _reflection.GeneratedProtocolMessageType('DeleteRegisteredModel', (_message.Message,), {

    'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
      'DESCRIPTOR' : _DELETEREGISTEREDMODEL_RESPONSE,
      '__module__' : 'unity_catalog_oss_messages_pb2'
      # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.DeleteRegisteredModel.Response)
      })
    ,
    'DESCRIPTOR' : _DELETEREGISTEREDMODEL,
    '__module__' : 'unity_catalog_oss_messages_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.DeleteRegisteredModel)
    })
  _sym_db.RegisterMessage(DeleteRegisteredModel)
  _sym_db.RegisterMessage(DeleteRegisteredModel.Response)

  GetRegisteredModel = _reflection.GeneratedProtocolMessageType('GetRegisteredModel', (_message.Message,), {

    'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
      'DESCRIPTOR' : _GETREGISTEREDMODEL_RESPONSE,
      '__module__' : 'unity_catalog_oss_messages_pb2'
      # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.GetRegisteredModel.Response)
      })
    ,
    'DESCRIPTOR' : _GETREGISTEREDMODEL,
    '__module__' : 'unity_catalog_oss_messages_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.GetRegisteredModel)
    })
  _sym_db.RegisterMessage(GetRegisteredModel)
  _sym_db.RegisterMessage(GetRegisteredModel.Response)

  UpdateRegisteredModel = _reflection.GeneratedProtocolMessageType('UpdateRegisteredModel', (_message.Message,), {

    'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
      'DESCRIPTOR' : _UPDATEREGISTEREDMODEL_RESPONSE,
      '__module__' : 'unity_catalog_oss_messages_pb2'
      # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.UpdateRegisteredModel.Response)
      })
    ,
    'DESCRIPTOR' : _UPDATEREGISTEREDMODEL,
    '__module__' : 'unity_catalog_oss_messages_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.UpdateRegisteredModel)
    })
  _sym_db.RegisterMessage(UpdateRegisteredModel)
  _sym_db.RegisterMessage(UpdateRegisteredModel.Response)

  ModelVersionInfo = _reflection.GeneratedProtocolMessageType('ModelVersionInfo', (_message.Message,), {
    'DESCRIPTOR' : _MODELVERSIONINFO,
    '__module__' : 'unity_catalog_oss_messages_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.ModelVersionInfo)
    })
  _sym_db.RegisterMessage(ModelVersionInfo)

  CreateModelVersion = _reflection.GeneratedProtocolMessageType('CreateModelVersion', (_message.Message,), {

    'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
      'DESCRIPTOR' : _CREATEMODELVERSION_RESPONSE,
      '__module__' : 'unity_catalog_oss_messages_pb2'
      # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.CreateModelVersion.Response)
      })
    ,
    'DESCRIPTOR' : _CREATEMODELVERSION,
    '__module__' : 'unity_catalog_oss_messages_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.CreateModelVersion)
    })
  _sym_db.RegisterMessage(CreateModelVersion)
  _sym_db.RegisterMessage(CreateModelVersion.Response)

  DeleteModelVersion = _reflection.GeneratedProtocolMessageType('DeleteModelVersion', (_message.Message,), {

    'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
      'DESCRIPTOR' : _DELETEMODELVERSION_RESPONSE,
      '__module__' : 'unity_catalog_oss_messages_pb2'
      # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.DeleteModelVersion.Response)
      })
    ,
    'DESCRIPTOR' : _DELETEMODELVERSION,
    '__module__' : 'unity_catalog_oss_messages_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.DeleteModelVersion)
    })
  _sym_db.RegisterMessage(DeleteModelVersion)
  _sym_db.RegisterMessage(DeleteModelVersion.Response)

  FinalizeModelVersion = _reflection.GeneratedProtocolMessageType('FinalizeModelVersion', (_message.Message,), {

    'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
      'DESCRIPTOR' : _FINALIZEMODELVERSION_RESPONSE,
      '__module__' : 'unity_catalog_oss_messages_pb2'
      # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.FinalizeModelVersion.Response)
      })
    ,
    'DESCRIPTOR' : _FINALIZEMODELVERSION,
    '__module__' : 'unity_catalog_oss_messages_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.FinalizeModelVersion)
    })
  _sym_db.RegisterMessage(FinalizeModelVersion)
  _sym_db.RegisterMessage(FinalizeModelVersion.Response)

  GetModelVersion = _reflection.GeneratedProtocolMessageType('GetModelVersion', (_message.Message,), {

    'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
      'DESCRIPTOR' : _GETMODELVERSION_RESPONSE,
      '__module__' : 'unity_catalog_oss_messages_pb2'
      # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.GetModelVersion.Response)
      })
    ,
    'DESCRIPTOR' : _GETMODELVERSION,
    '__module__' : 'unity_catalog_oss_messages_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.GetModelVersion)
    })
  _sym_db.RegisterMessage(GetModelVersion)
  _sym_db.RegisterMessage(GetModelVersion.Response)

  UpdateModelVersion = _reflection.GeneratedProtocolMessageType('UpdateModelVersion', (_message.Message,), {

    'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
      'DESCRIPTOR' : _UPDATEMODELVERSION_RESPONSE,
      '__module__' : 'unity_catalog_oss_messages_pb2'
      # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.UpdateModelVersion.Response)
      })
    ,
    'DESCRIPTOR' : _UPDATEMODELVERSION,
    '__module__' : 'unity_catalog_oss_messages_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.UpdateModelVersion)
    })
  _sym_db.RegisterMessage(UpdateModelVersion)
  _sym_db.RegisterMessage(UpdateModelVersion.Response)

  if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\'com.databricks.api.proto.managedcatalog\240\001\001\342?\002\020\001'
    _DELETEREGISTEREDMODEL.fields_by_name['full_name']._options = None
    _DELETEREGISTEREDMODEL.fields_by_name['full_name']._serialized_options = b'\370\206\031\001'
    _GETREGISTEREDMODEL_RESPONSE.fields_by_name['registered_model_info']._options = None
    _GETREGISTEREDMODEL_RESPONSE.fields_by_name['registered_model_info']._serialized_options = b'\200\207\031\001'
    _GETREGISTEREDMODEL.fields_by_name['full_name']._options = None
    _GETREGISTEREDMODEL.fields_by_name['full_name']._serialized_options = b'\370\206\031\001'
    _FINALIZEMODELVERSION_RESPONSE.fields_by_name['model_version_info']._options = None
    _FINALIZEMODELVERSION_RESPONSE.fields_by_name['model_version_info']._serialized_options = b'\200\207\031\001'
    _GETMODELVERSION_RESPONSE.fields_by_name['model_version_info']._options = None
    _GETMODELVERSION_RESPONSE.fields_by_name['model_version_info']._serialized_options = b'\200\207\031\001'
    _MODELVERSIONSTATUS._serialized_start=1997
    _MODELVERSIONSTATUS._serialized_end=2113
    _REGISTEREDMODELINFO._serialized_start=99
    _REGISTEREDMODELINFO._serialized_end=352
    _CREATEREGISTEREDMODEL._serialized_start=355
    _CREATEREGISTEREDMODEL._serialized_end=563
    _CREATEREGISTEREDMODEL_RESPONSE._serialized_start=480
    _CREATEREGISTEREDMODEL_RESPONSE._serialized_end=563
    _DELETEREGISTEREDMODEL._serialized_start=565
    _DELETEREGISTEREDMODEL._serialized_end=640
    _DELETEREGISTEREDMODEL_RESPONSE._serialized_start=480
    _DELETEREGISTEREDMODEL_RESPONSE._serialized_end=490
    _GETREGISTEREDMODEL._serialized_start=643
    _GETREGISTEREDMODEL._serialized_end=779
    _GETREGISTEREDMODEL_RESPONSE._serialized_start=690
    _GETREGISTEREDMODEL_RESPONSE._serialized_end=779
    _UPDATEREGISTEREDMODEL._serialized_start=782
    _UPDATEREGISTEREDMODEL._serialized_end=944
    _UPDATEREGISTEREDMODEL_RESPONSE._serialized_start=480
    _UPDATEREGISTEREDMODEL_RESPONSE._serialized_end=563
    _MODELVERSIONINFO._serialized_start=947
    _MODELVERSIONINFO._serialized_end=1269
    _CREATEMODELVERSION._serialized_start=1272
    _CREATEMODELVERSION._serialized_end=1483
    _CREATEMODELVERSION_RESPONSE._serialized_start=1406
    _CREATEMODELVERSION_RESPONSE._serialized_end=1483
    _DELETEMODELVERSION._serialized_start=1485
    _DELETEMODELVERSION._serialized_end=1553
    _DELETEMODELVERSION_RESPONSE._serialized_start=480
    _DELETEMODELVERSION_RESPONSE._serialized_end=490
    _FINALIZEMODELVERSION._serialized_start=1556
    _FINALIZEMODELVERSION._serialized_end=1699
    _FINALIZEMODELVERSION_RESPONSE._serialized_start=1616
    _FINALIZEMODELVERSION_RESPONSE._serialized_end=1699
    _GETMODELVERSION._serialized_start=1702
    _GETMODELVERSION._serialized_end=1840
    _GETMODELVERSION_RESPONSE._serialized_start=1616
    _GETMODELVERSION_RESPONSE._serialized_end=1699
    _UPDATEMODELVERSION._serialized_start=1843
    _UPDATEMODELVERSION._serialized_end=1995
    _UPDATEMODELVERSION_RESPONSE._serialized_start=1406
    _UPDATEMODELVERSION_RESPONSE._serialized_end=1483
  # @@protoc_insertion_point(module_scope)

