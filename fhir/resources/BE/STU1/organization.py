# -*- coding: utf-8 -*-
"""
Profile: https://www.ehealth.fgov.be/standards/fhir/core/StructureDefinition/be-organization
Release: STU1
Version: 2.0.1
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from fhir.resources.R4B.fhirtypes import IdentifierType
from fhir.resources.R4B.organization import Organization
from . import fhirtypes

class BeOrganization(Organization):

    __resource_type__ = "Organization"

    address: typing.List[fhirtypes.BeAddressType] = Field(
        None,
        alias="address",
        title="A belgian address for the organization",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[IdentifierType] | None = Field(
        None,
        alias="identifier",
        title="Identifies this organization  across multiple systems",
        description=(
            "Identifier for the organization that is used to identify the "
            "organization across multiple disparate systems."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: typing.List[fhirtypes.CDHCPARTYType] = Field(
        None,
        alias="type",
        title="Kind of organization",
        description="The kind(s) of organization that this is.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BeOrganization`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "active",
            "type",
            "name",
            "alias",
            "telecom",
            "address",
            "partOf",
            "contact",
            "endpoint",
        ]
