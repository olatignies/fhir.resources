import typing
from pydantic.v1 import Field
from fhir.resources import fhirtypes
from fhir.resources.codeableconcept import CodeableConcept

class CDHCPARTY(CodeableConcept):

    resource_type = Field("CDHCPARTY", const=True)

    coding: typing.List[fhirtypes.CodingType] = Field(
        None,
        alias="coding",
        title="use to code hc party",
        description="The hcparty code.",
        # if property is element of this resource.
        element_property=True,
    )
