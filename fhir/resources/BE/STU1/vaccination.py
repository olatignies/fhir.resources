# -*- coding: utf-8 -*-
"""
Profile: https://www.ehealth.fgov.be/standards/fhir/core/StructureDefinition/be-vaccination
Release: STU1
Version: 1.0.3
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field

from fhir.resources.R4B import backboneelement, fhirtypes
from fhir.resources.R4B.immunization import Immunization
from . import fhirtypes

class BeVaccination(Immunization):

    resource_type = Field("BeVaccination", const=True)
