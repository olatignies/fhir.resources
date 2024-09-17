# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EvidenceReport
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import evidencereport
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_evidencereport_1(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.status == "draft"
    assert inst.subject.note[0].text == "This is just an example."
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering ' "here]</div>"
    )
    assert inst.text.status == "generated"


def test_evidencereport_1(base_settings):
    """No. 1 tests collection for EvidenceReport.
    Test File: evidencereport-example.json
    """
    filename = base_settings["unittest_data_dir"] / "evidencereport-example.json"
    inst = evidencereport.EvidenceReport.model_validate_json(filename.read_bytes())
    assert "EvidenceReport" == inst.get_resource_type()

    impl_evidencereport_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "EvidenceReport" == data["resourceType"]

    inst2 = evidencereport.EvidenceReport(**data)
    impl_evidencereport_1(inst2)
