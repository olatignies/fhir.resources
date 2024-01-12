# _*_ coding: utf-8 _*_
import datetime
import decimal
import re
from email.utils import formataddr, parseaddr
from typing import TYPE_CHECKING, Any, Dict, Optional, Pattern, Union
from uuid import UUID

from fhir.resources.core.fhirabstractmodel import FHIRAbstractModel
from fhir.resources.fhirtypes import (
    IdentifierType,
    CodeableConceptType,
    AddressType
)
from pydantic.v1 import AnyUrl
from pydantic.v1.errors import ConfigError, DateError, DateTimeError, TimeError
from pydantic.v1.main import load_str_bytes
from pydantic.v1.networks import validate_email
from pydantic.v1.types import (
    ConstrainedBytes,
    ConstrainedDecimal,
    ConstrainedInt,
    ConstrainedStr,
)
from pydantic.v1.validators import (
    bool_validator,
    parse_date,
    parse_datetime,
    parse_time,
)

if TYPE_CHECKING:
    from pydantic.v1.types import CallableGenerator
    from pydantic.v1.fields import ModelField
    from pydantic.v1 import BaseConfig

__author__ = "Olivier Latignies<olatignies@gmail.com>"

def get_fhir_type_class(model_name):
    try:
        return globals()[model_name + "Type"]
    except KeyError:
        raise LookupError(f"'{__name__}.{model_name}Type' doesnt found.")

class NIHDIType(IdentifierType):
    __resource_type__ = "NIHDI"

class CBEType(IdentifierType):
    __resource_type__ = "CBE"

class SSINType(IdentifierType):
    __resource_type__ = "SSIN"

class EHPType(IdentifierType):
    __resource_type__ = "EHP"

class CDHCPARTYType(CodeableConceptType):
    __resource_type__ = "CD-HCPARTY"

class BeAddressType(AddressType):
    __resource_type__ = "BeAddress"

__all__ = [
    "NIHDIType",
    "CBEType",
    "SSINType",
    "EHPType",
    "CDHCPARTYType",
    "BeAddressType",
]




