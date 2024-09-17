# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationRequest
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class MedicationRequest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Ordering of medication for patient or group.
    An order or request for both supply of the medication and the instructions
    for administration of the medication to a patient. The resource is called
    "MedicationRequest" rather than "MedicationPrescription" or
    "MedicationOrder" to generalize the use across inpatient and outpatient
    settings, including care plans, etc., and to harmonize with workflow
    patterns.
    """

    __resource_type__ = "MedicationRequest"

    authoredOn: fhirtypes.DateTimeType = Field(  # type: ignore
        None,
        alias="authoredOn",
        title="When request was initially authored",
        description=(
            "The date (and perhaps time) when the prescription was initially "
            "written or authored on."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_authoredOn", title="Extension field for ``authoredOn``."
    )

    basedOn: typing.List[fhirtypes.ReferenceType] = Field(  # type: ignore
        None,
        alias="basedOn",
        title="What request fulfills",
        description=(
            "A plan or request that is fulfilled in whole or in part by this "
            "medication request."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "CarePlan",
                "MedicationRequest",
                "ServiceRequest",
                "ImmunizationRecommendation",
            ],
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] = Field(  # type: ignore
        None,
        alias="category",
        title="Type of medication usage",
        description=(
            "Indicates the type of medication request (for example, where the "
            "medication is expected to be consumed or administered (i.e. inpatient "
            "or outpatient))."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    courseOfTherapyType: fhirtypes.CodeableConceptType = Field(  # type: ignore
        None,
        alias="courseOfTherapyType",
        title="Overall pattern of medication administration",
        description=(
            "The description of the overall patte3rn of the administration of the "
            "medication to the patient."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    detectedIssue: typing.List[fhirtypes.ReferenceType] = Field(  # type: ignore
        None,
        alias="detectedIssue",
        title="Clinical Issue with action",
        description=(
            "Indicates an actual or potential clinical issue with or between one or"
            " more active or proposed clinical actions for a patient; e.g. Drug-"
            "drug interaction, duplicate therapy, dosage alert etc."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DetectedIssue"],
        },
    )

    dispenseRequest: fhirtypes.MedicationRequestDispenseRequestType = Field(  # type: ignore
        None,
        alias="dispenseRequest",
        title="Medication supply authorization",
        description=(
            "Indicates the specific details for the dispense or medication supply "
            "part of a medication request (also known as a Medication Prescription "
            "or Medication Order).  Note that this information is not always sent "
            "with the order.  There may be in some settings (e.g. hospitals) "
            "institutional or system support for completing the dispense details in"
            " the pharmacy department."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    doNotPerform: bool = Field(  # type: ignore
        None,
        alias="doNotPerform",
        title="True if request is prohibiting action",
        description=(
            "If true indicates that the provider is asking for the medication "
            "request not to occur."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    doNotPerform__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_doNotPerform", title="Extension field for ``doNotPerform``."
    )

    dosageInstruction: typing.List[fhirtypes.DosageType] = Field(  # type: ignore
        None,
        alias="dosageInstruction",
        title="How the medication should be taken",
        description="Indicates how the medication is to be used by the patient.",
        json_schema_extra={
            "element_property": True,
        },
    )

    encounter: fhirtypes.ReferenceType = Field(  # type: ignore
        None,
        alias="encounter",
        title="Encounter created as part of encounter/admission/stay",
        description=(
            "The Encounter during which this [x] was created or to which the "
            "creation of this record is tightly associated."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    eventHistory: typing.List[fhirtypes.ReferenceType] = Field(  # type: ignore
        None,
        alias="eventHistory",
        title="A list of events of interest in the lifecycle",
        description=(
            "Links to Provenance records for past versions of this resource or "
            "fulfilling request or event resources that identify key state "
            "transitions or updates that are likely to be relevant to a user "
            "looking at the current version of the resource."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Provenance"],
        },
    )

    groupIdentifier: fhirtypes.IdentifierType = Field(  # type: ignore
        None,
        alias="groupIdentifier",
        title="Composite request this is part of",
        description=(
            "A shared identifier common to all requests that were authorized more "
            "or less simultaneously by a single author, representing the identifier"
            " of the requisition or prescription."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(  # type: ignore
        None,
        alias="identifier",
        title="External ids for this request",
        description=(
            "Identifiers associated with this medication request that are defined "
            "by business processes and/or used to refer to it when a direct URL "
            "reference to the resource itself is not appropriate. They are business"
            " identifiers assigned to this resource by the performer or other "
            "systems and remain constant as the resource is updated and propagates "
            "from server to server."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    instantiatesCanonical: typing.List[typing.Optional[fhirtypes.CanonicalType]] = Field(  # type: ignore
        None,
        alias="instantiatesCanonical",
        title="Instantiates FHIR protocol or definition",
        description=(
            "The URL pointing to a protocol, guideline, orderset, or other "
            "definition that is adhered to in whole or in part by this "
            "MedicationRequest."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    instantiatesCanonical__ext: typing.List[typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(  # type: ignore
        None,
        alias="_instantiatesCanonical",
        title="Extension field for ``instantiatesCanonical``.",
    )

    instantiatesUri: typing.List[typing.Optional[fhirtypes.UriType]] = Field(  # type: ignore
        None,
        alias="instantiatesUri",
        title="Instantiates external protocol or definition",
        description=(
            "The URL pointing to an externally maintained protocol, guideline, "
            "orderset or other definition that is adhered to in whole or in part by"
            " this MedicationRequest."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    instantiatesUri__ext: typing.List[typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(  # type: ignore
        None, alias="_instantiatesUri", title="Extension field for ``instantiatesUri``."
    )

    insurance: typing.List[fhirtypes.ReferenceType] = Field(  # type: ignore
        None,
        alias="insurance",
        title="Associated insurance coverage",
        description=(
            "Insurance plans, coverage extensions, pre-authorizations and/or pre-"
            "determinations that may be required for delivering the requested "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Coverage", "ClaimResponse"],
        },
    )

    intent: fhirtypes.CodeType = Field(  # type: ignore
        None,
        alias="intent",
        title=(
            "proposal | plan | order | original-order | reflex-order | filler-order"
            " | instance-order | option"
        ),
        description="Whether the request is a proposal, plan, or an original order.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "proposal",
                "plan",
                "order",
                "original-order",
                "reflex-order",
                "filler-order",
                "instance-order",
                "option",
            ],
        },
    )
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_intent", title="Extension field for ``intent``."
    )

    medicationCodeableConcept: fhirtypes.CodeableConceptType = Field(  # type: ignore
        None,
        alias="medicationCodeableConcept",
        title="Medication to be taken",
        description=(
            "Identifies the medication being requested. This is a link to a "
            "resource that represents the medication which may be the details of "
            "the medication or simply an attribute carrying a code that identifies "
            "the medication from a known list of medications."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e medication[x]
            "one_of_many": "medication",
            "one_of_many_required": True,
        },
    )

    medicationReference: fhirtypes.ReferenceType = Field(  # type: ignore
        None,
        alias="medicationReference",
        title="Medication to be taken",
        description=(
            "Identifies the medication being requested. This is a link to a "
            "resource that represents the medication which may be the details of "
            "the medication or simply an attribute carrying a code that identifies "
            "the medication from a known list of medications."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e medication[x]
            "one_of_many": "medication",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Medication"],
        },
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(  # type: ignore
        None,
        alias="note",
        title="Information about the prescription",
        description=(
            "Extra information about the prescription that could not be conveyed by"
            " the other attributes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    performer: fhirtypes.ReferenceType = Field(  # type: ignore
        None,
        alias="performer",
        title="Intended performer of administration",
        description=(
            "The specified desired performer of the medication treatment (e.g. the "
            "performer of the medication administration)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
                "Patient",
                "Device",
                "RelatedPerson",
                "CareTeam",
            ],
        },
    )

    performerType: fhirtypes.CodeableConceptType = Field(  # type: ignore
        None,
        alias="performerType",
        title="Desired kind of performer of the medication administration",
        description=(
            "Indicates the type of performer of the administration of the "
            "medication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    priorPrescription: fhirtypes.ReferenceType = Field(  # type: ignore
        None,
        alias="priorPrescription",
        title="An order/prescription that is being replaced",
        description=(
            "A link to a resource representing an earlier order related order or "
            "prescription."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MedicationRequest"],
        },
    )

    priority: fhirtypes.CodeType = Field(  # type: ignore
        None,
        alias="priority",
        title="routine | urgent | asap | stat",
        description=(
            "Indicates how quickly the Medication Request should be addressed with "
            "respect to other requests."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["routine", "urgent", "asap", "stat"],
        },
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_priority", title="Extension field for ``priority``."
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] = Field(  # type: ignore
        None,
        alias="reasonCode",
        title="Reason or indication for ordering or not ordering the medication",
        description=(
            "The reason or the indication for ordering or not ordering the "
            "medication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] = Field(  # type: ignore
        None,
        alias="reasonReference",
        title=(
            "Condition or observation that supports why the prescription is being "
            "written"
        ),
        description="Condition or observation that supports why the medication was ordered.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Condition", "Observation"],
        },
    )

    recorder: fhirtypes.ReferenceType = Field(  # type: ignore
        None,
        alias="recorder",
        title="Person who entered the request",
        description=(
            "The person who entered the order on behalf of another individual for "
            "example in the case of a verbal or a telephone order."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "PractitionerRole"],
        },
    )

    reportedBoolean: bool = Field(  # type: ignore
        None,
        alias="reportedBoolean",
        title="Reported rather than primary record",
        description=(
            "Indicates if this record was captured as a secondary 'reported' record"
            " rather than as an original primary source-of-truth record.  It may "
            "also indicate the source of the report."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e reported[x]
            "one_of_many": "reported",
            "one_of_many_required": False,
        },
    )
    reportedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_reportedBoolean", title="Extension field for ``reportedBoolean``."
    )

    reportedReference: fhirtypes.ReferenceType = Field(  # type: ignore
        None,
        alias="reportedReference",
        title="Reported rather than primary record",
        description=(
            "Indicates if this record was captured as a secondary 'reported' record"
            " rather than as an original primary source-of-truth record.  It may "
            "also indicate the source of the report."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e reported[x]
            "one_of_many": "reported",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Practitioner",
                "PractitionerRole",
                "RelatedPerson",
                "Organization",
            ],
        },
    )

    requester: fhirtypes.ReferenceType = Field(  # type: ignore
        None,
        alias="requester",
        title="Who/What requested the Request",
        description=(
            "The individual, organization, or device that initiated the request and"
            " has responsibility for its activation."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
                "Patient",
                "RelatedPerson",
                "Device",
            ],
        },
    )

    status: fhirtypes.CodeType = Field(  # type: ignore
        None,
        alias="status",
        title=(
            "active | on-hold | cancelled | completed | entered-in-error | stopped "
            "| draft | unknown"
        ),
        description=(
            "A code specifying the current state of the order.  Generally, this "
            "will be active or completed state."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "active",
                "on-hold",
                "cancelled",
                "completed",
                "entered-in-error",
                "stopped",
                "draft",
                "unknown",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    statusReason: fhirtypes.CodeableConceptType = Field(  # type: ignore
        None,
        alias="statusReason",
        title="Reason for current status",
        description="Captures the reason for the current state of the MedicationRequest.",
        json_schema_extra={
            "element_property": True,
        },
    )

    subject: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="subject",
        title="Who or group medication request is for",
        description=(
            "A link to a resource representing the person or set of individuals to "
            "whom the medication will be given."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Group"],
        },
    )

    substitution: fhirtypes.MedicationRequestSubstitutionType = Field(  # type: ignore
        None,
        alias="substitution",
        title="Any restrictions on medication substitution",
        description=(
            "Indicates whether or not substitution can or should be part of the "
            "dispense. In some cases, substitution must happen, in other cases "
            "substitution must not happen. This block explains the prescriber's "
            "intent. If nothing is specified substitution may be done."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    supportingInformation: typing.List[fhirtypes.ReferenceType] = Field(  # type: ignore
        None,
        alias="supportingInformation",
        title="Information to support ordering of the medication",
        description=(
            "Include additional information (for example, patient height and "
            "weight) that supports the ordering of the medication."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationRequest`` according specification,
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
            "status",
            "statusReason",
            "intent",
            "category",
            "priority",
            "doNotPerform",
            "reportedBoolean",
            "reportedReference",
            "medicationCodeableConcept",
            "medicationReference",
            "subject",
            "encounter",
            "supportingInformation",
            "authoredOn",
            "requester",
            "performer",
            "performerType",
            "recorder",
            "reasonCode",
            "reasonReference",
            "instantiatesCanonical",
            "instantiatesUri",
            "basedOn",
            "groupIdentifier",
            "courseOfTherapyType",
            "insurance",
            "note",
            "dosageInstruction",
            "dispenseRequest",
            "substitution",
            "priorPrescription",
            "detectedIssue",
            "eventHistory",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("intent", "intent__ext"), ("status", "status__ext")]
        return required_fields

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "medication": ["medicationCodeableConcept", "medicationReference"],
            "reported": ["reportedBoolean", "reportedReference"],
        }
        return one_of_many_fields


class MedicationRequestDispenseRequest(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Medication supply authorization.
    Indicates the specific details for the dispense or medication supply part
    of a medication request (also known as a Medication Prescription or
    Medication Order).  Note that this information is not always sent with the
    order.  There may be in some settings (e.g. hospitals) institutional or
    system support for completing the dispense details in the pharmacy
    department.
    """

    __resource_type__ = "MedicationRequestDispenseRequest"

    dispenseInterval: fhirtypes.DurationType = Field(  # type: ignore
        None,
        alias="dispenseInterval",
        title="Minimum period of time between dispenses",
        description=(
            "The minimum period of time that must occur between dispenses of the "
            "medication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    expectedSupplyDuration: fhirtypes.DurationType = Field(  # type: ignore
        None,
        alias="expectedSupplyDuration",
        title="Number of days supply per dispense",
        description=(
            "Identifies the period time over which the supplied product is expected"
            " to be used, or the length of time the dispense is expected to last."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    initialFill: fhirtypes.MedicationRequestDispenseRequestInitialFillType = Field(  # type: ignore
        None,
        alias="initialFill",
        title="First fill details",
        description=(
            "Indicates the quantity or duration for the first dispense of the "
            "medication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    numberOfRepeatsAllowed: fhirtypes.UnsignedIntType = Field(  # type: ignore
        None,
        alias="numberOfRepeatsAllowed",
        title="Number of refills authorized",
        description=(
            "An integer indicating the number of times, in addition to the original"
            " dispense, (aka refills or repeats) that the patient can receive the "
            "prescribed medication. Usage Notes: This integer does not include the "
            "original order dispense. This means that if an order indicates "
            'dispense 30 tablets plus "3 repeats", then the order can be dispensed '
            "a total of 4 times and the patient can receive a total of 120 tablets."
            "  A prescriber may explicitly say that zero refills are permitted "
            "after the initial dispense."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    numberOfRepeatsAllowed__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None,
        alias="_numberOfRepeatsAllowed",
        title="Extension field for ``numberOfRepeatsAllowed``.",
    )

    performer: fhirtypes.ReferenceType = Field(  # type: ignore
        None,
        alias="performer",
        title="Intended dispenser",
        description=(
            "Indicates the intended dispensing Organization specified by the "
            "prescriber."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    quantity: fhirtypes.QuantityType = Field(  # type: ignore
        None,
        alias="quantity",
        title="Amount of medication to supply per dispense",
        description="The amount that is to be dispensed for one fill.",
        json_schema_extra={
            "element_property": True,
        },
    )

    validityPeriod: fhirtypes.PeriodType = Field(  # type: ignore
        None,
        alias="validityPeriod",
        title="Time period supply is authorized for",
        description=(
            "This indicates the validity period of a prescription (stale dating the"
            " Prescription)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationRequestDispenseRequest`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "initialFill",
            "dispenseInterval",
            "validityPeriod",
            "numberOfRepeatsAllowed",
            "quantity",
            "expectedSupplyDuration",
            "performer",
        ]


class MedicationRequestDispenseRequestInitialFill(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    First fill details.
    Indicates the quantity or duration for the first dispense of the
    medication.
    """

    __resource_type__ = "MedicationRequestDispenseRequestInitialFill"

    duration: fhirtypes.DurationType = Field(  # type: ignore
        None,
        alias="duration",
        title="First fill duration",
        description="The length of time that the first dispense is expected to last.",
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType = Field(  # type: ignore
        None,
        alias="quantity",
        title="First fill quantity",
        description="The amount or quantity to provide as part of the first dispense.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationRequestDispenseRequestInitialFill`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "quantity", "duration"]


class MedicationRequestSubstitution(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Any restrictions on medication substitution.
    Indicates whether or not substitution can or should be part of the
    dispense. In some cases, substitution must happen, in other cases
    substitution must not happen. This block explains the prescriber's intent.
    If nothing is specified substitution may be done.
    """

    __resource_type__ = "MedicationRequestSubstitution"

    allowedBoolean: bool = Field(  # type: ignore
        None,
        alias="allowedBoolean",
        title="Whether substitution is allowed or not",
        description=(
            "True if the prescriber allows a different drug to be dispensed from "
            "what was prescribed."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e allowed[x]
            "one_of_many": "allowed",
            "one_of_many_required": True,
        },
    )
    allowedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_allowedBoolean", title="Extension field for ``allowedBoolean``."
    )

    allowedCodeableConcept: fhirtypes.CodeableConceptType = Field(  # type: ignore
        None,
        alias="allowedCodeableConcept",
        title="Whether substitution is allowed or not",
        description=(
            "True if the prescriber allows a different drug to be dispensed from "
            "what was prescribed."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e allowed[x]
            "one_of_many": "allowed",
            "one_of_many_required": True,
        },
    )

    reason: fhirtypes.CodeableConceptType = Field(  # type: ignore
        None,
        alias="reason",
        title="Why should (not) substitution be made",
        description=(
            "Indicates the reason for the substitution, or why substitution must or"
            " must not be performed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationRequestSubstitution`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "allowedBoolean",
            "allowedCodeableConcept",
            "reason",
        ]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {"allowed": ["allowedBoolean", "allowedCodeableConcept"]}
        return one_of_many_fields
