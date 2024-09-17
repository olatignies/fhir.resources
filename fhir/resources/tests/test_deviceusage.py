# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceUsage
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import deviceusage
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_deviceusage_1(inst):
    assert inst.device.concept.text == "ACME defribillator"
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http:goodhealth.org/identifiers"}
        ).valueUri
    )
    assert inst.identifier[0].value == "51ebb7a9-4e3a-4360-9a05-0cc2d869086f"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.reason[0].reference.display == "PHx of Appendectomy (surgery)"
    assert inst.reason[0].reference.reference == "Condition/example"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_deviceusage_1(base_settings):
    """No. 1 tests collection for DeviceUsage.
    Test File: deviceusage-example.json
    """
    filename = base_settings["unittest_data_dir"] / "deviceusage-example.json"
    inst = deviceusage.DeviceUsage.model_validate_json(filename.read_bytes())
    assert "DeviceUsage" == inst.get_resource_type()

    impl_deviceusage_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "DeviceUsage" == data["resourceType"]

    inst2 = deviceusage.DeviceUsage(**data)
    impl_deviceusage_1(inst2)
