# _*_ coding: utf-8 _*_
import datetime
import decimal
import re
from email.utils import formataddr, parseaddr
from typing import TYPE_CHECKING, Any, Dict, Optional, Pattern, Union
from uuid import UUID

from fhir.resources.core.fhirabstractmodel import FHIRAbstractModel
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

from fhir.resources.R4B.fhirtypes import PatientType

if TYPE_CHECKING:
    from pydantic.v1.types import CallableGenerator
    from pydantic.v1.fields import ModelField
    from pydantic.v1 import BaseConfig

__author__ = "Olivier Latignies<olatignies@gmail.com>"

class AbstractType(dict):
    """ """

    __fhir_release__: str = "2.0.1"
    __resource_type__: str = ...  # type: ignore

    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(type=cls.__resource_type__)

    @classmethod
    def __get_validators__(cls) -> "CallableGenerator":
        from . import fhirtypesvalidators

        yield getattr(fhirtypesvalidators, cls.__resource_type__.lower() + "_validator")

    @classmethod
    def is_primitive(cls) -> bool:
        """ """
        return False

    @classmethod
    def fhir_type_name(cls) -> str:
        """ """
        return cls.__resource_type__

def get_fhir_type_class(model_name):
    try:
        return globals()[model_name + "Type"]
    except KeyError:
        raise LookupError(f"'{__name__}.{model_name}Type' doesnt found.")

class CodeableConceptType(AbstractType):
    __resource_type__ = "CodeableConcept"

class Primitive:
    """FHIR Primitive Data Type Base Class"""

    __fhir_release__: str = "R4B"
    __visit_name__: Optional[str] = None
    regex: Optional[Pattern[str]] = None

    @classmethod
    def is_primitive(cls) -> bool:
        """ """
        return True

    @classmethod
    def fhir_type_name(cls) -> Optional[str]:
        """ """
        return cls.__visit_name__

class IdentifierType(AbstractType):
    __resource_type__ = "Identifier"

class String(ConstrainedStr, Primitive):
    """A sequence of Unicode characters
    Note that strings SHALL NOT exceed 1MB (1024*1024 characters) in size.
    Strings SHOULD not contain Unicode character points below 32, except for
    u0009 (horizontal tab), u0010 (carriage return) and u0013 (line feed).
    Leading and Trailing whitespace is allowed, but SHOULD be removed when using
    the XML format. Note: This means that a string that consists only of whitespace
    could be trimmed to nothing, which would be treated as an invalid element value.
    Therefore strings SHOULD always contain non-whitespace content"""

    regex = re.compile(r"[ \r\n\t\S]+")
    allow_empty_str = False
    __visit_name__ = "string"

    @classmethod
    def configure_empty_str(cls, allow: Optional[bool] = None):
        """About empty string
        1. https://bit.ly/3woGnFG
        2. https://github.com/nazrulworld/fhir.resources/issues/65#issuecomment-856693256
        There are a lot of valid discussion about accept empty string as String value but
        it is cleared for us that according to FHIR Specification, empty string is not valid!
        However in real use cases, we see empty string is coming other (when the task is related
        to query data from other system)

        It is in your hand now, if you would like to allow empty string!
        by default empty string is not
        accepted.
        """
        if isinstance(allow, bool):
            cls.allow_empty_str = allow

    @classmethod
    def validate(cls, value: Union[str]) -> Union[str]:
        if cls.allow_empty_str is True and value in ("", ""):
            return value
        # do the default things
        return ConstrainedStr.validate.__func__(cls, value)  # type: ignore

    @classmethod
    def to_string(cls, value):
        """ """
        if isinstance(value, bytes):
            value = value.decode()
        elif value is None:
            value = ""
        assert isinstance(value, str)
        return value

class Code(ConstrainedStr, Primitive):
    """Indicates that the value is taken from a set of controlled
    strings defined elsewhere (see Using codes for further discussion).
    Technically, a code is restricted to a string which has at least one
    character and no leading or trailing whitespace, and where there is
    no whitespace other than single spaces in the contents"""

    regex = re.compile(r"^[^\s]+(\s[^\s]+)*$")
    __visit_name__ = "code"

    @classmethod
    def to_string(cls, value):
        """ """
        if isinstance(value, bytes):
            value = value.decode()
        assert isinstance(value, str)
        return value

class ReferenceType(AbstractType):
    __resource_type__ = "Reference"

class AddressType(AbstractType):
    __resource_type__ = "Address"

class NIHDIType(IdentifierType):
    __resource_type__ = "NIHDI"

class CBEType(IdentifierType):
    __resource_type__ = "CBE"

class SSINType(IdentifierType):
    __resource_type__ = "SSIN"

class EHPType(IdentifierType):
    __resource_type__ = "EHP"

class CDHCPARTYType(CodeableConceptType):
    __resource_type__ = "CDHCPARTY"

class BeAddressType(AddressType):
    __resource_type__ = "BeAddress"

class BePatientType(PatientType):
    __resource_type__ = "BePatient"

__all__ = [
    "NIHDIType",
    "CBEType",
    "SSINType",
    "EHPType",
    "CDHCPARTYType",
    "BeAddressType",
    "BePatientType",
]




