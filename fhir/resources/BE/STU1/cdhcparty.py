import typing
from pydantic import Field
from fhir.resources import fhirtypes
from fhir.resources.codeableconcept import CodeableConcept

class CDHCPARTY(CodeableConcept):

    __resource_type__ = "CDHCPARTY"

    coding: typing.List[fhirtypes.CodingType] = Field(
        None,
        alias="coding",
        title="use to code hc party",
        description="The hcparty code.",
        # if property is element of this resource.
        element_property=True,
    )
