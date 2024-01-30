# -*- coding: utf-8 -*-
"""
Profile: https://www.ehealth.fgov.be/standards/fhir/core/StructureDefinition/be-patient
Release: STU1
Version: 2.0.1
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field

from fhir.resources.R4B import backboneelement, fhirtypes
from fhir.resources.R4B.patient import Patient
from . import fhirtypes

class BePatient(Patient):

    resource_type = Field("BePatient", const=True)

    address: typing.List[fhirtypes.BeAddressType] = Field(
        None,
        alias="address",
        title="An address for the individual in BE",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

