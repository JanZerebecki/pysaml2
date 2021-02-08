import inspect

from xmlschema import XMLSchema as _XMLSchema
from xmlschema.exceptions import XMLSchemaException as XMLSchemaError

import saml2.data.schemas as _data_schemas

def _create_xml_schema_validator(source, **kwargs):
    kwargs = {
        **kwargs,
        "validation": "strict",
        "locations": _locations,
        "base_url": source,
        "allow": "sandbox",
        "use_fallback": False,
    }
    return _XMLSchema(source, **kwargs)


def _resource_path_str(package, resource):
    inspect.getabsfile(_data_schemas)


_path_schema_xml = _resource_path_str(_data_schemas, "xml.xsd")
_path_schema_envelope = _resource_path_str(_data_schemas, "envelope.xsd")
_path_schema_xenc = _resource_path_str(_data_schemas, "xenc-schema.xsd")
_path_schema_xmldsig_core = _resource_path_str(_data_schemas, "xmldsig-core-schema.xsd")
_path_schema_saml_assertion = _resource_path_str(_data_schemas, "saml-schema-assertion-2.0.xsd")
_path_schema_saml_metadata = _resource_path_str(_data_schemas, "saml-schema-metadata-2.0.xsd")
_path_schema_saml_protocol = _resource_path_str(_data_schemas, "saml-schema-protocol-2.0.xsd")

_locations = {
    "http://www.w3.org/XML/1998/namespace": _path_schema_xml,
    "http://schemas.xmlsoap.org/soap/envelope/": _path_schema_envelope,
    "http://www.w3.org/2001/04/xmlenc#": _path_schema_xenc,
    "http://www.w3.org/2000/09/xmldsig#": _path_schema_xmldsig_core,
    "urn:oasis:names:tc:SAML:2.0:assertion": _path_schema_saml_assertion,
    "urn:oasis:names:tc:SAML:2.0:protocol": _path_schema_saml_protocol,
}

schema_saml_assertion = _create_xml_schema_validator(_resource_path_str(_data_schemas, "saml-schema-assertion-2.0.xsd"))
schema_saml_metadata = _create_xml_schema_validator(_resource_path_str(_data_schemas, "saml-schema-metadata-2.0.xsd"))
schema_saml_protocol = _create_xml_schema_validator(_resource_path_str(_data_schemas, "saml-schema-protocol-2.0.xsd"))


node_to_schema = {
    # AssertionType
    "urn:oasis:names:tc:SAML:2.0:assertion:Assertion": schema_saml_assertion,
    # EntitiesDescriptorType
    "urn:oasis:names:tc:SAML:2.0:metadata:EntitiesDescriptor": schema_saml_metadata,
    # EntityDescriptorType
    "urn:oasis:names:tc:SAML:2.0:metadata:EntityDescriptor": schema_saml_metadata,
    # RequestAbstractType
    "urn:oasis:names:tc:SAML:2.0:protocol:AssertionIDRequest": schema_saml_protocol,
    "urn:oasis:names:tc:SAML:2.0:protocol:SubjectQuery": schema_saml_protocol,
    "urn:oasis:names:tc:SAML:2.0:protocol:AuthnRequest": schema_saml_protocol,
    "urn:oasis:names:tc:SAML:2.0:protocol:ArtifactResolve": schema_saml_protocol,
    "urn:oasis:names:tc:SAML:2.0:protocol:ManageNameIDRequest": schema_saml_protocol,
    "urn:oasis:names:tc:SAML:2.0:protocol:LogoutRequest": schema_saml_protocol,
    "urn:oasis:names:tc:SAML:2.0:protocol:NameIDMappingRequest": schema_saml_protocol,
    # StatusResponseType
    "urn:oasis:names:tc:SAML:2.0:protocol:Response": schema_saml_protocol,
    "urn:oasis:names:tc:SAML:2.0:protocol:ArtifactResponse": schema_saml_protocol,
    "urn:oasis:names:tc:SAML:2.0:protocol:ManageNameIDResponse": schema_saml_protocol,
    "urn:oasis:names:tc:SAML:2.0:protocol:LogoutResponse": schema_saml_protocol,
    "urn:oasis:names:tc:SAML:2.0:protocol:NameIDMappingResponse": schema_saml_protocol,
}
