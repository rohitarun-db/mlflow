
import google.protobuf
from packaging.version import Version
if Version(google.protobuf.__version__).major >= 5:
  # -*- coding: utf-8 -*-
  # Generated by the protocol buffer compiler.  DO NOT EDIT!
  # source: unity_catalog_oss_service.proto
  # Protobuf Python Version: 5.26.0
  """Generated protocol buffer code."""
  from google.protobuf import descriptor as _descriptor
  from google.protobuf import descriptor_pool as _descriptor_pool
  from google.protobuf import symbol_database as _symbol_database
  from google.protobuf.internal import builder as _builder
  # @@protoc_insertion_point(imports)

  _sym_db = _symbol_database.Default()


  from . import databricks_pb2 as databricks__pb2
  from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2
  from . import unity_catalog_oss_messages_pb2 as unity_catalog_oss_messages_pb2


  DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1funity_catalog_oss_service.proto\x12\x13mlflow.unitycatalog\x1a\x10\x64\x61tabricks.proto\x1a\x15scalapb/scalapb.proto\x1a unity_catalog_oss_messages.proto2\xb8\x03\n\x13UnityCatalogService\x12\xa5\x01\n\x15\x63reateRegisteredModel\x12*.mlflow.unitycatalog.CreateRegisteredModel\x1a\x33.mlflow.unitycatalog.CreateRegisteredModel.Response\"+\xf2\x86\x19\'\n#\n\x04POST\x12\x15/unity-catalog/models\x1a\x04\x08\x02\x10\x01\x10\x01\x12\xf8\x01\n\'generateTemporaryModelVersionCredential\x12<.mlflow.unitycatalog.GenerateTemporaryModelVersionCredential\x1a\x45.mlflow.unitycatalog.GenerateTemporaryModelVersionCredential.Response\"H\xf2\x86\x19\x44\n@\n\x04POST\x12\x32/unity-catalog/temporary-model-version-credentials\x1a\x04\x08\x02\x10\x01\x10\x03\x42\x34\n\'com.databricks.api.proto.managedcatalog\x90\x01\x01\xa0\x01\x01\xe2?\x02\x10\x01')

  _globals = globals()
  _builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
  _builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'unity_catalog_oss_service_pb2', _globals)
  if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\'com.databricks.api.proto.managedcatalog\220\001\001\240\001\001\342?\002\020\001'
    _globals['_UNITYCATALOGSERVICE'].methods_by_name['createRegisteredModel']._loaded_options = None
    _globals['_UNITYCATALOGSERVICE'].methods_by_name['createRegisteredModel']._serialized_options = b'\362\206\031\'\n#\n\004POST\022\025/unity-catalog/models\032\004\010\002\020\001\020\001'
    _globals['_UNITYCATALOGSERVICE'].methods_by_name['generateTemporaryModelVersionCredential']._loaded_options = None
    _globals['_UNITYCATALOGSERVICE'].methods_by_name['generateTemporaryModelVersionCredential']._serialized_options = b'\362\206\031D\n@\n\004POST\0222/unity-catalog/temporary-model-version-credentials\032\004\010\002\020\001\020\003'
    _globals['_UNITYCATALOGSERVICE']._serialized_start=132
    _globals['_UNITYCATALOGSERVICE']._serialized_end=572
  _builder.BuildServices(DESCRIPTOR, 'unity_catalog_oss_service_pb2', _globals)
  # @@protoc_insertion_point(module_scope)

else:
  # -*- coding: utf-8 -*-
  # Generated by the protocol buffer compiler.  DO NOT EDIT!
  # source: unity_catalog_oss_service.proto
  """Generated protocol buffer code."""
  from google.protobuf import descriptor as _descriptor
  from google.protobuf import descriptor_pool as _descriptor_pool
  from google.protobuf import message as _message
  from google.protobuf import reflection as _reflection
  from google.protobuf import symbol_database as _symbol_database
  from google.protobuf import service as _service
  from google.protobuf import service_reflection
  # @@protoc_insertion_point(imports)

  _sym_db = _symbol_database.Default()


  from . import databricks_pb2 as databricks__pb2
  from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2
  from . import unity_catalog_oss_messages_pb2 as unity_catalog_oss_messages_pb2


  DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1funity_catalog_oss_service.proto\x12\x13mlflow.unitycatalog\x1a\x10\x64\x61tabricks.proto\x1a\x15scalapb/scalapb.proto\x1a unity_catalog_oss_messages.proto2\xb8\x03\n\x13UnityCatalogService\x12\xa5\x01\n\x15\x63reateRegisteredModel\x12*.mlflow.unitycatalog.CreateRegisteredModel\x1a\x33.mlflow.unitycatalog.CreateRegisteredModel.Response\"+\xf2\x86\x19\'\n#\n\x04POST\x12\x15/unity-catalog/models\x1a\x04\x08\x02\x10\x01\x10\x01\x12\xf8\x01\n\'generateTemporaryModelVersionCredential\x12<.mlflow.unitycatalog.GenerateTemporaryModelVersionCredential\x1a\x45.mlflow.unitycatalog.GenerateTemporaryModelVersionCredential.Response\"H\xf2\x86\x19\x44\n@\n\x04POST\x12\x32/unity-catalog/temporary-model-version-credentials\x1a\x04\x08\x02\x10\x01\x10\x03\x42\x34\n\'com.databricks.api.proto.managedcatalog\x90\x01\x01\xa0\x01\x01\xe2?\x02\x10\x01')



  _UNITYCATALOGSERVICE = DESCRIPTOR.services_by_name['UnityCatalogService']
  if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\'com.databricks.api.proto.managedcatalog\220\001\001\240\001\001\342?\002\020\001'
    _UNITYCATALOGSERVICE.methods_by_name['createRegisteredModel']._options = None
    _UNITYCATALOGSERVICE.methods_by_name['createRegisteredModel']._serialized_options = b'\362\206\031\'\n#\n\004POST\022\025/unity-catalog/models\032\004\010\002\020\001\020\001'
    _UNITYCATALOGSERVICE.methods_by_name['generateTemporaryModelVersionCredential']._options = None
    _UNITYCATALOGSERVICE.methods_by_name['generateTemporaryModelVersionCredential']._serialized_options = b'\362\206\031D\n@\n\004POST\0222/unity-catalog/temporary-model-version-credentials\032\004\010\002\020\001\020\003'
    _UNITYCATALOGSERVICE._serialized_start=132
    _UNITYCATALOGSERVICE._serialized_end=572
  UnityCatalogService = service_reflection.GeneratedServiceType('UnityCatalogService', (_service.Service,), dict(
    DESCRIPTOR = _UNITYCATALOGSERVICE,
    __module__ = 'unity_catalog_oss_service_pb2'
    ))

  UnityCatalogService_Stub = service_reflection.GeneratedServiceStubType('UnityCatalogService_Stub', (UnityCatalogService,), dict(
    DESCRIPTOR = _UNITYCATALOGSERVICE,
    __module__ = 'unity_catalog_oss_service_pb2'
    ))


  # @@protoc_insertion_point(module_scope)

