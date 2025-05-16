from __future__ import annotations as _annotations

from fhir.resources.R4B.allergyintolerance import AllergyIntolerance, AllergyIntoleranceReaction

"""
Profile: https://www.ehealth.fgov.be/standards/fhir/allergy/StructureDefinition/be-allergyintolerance
Release: STU1
Version: 1.1.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from fhir.resources.R4B import backboneelement, domainresource, fhirtypes
from fhir.resources.BE.STU1.fhirtypes import AllergyIntoleranceReactionType

class BeAllergyIntolerance(AllergyIntolerance):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Allergy or Intolerance (generally: Risk of adverse reaction to a substance).
    Risk of harmful or undesirable, physiological response which is unique to
    an individual and associated with exposure to a substance.
    """

    __resource_type__ = "AllergyIntolerance"
    
    reaction: typing.List[AllergyIntoleranceReactionType] | None = Field(  # type: ignore
        None,
        alias="reaction",
        title="Adverse Reaction Events linked to exposure to substance",
        description=(
            "Details about each adverse reaction event linked to exposure to the "
            "identified substance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )


class BeAllergyIntoleranceReaction(AllergyIntoleranceReaction):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Adverse Reaction Events linked to exposure to substance.
    Details about each adverse reaction event linked to exposure to the
    identified substance.
    """

    __resource_type__ = "AllergyIntoleranceReaction"
