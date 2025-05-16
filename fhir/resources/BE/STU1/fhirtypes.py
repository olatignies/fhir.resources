from __future__ import annotations as _annotations

from fhir_core.types import (
    Base64BinaryType,
    BooleanType,
    CanonicalType,
    CodeType,
    DateTimeType,
    DateType,
    DecimalType,
    IdType,
    InstantType,
    Integer64Type,
    IntegerType,
    MarkdownType,
    OidType,
    PositiveIntType,
    StringType,
    TimeType,
    UnsignedIntType,
    UriType,
    UrlType,
    UuidType,
    XhtmlType,
    create_fhir_element_or_resource_type,
    create_fhir_type,
)

from fhir.resources.R4B.fhirtypes import AddressType, PatientType

__author__ = "Olivier Latignies"
__email__ = "olatignies@gmail.com"

AllergyIntoleranceType = create_fhir_type(
    "AllergyIntoleranceType", "fhir.resources.BE.STU1.allergyintolerance.BeAllergyIntolerance"
)

AllergyIntoleranceReactionType = create_fhir_type(
    "AllergyIntoleranceReactionType", "fhir.resources.BE.STU1.allergyintolerance.BeAllergyIntoleranceReaction"
)

ReferenceType = create_fhir_type(
    "ReferenceType", "fhir.resources.R4B.reference.Reference"
)

IdentifierType = create_fhir_type(
    "IdentifierType", "fhir.resources.R4B.identifier.Identifier"
)

CodeableConceptType = create_fhir_type(
    "CodeableConceptType", "fhir.resources.R4B.codeableconcept.CodeableConcept"
)

NIHDIType = create_fhir_type(
    "NIHDIType", "fhir.resources.BE.STU1.nihdi.NIHDI"
)

class CBEType(IdentifierType):
    __resource_type__ = "CBE"

class SSINType(IdentifierType):
    __resource_type__ = "SSIN"

class EHPType(IdentifierType):
    __resource_type__ = "EHP"

class CDHCPARTYType(CodeableConceptType):
    __resource_type__ = "CDHCPARTY"

BeAddressType = create_fhir_type("AddressType", "fhir.resources.BE.STU1.address.BeAddress")

class BePatientType(PatientType):
    __resource_type__ = "Patient"

__all__ = [
    "ReferenceType",
    "IdentifierType",
    "CodeableConceptType",
    "NIHDIType",
    "CBEType",
    "SSINType",
    "EHPType",
    "CDHCPARTYType",
    "AllergyIntoleranceType",
    "BeAddressType",
    "BePatientType",
]
