# -*- coding: utf-8 -*-
"""
Profile: https://www.ehealth.fgov.be/standards/fhir/core/StructureDefinition/be-patient
Release: STU1
Version: 2.0.1
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from fhir.resources.R4B.patient import Patient
from . import fhirtypes

class BePatient(Patient):

    __resource_type__ = "BePatient"

    address: typing.List[fhirtypes.BeAddressType] = Field(
        None,
        alias="address",
        title="An address for the individual in BE",
        description=None,
        json_schema_extra={"element_property": True},
    )

