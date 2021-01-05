# -*- mode:python; coding:utf-8 -*-

# Copyright (c) 2020 IBM Corp. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for models util module."""
import inspect
import os
import pkgutil
import sys
import uuid
from datetime import date, datetime
from typing import Any, Dict, List

import pydantic.networks
from pydantic import ConstrainedStr, typing

import pytest

import trestle.core.err as err
import trestle.core.generators as gens
import trestle.oscal as oscal
import trestle.oscal.assessment_plan as ap
import trestle.oscal.catalog as catalog
import trestle.oscal.ssp as ssp
from trestle.core.base_model import OscalBaseModel


def is_valid_uuid(val: Any) -> bool:
    """Check if a string is a valid uuid."""
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False


def test_get_sample_value_by_type() -> None:
    """Test get_sample_value_by_type function."""
    assert type(gens.generate_sample_value_by_type(datetime, '')) == datetime
    assert gens.generate_sample_value_by_type(bool, '') is False
    assert gens.generate_sample_value_by_type(int, '') == 0
    assert gens.generate_sample_value_by_type(str, '') == 'REPLACE_ME'
    assert gens.generate_sample_value_by_type(float, '') == 0.0
    assert gens.generate_sample_value_by_type(ConstrainedStr, '') == '00000000-0000-4000-8000-000000000000'
    uuid_ = gens.generate_sample_value_by_type(ConstrainedStr, 'uuid')
    assert gens.generate_sample_value_by_type(ssp.Type, '') == ssp.Type('person')
    assert is_valid_uuid(uuid_) and str(uuid_) != '00000000-0000-4000-8000-000000000000'
    assert gens.generate_sample_value_by_type(ConstrainedStr, 'date_authorized') == date.today().isoformat()
    assert gens.generate_sample_value_by_type(pydantic.networks.EmailStr,
                                              'anything') == pydantic.networks.EmailStr('dummy@sample.com')
    assert gens.generate_sample_value_by_type(pydantic.networks.AnyUrl, 'anything') == pydantic.networks.AnyUrl(
        'https://sample.com/replaceme.html', scheme='http', host='sample.com'
    )
    with pytest.raises(err.TrestleError):
        gens.generate_sample_value_by_type(list, 'uuid')


def test_generate_sample_with_conint() -> None:
    """Generate a sample model where it is known to contain conint fields."""
    gens.generate_sample_model(ap.AtFrequency)


def test_generate_sample_with_list_primitives() -> None:
    """A switch is required to handle cases where the inner object of a list is not a OscalBaseModel."""
    gens.generate_sample_model(ap.Observation)


def test_generate_sample_model() -> None:
    """Test utils method generate_sample_model."""
    # Create the expected catalog first
    expected_ctlg_dict = {
        'uuid': 'ea784488-49a1-4ee5-9830-38058c7c10a4',
        'metadata': {
            'title': 'REPLACE_ME',
            'last-modified': '2020-10-21T06:52:10.387+00:00',
            'version': 'REPLACE_ME',
            'oscal-version': 'REPLACE_ME'
        }
    }
    expected_ctlg = catalog.Catalog(**expected_ctlg_dict)

    actual_ctlg = gens.generate_sample_model(catalog.Catalog)

    # Check if uuid is valid, then change to uuid of expected catalog, as newly generated
    # uuids will always be different
    assert is_valid_uuid(actual_ctlg.uuid)
    actual_ctlg.uuid = expected_ctlg.uuid
    # Check if last-modified datetime is of type datetime, and then equate in actual and expected
    assert type(actual_ctlg.metadata) is catalog.Metadata
    assert type(actual_ctlg.metadata.last_modified) is datetime
    actual_ctlg.metadata.last_modified = expected_ctlg.metadata.last_modified
    # Check that expected generated catalog is now same a actual catalog
    assert expected_ctlg == actual_ctlg

    # Test list type models
    expected_role = catalog.Role(**{'id': 'REPLACE_ME', 'title': 'REPLACE_ME'})
    list_role = gens.generate_sample_model(List[catalog.Role])
    assert type(list_role) is list
    actual_role = list_role[0]
    assert expected_role == actual_role

    # Test dict type models
    expected_rp = {'party-uuids': ['00000000-0000-4000-8000-000000000000']}
    expected_rp = catalog.ResponsibleParty(**expected_rp)
    expected_rp_dict = {'REPLACE_ME': expected_rp}
    actual_rp_dict = gens.generate_sample_model(Dict[str, catalog.ResponsibleParty])
    assert type(actual_rp_dict) is dict
    assert expected_rp_dict == actual_rp_dict


def test_get_all_sample_models() -> None:
    """Test we can get all models which exist."""
    pkgpath = os.path.dirname(oscal.__file__)
    for _, name, _ in pkgutil.iter_modules([pkgpath]):
        __import__(f'trestle.oscal.{name}')
        clsmembers = inspect.getmembers(sys.modules[f'trestle.oscal.{name}'], inspect.isclass)
        for _, oscal_cls in clsmembers:
            # This removes some enums and other objects.

            if issubclass(oscal_cls, OscalBaseModel):
                gens.generate_sample_model(oscal_cls)
