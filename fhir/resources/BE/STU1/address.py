# -*- coding: utf-8 -*-
"""
Profile: https://www.ehealth.fgov.be/standards/fhir/core/StructureDefinition/be-address
Release: STU1
Version: 2.0.1
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field

from fhir.resources.R4B import backboneelement, fhirtypes
from fhir.resources.R4B.address import Address
from . import fhirtypes

class BeAddress(Address):

    resource_type = Field("BeAddress", const=True)

    country: fhirtypes.String = Field(
        None,
        alias="country",
        title="Country (e.g. can be ISO 3166 2 or 3 letter code)",
        description="Country - a nation as commonly understood or generally accepted.",
        # if property is element of this resource.
        element_property=True,
    )

    line: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="line",
        title="Street name, number, direction & P.O. Box etc.",
        description=(
            "This component contains the house number, apartment number, street "
            "name, street direction,  P.O. Box number, delivery hints, and similar "
            "address information."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="postal | physical | both",
        description=(
            "Distinguishes between physical addresses (those you can visit) and "
            "mailing addresses (e.g. PO Boxes and care-of addresses). Most "
            "addresses are both."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        # enum_values=["postal", "physical", "both"],
    )

    use: fhirtypes.Code = Field(
        None,
        alias="use",
        title="home | work | temp | old | billing - purpose of this address",
        description="The purpose of this address.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        # enum_values=["home", "work", "temp", "old", "billing"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BeAddress`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "use",
            "type",
            "text",
            "line",
            "city",
            "district",
            "state",
            "postalCode",
            "country",
            "period",
        ]
