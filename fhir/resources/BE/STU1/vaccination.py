# -*- coding: utf-8 -*-
"""
Profile: https://www.ehealth.fgov.be/standards/fhir/core/StructureDefinition/be-vaccination
Release: STU1
Version: 1.0.3
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""

import typing

from pydantic import Field, model_validator

from fhir.resources.R4B.immunization import Immunization
from fhir.resources.R4B.fhirtypes import ReferenceType, ExtensionType

class BeVaccination(Immunization):

    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Immunization event information.
    Describes the event of a patient being administered a vaccine or a record
    of an immunization as reported by a patient, a clinician or another party.
    """

    __resource_type__ = "Immunization"

    @model_validator(mode="before")
    @classmethod
    def normalize_list_fields(cls, values: dict) -> dict:
        # The BE vaccination server sends `identifier` as a single object
        # instead of an array, violating FHIR JSON spec (cardinality 0..*).
        if isinstance(values.get("identifier"), dict):
            values["identifier"] = [values["identifier"]]
        return values

    extension: typing.List[ExtensionType] | None = Field(  # type: ignore
        None,
        alias="extension",
        title="Additional content defined by implementations",
        description=(
            "May be used to represent additional information that is not part of "
            "the basic definition of the resource. To make the use of extensions "
            "safe and managable, there is a strict set of governance applied to the"
            " definition and use of extensions. Though any implementer can define "
            "an extension, there is a set of requirements that SHALL be met as part"
            " of the definition of the extension."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
