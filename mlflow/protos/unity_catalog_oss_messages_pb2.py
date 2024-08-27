
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


  DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n unity_catalog_oss_messages.proto\x12\x13mlflow.unitycatalog\x1a\x15scalapb/scalapb.proto\x1a\x10\x64\x61tabricks.proto\"\xfd\x01\n\x13RegisteredModelInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61talog_name\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t\x12\x0f\n\x07\x63omment\x18\x05 \x01(\t\x12\x18\n\x10storage_location\x18\x06 \x01(\t\x12\x11\n\tfull_name\x18\t \x01(\t\x12\x12\n\ncreated_at\x18\x0b \x01(\x03\x12\x12\n\ncreated_by\x18\x0c \x01(\t\x12\x12\n\nupdated_at\x18\r \x01(\x03\x12\x12\n\nupdated_by\x18\x0e \x01(\t\x12\n\n\x02id\x18\x12 \x01(\t\x12\x13\n\x0b\x62rowse_only\x18\x15 \x01(\x08\"\xd0\x01\n\x15\x43reateRegisteredModel\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61talog_name\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t\x12\x0f\n\x07\x63omment\x18\x05 \x01(\t\x12\x18\n\x10storage_location\x18\x06 \x01(\t\x1aS\n\x08Response\x12G\n\x15registered_model_info\x18\x01 \x01(\x0b\x32(.mlflow.unitycatalog.RegisteredModelInfo\"E\n\x15\x44\x65leteRegisteredModel\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\r\n\x05\x66orce\x18\x02 \x01(\x08\x1a\n\n\x08Response\"\x82\x01\n\x12GetRegisteredModel\x12\x17\n\tfull_name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x1aS\n\x08Response\x12G\n\x15registered_model_info\x18\x01 \x01(\x0b\x32(.mlflow.unitycatalog.RegisteredModelInfo\"\xa2\x01\n\x15UpdateRegisteredModel\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x10\n\x08new_name\x18\x03 \x01(\t\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\x1aS\n\x08Response\x12G\n\x15registered_model_info\x18\x01 \x01(\x0b\x32(.mlflow.unitycatalog.RegisteredModelInfo\"\xc2\x02\n\x10ModelVersionInfo\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61talog_name\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t\x12\x0e\n\x06source\x18\x05 \x01(\t\x12\x0f\n\x07\x63omment\x18\x04 \x01(\t\x12\x0e\n\x06run_id\x18\x06 \x01(\t\x12\x37\n\x06status\x18\x08 \x01(\x0e\x32\'.mlflow.unitycatalog.ModelVersionStatus\x12\x0f\n\x07version\x18\t \x01(\x03\x12\x18\n\x10storage_location\x18\n \x01(\t\x12\x12\n\ncreated_at\x18\x0c \x01(\x03\x12\x12\n\ncreated_by\x18\r \x01(\t\x12\x12\n\nupdated_at\x18\x0e \x01(\x03\x12\x12\n\nupdated_by\x18\x0f \x01(\t\x12\n\n\x02id\x18\x10 \x01(\t\"\xd3\x01\n\x12\x43reateModelVersion\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61talog_name\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t\x12\x0e\n\x06source\x18\x04 \x01(\t\x12\x0e\n\x06run_id\x18\x05 \x01(\t\x12\x0f\n\x07\x63omment\x18\x06 \x01(\t\x1aM\n\x08Response\x12\x41\n\x12model_version_info\x18\x01 \x01(\x0b\x32%.mlflow.unitycatalog.ModelVersionInfo\"D\n\x12\x44\x65leteModelVersion\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x1a\n\n\x08Response\"\x89\x01\n\x14\x46inalizeModelVersion\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x1aM\n\x08Response\x12\x41\n\x12model_version_info\x18\x01 \x01(\x0b\x32%.mlflow.unitycatalog.ModelVersionInfo\"\x84\x01\n\x0fGetModelVersion\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x1aM\n\x08Response\x12\x41\n\x12model_version_info\x18\x01 \x01(\x0b\x32%.mlflow.unitycatalog.ModelVersionInfo\"\x98\x01\n\x12UpdateModelVersion\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\x1aM\n\x08Response\x12\x41\n\x12model_version_info\x18\x01 \x01(\x0b\x32%.mlflow.unitycatalog.ModelVersionInfo\"\x83\x01\n\x14TemporaryCredentials\x12\x43\n\x14\x61ws_temp_credentials\x18\x02 \x01(\x0b\x32#.mlflow.unitycatalog.AwsCredentialsH\x00\x12\x17\n\x0f\x65xpiration_time\x18\x01 \x01(\x03\x42\r\n\x0b\x63redentials\"Y\n\x0e\x41wsCredentials\x12\x15\n\raccess_key_id\x18\x01 \x01(\t\x12\x19\n\x11secret_access_key\x18\x02 \x01(\t\x12\x15\n\rsession_token\x18\x03 \x01(\t\"\x84\x02\n\'GenerateTemporaryModelVersionCredential\x12\x14\n\x0c\x63\x61talog_name\x18\x01 \x01(\t\x12\x13\n\x0bschema_name\x18\x02 \x01(\t\x12\x12\n\nmodel_name\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\x03\x12=\n\toperation\x18\x05 \x01(\x0e\x32*.mlflow.unitycatalog.ModelVersionOperation\x1aJ\n\x08Response\x12>\n\x0b\x63redentials\x18\x01 \x01(\x0b\x32).mlflow.unitycatalog.TemporaryCredentials*t\n\x12ModelVersionStatus\x12 \n\x1cMODEL_VERSION_STATUS_UNKNOWN\x10\x00\x12\x18\n\x14PENDING_REGISTRATION\x10\x01\x12\x17\n\x13\x46\x41ILED_REGISTRATION\x10\x02\x12\t\n\x05READY\x10\x03*r\n\x15ModelVersionOperation\x12#\n\x1fUNKNOWN_MODEL_VERSION_OPERATION\x10\x00\x12\x16\n\x12READ_MODEL_VERSION\x10\x01\x12\x1c\n\x18READ_WRITE_MODEL_VERSION\x10\x02\x42\x31\n\'com.databricks.api.proto.managedcatalog\xa0\x01\x01\xe2?\x02\x10\x01')

  _globals = globals()
  _builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
  _builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'unity_catalog_oss_messages_pb2', _globals)
  if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\'com.databricks.api.proto.managedcatalog\240\001\001\342?\002\020\001'
    _globals['_GETREGISTEREDMODEL'].fields_by_name['full_name']._loaded_options = None
    _globals['_GETREGISTEREDMODEL'].fields_by_name['full_name']._serialized_options = b'\370\206\031\001'
    _globals['_MODELVERSIONSTATUS']._serialized_start=2461
    _globals['_MODELVERSIONSTATUS']._serialized_end=2577
    _globals['_MODELVERSIONOPERATION']._serialized_start=2579
    _globals['_MODELVERSIONOPERATION']._serialized_end=2693
    _globals['_REGISTEREDMODELINFO']._serialized_start=99
    _globals['_REGISTEREDMODELINFO']._serialized_end=352
    _globals['_CREATEREGISTEREDMODEL']._serialized_start=355
    _globals['_CREATEREGISTEREDMODEL']._serialized_end=563
    _globals['_CREATEREGISTEREDMODEL_RESPONSE']._serialized_start=480
    _globals['_CREATEREGISTEREDMODEL_RESPONSE']._serialized_end=563
    _globals['_DELETEREGISTEREDMODEL']._serialized_start=565
    _globals['_DELETEREGISTEREDMODEL']._serialized_end=634
    _globals['_DELETEREGISTEREDMODEL_RESPONSE']._serialized_start=480
    _globals['_DELETEREGISTEREDMODEL_RESPONSE']._serialized_end=490
    _globals['_GETREGISTEREDMODEL']._serialized_start=637
    _globals['_GETREGISTEREDMODEL']._serialized_end=767
    _globals['_GETREGISTEREDMODEL_RESPONSE']._serialized_start=480
    _globals['_GETREGISTEREDMODEL_RESPONSE']._serialized_end=563
    _globals['_UPDATEREGISTEREDMODEL']._serialized_start=770
    _globals['_UPDATEREGISTEREDMODEL']._serialized_end=932
    _globals['_UPDATEREGISTEREDMODEL_RESPONSE']._serialized_start=480
    _globals['_UPDATEREGISTEREDMODEL_RESPONSE']._serialized_end=563
    _globals['_MODELVERSIONINFO']._serialized_start=935
    _globals['_MODELVERSIONINFO']._serialized_end=1257
    _globals['_CREATEMODELVERSION']._serialized_start=1260
    _globals['_CREATEMODELVERSION']._serialized_end=1471
    _globals['_CREATEMODELVERSION_RESPONSE']._serialized_start=1394
    _globals['_CREATEMODELVERSION_RESPONSE']._serialized_end=1471
    _globals['_DELETEMODELVERSION']._serialized_start=1473
    _globals['_DELETEMODELVERSION']._serialized_end=1541
    _globals['_DELETEMODELVERSION_RESPONSE']._serialized_start=480
    _globals['_DELETEMODELVERSION_RESPONSE']._serialized_end=490
    _globals['_FINALIZEMODELVERSION']._serialized_start=1544
    _globals['_FINALIZEMODELVERSION']._serialized_end=1681
    _globals['_FINALIZEMODELVERSION_RESPONSE']._serialized_start=1394
    _globals['_FINALIZEMODELVERSION_RESPONSE']._serialized_end=1471
    _globals['_GETMODELVERSION']._serialized_start=1684
    _globals['_GETMODELVERSION']._serialized_end=1816
    _globals['_GETMODELVERSION_RESPONSE']._serialized_start=1394
    _globals['_GETMODELVERSION_RESPONSE']._serialized_end=1471
    _globals['_UPDATEMODELVERSION']._serialized_start=1819
    _globals['_UPDATEMODELVERSION']._serialized_end=1971
    _globals['_UPDATEMODELVERSION_RESPONSE']._serialized_start=1394
    _globals['_UPDATEMODELVERSION_RESPONSE']._serialized_end=1471
    _globals['_TEMPORARYCREDENTIALS']._serialized_start=1974
    _globals['_TEMPORARYCREDENTIALS']._serialized_end=2105
    _globals['_AWSCREDENTIALS']._serialized_start=2107
    _globals['_AWSCREDENTIALS']._serialized_end=2196
    _globals['_GENERATETEMPORARYMODELVERSIONCREDENTIAL']._serialized_start=2199
    _globals['_GENERATETEMPORARYMODELVERSIONCREDENTIAL']._serialized_end=2459
    _globals['_GENERATETEMPORARYMODELVERSIONCREDENTIAL_RESPONSE']._serialized_start=2385
    _globals['_GENERATETEMPORARYMODELVERSIONCREDENTIAL_RESPONSE']._serialized_end=2459
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


  DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n unity_catalog_oss_messages.proto\x12\x13mlflow.unitycatalog\x1a\x15scalapb/scalapb.proto\x1a\x10\x64\x61tabricks.proto\"\xfd\x01\n\x13RegisteredModelInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61talog_name\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t\x12\x0f\n\x07\x63omment\x18\x05 \x01(\t\x12\x18\n\x10storage_location\x18\x06 \x01(\t\x12\x11\n\tfull_name\x18\t \x01(\t\x12\x12\n\ncreated_at\x18\x0b \x01(\x03\x12\x12\n\ncreated_by\x18\x0c \x01(\t\x12\x12\n\nupdated_at\x18\r \x01(\x03\x12\x12\n\nupdated_by\x18\x0e \x01(\t\x12\n\n\x02id\x18\x12 \x01(\t\x12\x13\n\x0b\x62rowse_only\x18\x15 \x01(\x08\"\xd0\x01\n\x15\x43reateRegisteredModel\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61talog_name\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t\x12\x0f\n\x07\x63omment\x18\x05 \x01(\t\x12\x18\n\x10storage_location\x18\x06 \x01(\t\x1aS\n\x08Response\x12G\n\x15registered_model_info\x18\x01 \x01(\x0b\x32(.mlflow.unitycatalog.RegisteredModelInfo\"E\n\x15\x44\x65leteRegisteredModel\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\r\n\x05\x66orce\x18\x02 \x01(\x08\x1a\n\n\x08Response\"\x82\x01\n\x12GetRegisteredModel\x12\x17\n\tfull_name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x1aS\n\x08Response\x12G\n\x15registered_model_info\x18\x01 \x01(\x0b\x32(.mlflow.unitycatalog.RegisteredModelInfo\"\xa2\x01\n\x15UpdateRegisteredModel\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x10\n\x08new_name\x18\x03 \x01(\t\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\x1aS\n\x08Response\x12G\n\x15registered_model_info\x18\x01 \x01(\x0b\x32(.mlflow.unitycatalog.RegisteredModelInfo\"\xc2\x02\n\x10ModelVersionInfo\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61talog_name\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t\x12\x0e\n\x06source\x18\x05 \x01(\t\x12\x0f\n\x07\x63omment\x18\x04 \x01(\t\x12\x0e\n\x06run_id\x18\x06 \x01(\t\x12\x37\n\x06status\x18\x08 \x01(\x0e\x32\'.mlflow.unitycatalog.ModelVersionStatus\x12\x0f\n\x07version\x18\t \x01(\x03\x12\x18\n\x10storage_location\x18\n \x01(\t\x12\x12\n\ncreated_at\x18\x0c \x01(\x03\x12\x12\n\ncreated_by\x18\r \x01(\t\x12\x12\n\nupdated_at\x18\x0e \x01(\x03\x12\x12\n\nupdated_by\x18\x0f \x01(\t\x12\n\n\x02id\x18\x10 \x01(\t\"\xd3\x01\n\x12\x43reateModelVersion\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61talog_name\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t\x12\x0e\n\x06source\x18\x04 \x01(\t\x12\x0e\n\x06run_id\x18\x05 \x01(\t\x12\x0f\n\x07\x63omment\x18\x06 \x01(\t\x1aM\n\x08Response\x12\x41\n\x12model_version_info\x18\x01 \x01(\x0b\x32%.mlflow.unitycatalog.ModelVersionInfo\"D\n\x12\x44\x65leteModelVersion\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x1a\n\n\x08Response\"\x89\x01\n\x14\x46inalizeModelVersion\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x1aM\n\x08Response\x12\x41\n\x12model_version_info\x18\x01 \x01(\x0b\x32%.mlflow.unitycatalog.ModelVersionInfo\"\x84\x01\n\x0fGetModelVersion\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x1aM\n\x08Response\x12\x41\n\x12model_version_info\x18\x01 \x01(\x0b\x32%.mlflow.unitycatalog.ModelVersionInfo\"\x98\x01\n\x12UpdateModelVersion\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\x1aM\n\x08Response\x12\x41\n\x12model_version_info\x18\x01 \x01(\x0b\x32%.mlflow.unitycatalog.ModelVersionInfo\"\x83\x01\n\x14TemporaryCredentials\x12\x43\n\x14\x61ws_temp_credentials\x18\x02 \x01(\x0b\x32#.mlflow.unitycatalog.AwsCredentialsH\x00\x12\x17\n\x0f\x65xpiration_time\x18\x01 \x01(\x03\x42\r\n\x0b\x63redentials\"Y\n\x0e\x41wsCredentials\x12\x15\n\raccess_key_id\x18\x01 \x01(\t\x12\x19\n\x11secret_access_key\x18\x02 \x01(\t\x12\x15\n\rsession_token\x18\x03 \x01(\t\"\x84\x02\n\'GenerateTemporaryModelVersionCredential\x12\x14\n\x0c\x63\x61talog_name\x18\x01 \x01(\t\x12\x13\n\x0bschema_name\x18\x02 \x01(\t\x12\x12\n\nmodel_name\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\x03\x12=\n\toperation\x18\x05 \x01(\x0e\x32*.mlflow.unitycatalog.ModelVersionOperation\x1aJ\n\x08Response\x12>\n\x0b\x63redentials\x18\x01 \x01(\x0b\x32).mlflow.unitycatalog.TemporaryCredentials*t\n\x12ModelVersionStatus\x12 \n\x1cMODEL_VERSION_STATUS_UNKNOWN\x10\x00\x12\x18\n\x14PENDING_REGISTRATION\x10\x01\x12\x17\n\x13\x46\x41ILED_REGISTRATION\x10\x02\x12\t\n\x05READY\x10\x03*r\n\x15ModelVersionOperation\x12#\n\x1fUNKNOWN_MODEL_VERSION_OPERATION\x10\x00\x12\x16\n\x12READ_MODEL_VERSION\x10\x01\x12\x1c\n\x18READ_WRITE_MODEL_VERSION\x10\x02\x42\x31\n\'com.databricks.api.proto.managedcatalog\xa0\x01\x01\xe2?\x02\x10\x01')

  _MODELVERSIONSTATUS = DESCRIPTOR.enum_types_by_name['ModelVersionStatus']
  ModelVersionStatus = enum_type_wrapper.EnumTypeWrapper(_MODELVERSIONSTATUS)
  _MODELVERSIONOPERATION = DESCRIPTOR.enum_types_by_name['ModelVersionOperation']
  ModelVersionOperation = enum_type_wrapper.EnumTypeWrapper(_MODELVERSIONOPERATION)
  MODEL_VERSION_STATUS_UNKNOWN = 0
  PENDING_REGISTRATION = 1
  FAILED_REGISTRATION = 2
  READY = 3
  UNKNOWN_MODEL_VERSION_OPERATION = 0
  READ_MODEL_VERSION = 1
  READ_WRITE_MODEL_VERSION = 2


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
  _TEMPORARYCREDENTIALS = DESCRIPTOR.message_types_by_name['TemporaryCredentials']
  _AWSCREDENTIALS = DESCRIPTOR.message_types_by_name['AwsCredentials']
  _GENERATETEMPORARYMODELVERSIONCREDENTIAL = DESCRIPTOR.message_types_by_name['GenerateTemporaryModelVersionCredential']
  _GENERATETEMPORARYMODELVERSIONCREDENTIAL_RESPONSE = _GENERATETEMPORARYMODELVERSIONCREDENTIAL.nested_types_by_name['Response']
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

  TemporaryCredentials = _reflection.GeneratedProtocolMessageType('TemporaryCredentials', (_message.Message,), {
    'DESCRIPTOR' : _TEMPORARYCREDENTIALS,
    '__module__' : 'unity_catalog_oss_messages_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.TemporaryCredentials)
    })
  _sym_db.RegisterMessage(TemporaryCredentials)

  AwsCredentials = _reflection.GeneratedProtocolMessageType('AwsCredentials', (_message.Message,), {
    'DESCRIPTOR' : _AWSCREDENTIALS,
    '__module__' : 'unity_catalog_oss_messages_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.AwsCredentials)
    })
  _sym_db.RegisterMessage(AwsCredentials)

  GenerateTemporaryModelVersionCredential = _reflection.GeneratedProtocolMessageType('GenerateTemporaryModelVersionCredential', (_message.Message,), {

    'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
      'DESCRIPTOR' : _GENERATETEMPORARYMODELVERSIONCREDENTIAL_RESPONSE,
      '__module__' : 'unity_catalog_oss_messages_pb2'
      # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.GenerateTemporaryModelVersionCredential.Response)
      })
    ,
    'DESCRIPTOR' : _GENERATETEMPORARYMODELVERSIONCREDENTIAL,
    '__module__' : 'unity_catalog_oss_messages_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.GenerateTemporaryModelVersionCredential)
    })
  _sym_db.RegisterMessage(GenerateTemporaryModelVersionCredential)
  _sym_db.RegisterMessage(GenerateTemporaryModelVersionCredential.Response)

  if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\'com.databricks.api.proto.managedcatalog\240\001\001\342?\002\020\001'
    _GETREGISTEREDMODEL.fields_by_name['full_name']._options = None
    _GETREGISTEREDMODEL.fields_by_name['full_name']._serialized_options = b'\370\206\031\001'
    _MODELVERSIONSTATUS._serialized_start=2461
    _MODELVERSIONSTATUS._serialized_end=2577
    _MODELVERSIONOPERATION._serialized_start=2579
    _MODELVERSIONOPERATION._serialized_end=2693
    _REGISTEREDMODELINFO._serialized_start=99
    _REGISTEREDMODELINFO._serialized_end=352
    _CREATEREGISTEREDMODEL._serialized_start=355
    _CREATEREGISTEREDMODEL._serialized_end=563
    _CREATEREGISTEREDMODEL_RESPONSE._serialized_start=480
    _CREATEREGISTEREDMODEL_RESPONSE._serialized_end=563
    _DELETEREGISTEREDMODEL._serialized_start=565
    _DELETEREGISTEREDMODEL._serialized_end=634
    _DELETEREGISTEREDMODEL_RESPONSE._serialized_start=480
    _DELETEREGISTEREDMODEL_RESPONSE._serialized_end=490
    _GETREGISTEREDMODEL._serialized_start=637
    _GETREGISTEREDMODEL._serialized_end=767
    _GETREGISTEREDMODEL_RESPONSE._serialized_start=480
    _GETREGISTEREDMODEL_RESPONSE._serialized_end=563
    _UPDATEREGISTEREDMODEL._serialized_start=770
    _UPDATEREGISTEREDMODEL._serialized_end=932
    _UPDATEREGISTEREDMODEL_RESPONSE._serialized_start=480
    _UPDATEREGISTEREDMODEL_RESPONSE._serialized_end=563
    _MODELVERSIONINFO._serialized_start=935
    _MODELVERSIONINFO._serialized_end=1257
    _CREATEMODELVERSION._serialized_start=1260
    _CREATEMODELVERSION._serialized_end=1471
    _CREATEMODELVERSION_RESPONSE._serialized_start=1394
    _CREATEMODELVERSION_RESPONSE._serialized_end=1471
    _DELETEMODELVERSION._serialized_start=1473
    _DELETEMODELVERSION._serialized_end=1541
    _DELETEMODELVERSION_RESPONSE._serialized_start=480
    _DELETEMODELVERSION_RESPONSE._serialized_end=490
    _FINALIZEMODELVERSION._serialized_start=1544
    _FINALIZEMODELVERSION._serialized_end=1681
    _FINALIZEMODELVERSION_RESPONSE._serialized_start=1394
    _FINALIZEMODELVERSION_RESPONSE._serialized_end=1471
    _GETMODELVERSION._serialized_start=1684
    _GETMODELVERSION._serialized_end=1816
    _GETMODELVERSION_RESPONSE._serialized_start=1394
    _GETMODELVERSION_RESPONSE._serialized_end=1471
    _UPDATEMODELVERSION._serialized_start=1819
    _UPDATEMODELVERSION._serialized_end=1971
    _UPDATEMODELVERSION_RESPONSE._serialized_start=1394
    _UPDATEMODELVERSION_RESPONSE._serialized_end=1471
    _TEMPORARYCREDENTIALS._serialized_start=1974
    _TEMPORARYCREDENTIALS._serialized_end=2105
    _AWSCREDENTIALS._serialized_start=2107
    _AWSCREDENTIALS._serialized_end=2196
    _GENERATETEMPORARYMODELVERSIONCREDENTIAL._serialized_start=2199
    _GENERATETEMPORARYMODELVERSIONCREDENTIAL._serialized_end=2459
    _GENERATETEMPORARYMODELVERSIONCREDENTIAL_RESPONSE._serialized_start=2385
    _GENERATETEMPORARYMODELVERSIONCREDENTIAL_RESPONSE._serialized_end=2459
  # @@protoc_insertion_point(module_scope)

