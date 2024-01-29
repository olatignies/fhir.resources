# -*- coding: utf-8 -*-
"""
Profile: https://www.ehealth.fgov.be/standards/fhir/core/StructureDefinition/be-organization
Release: STU1
Version: 2.0.1
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field

from fhir.resources.R4B import backboneelement, fhirtypes
from fhir.resources.R4B.organization import Organization
from . import fhirtypes

class BeOrganization(Organization):

    resource_type = Field("BeOrganization", const=True)

    address: typing.List[fhirtypes.BeAddressType] = Field(
        None,
        alias="address",
        title="An address for the organization",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[typing.Union[fhirtypes.NIHDIType,fhirtypes.CBEType,fhirtypes.SSINType,fhirtypes.EHPType]] = Field(
        None,
        alias="identifier",
        title="Identifies this organization  across multiple systems",
        description=(
            "Identifier for the organization that is used to identify the "
            "organization across multiple disparate systems."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: typing.List[fhirtypes.CDHCPARTYType] = Field(
        None,
        alias="type",
        title="Kind of organization",
        description="The kind(s) of organization that this is.",
        # if property is element of this resource.
        element_property=True,
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
