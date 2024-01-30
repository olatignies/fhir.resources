# -*- coding: utf-8 -*-
"""
Profile: https://www.ehealth.fgov.be/standards/fhir/core/StructureDefinition/be-vaccination
Release: STU1
Version: 1.0.3
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""

from pydantic.v1 import Field

from fhir.resources.R4B.immunization import Immunization
from fhir.resources.R4B.fhirtypes import ReferenceType, IdentifierType

class BeVaccination(Immunization):

    resource_type = Field("Immunization", const=True)

    patient: ReferenceType = Field(
        ...,
        alias="patient",
        title="Who was immunized BE",
        description="The patient who either received or did not receive the immunization.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["BePatient"],
    )

    # identifier: IdentifierType = Field(
    #     None,
    #     alias="identifier",
    #     title="Business identifier",
    #     description="A unique identifier assigned to this immunization record.",
    #     # if property is element of this resource.
    #     element_property=True,
    # )
