import typing
from pydantic.v1 import Field
from fhir.resources import fhirtypes
from fhir.resources.R4B.namingsystem import NamingSystem

class BeNIHDINamingSystem(NamingSystem):

    __resource_type__ = "NamingSystem"

    coding: typing.List[fhirtypes.CodingType] = Field(
        None,
        alias="coding",
        title="use to code hc party",
        description="The hcparty code.",
        # if property is element of this resource.
        element_property=True,
    )
