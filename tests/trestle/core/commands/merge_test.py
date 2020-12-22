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
"""Tests for trestle split command."""
import argparse
import os
import shutil
from pathlib import Path

import pytest

from tests import test_utils

import trestle.oscal.catalog as oscatalog
from trestle.core.commands.merge import MergeCmd
from trestle.core.err import TrestleError
from trestle.core.models.actions import CreatePathAction, RemovePathAction, WriteFileAction
from trestle.core.models.elements import Element, ElementPath
from trestle.core.models.file_content_type import FileContentType
from trestle.core.models.plans import Plan
from trestle.utils import fs
from trestle.utils.load_distributed import load_distributed


def test_merge_invalid_element_path(testdata_dir, tmp_trestle_dir):
    """Test to make sure each element in -e contains 2 parts at least."""
    cmd = MergeCmd()
    args = argparse.Namespace(verbose=1, element='catalog', list_available_elements=False)
    with pytest.raises(TrestleError):
        cmd._run(args)

    args = argparse.Namespace(verbose=1, element='catalog.metadata', list_available_elements=False)
    test_utils.ensure_trestle_config_dir(tmp_trestle_dir)
    test_data_source = testdata_dir / 'split_merge/step4_split_groups_array/catalogs'
    catalogs_dir = Path('catalogs/')
    mycatalog_dir = catalogs_dir / 'mycatalog'
    catalog_dir = mycatalog_dir / 'catalog'

    # Copy files from test/data/split_merge/step4
    shutil.rmtree(catalogs_dir)
    shutil.copytree(test_data_source, catalogs_dir)

    os.chdir(mycatalog_dir)
    cmd._run(args)


def test_merge_plan_simple_case(testdata_dir, tmp_trestle_dir):
    """Test '$mycatalog$ trestle merge -e catalog.back-matter'."""
    # Assume we are running a command like below
    # trestle merge -e catalog.back-matter
    content_type = FileContentType.JSON
    fext = FileContentType.to_file_extension(content_type)

    # prepare trestle project dir with the file
    test_utils.ensure_trestle_config_dir(tmp_trestle_dir)

    test_data_source = testdata_dir / 'split_merge/step4_split_groups_array/catalogs'

    catalogs_dir = Path('catalogs/')
    mycatalog_dir = catalogs_dir / 'mycatalog'
    catalog_dir = mycatalog_dir / 'catalog'

    # Copy files from test/data/split_merge/step4
    shutil.rmtree(catalogs_dir)
    shutil.copytree(test_data_source, catalogs_dir)

    os.chdir(mycatalog_dir)
    catalog_file = Path(f'catalog{fext}')
    catalog_dir = Path('catalog/')
    back_matter_file = catalog_dir / f'back-matter{fext}'

    assert catalog_file.exists()
    assert back_matter_file.exists()

    # Read files

    # The destination file/model needs to be loaded in a stripped model
    stripped_catalog_type, _ = fs.get_stripped_contextual_model(catalog_file.absolute())
    stripped_catalog = stripped_catalog_type.oscal_read(catalog_file)

    # Back-matter model needs to be complete and if it is decomposed, needs to be merged recursively first
    back_matter = oscatalog.BackMatter.oscal_read(back_matter_file)

    # Back-matter needs to be inserted in a stripped Catalog that does NOT exclude the back-matter fields

    merged_catalog_type, merged_catalog_alias = fs.get_stripped_contextual_model(
        catalog_file.absolute(), aliases_not_to_be_stripped=['back-matter'])
    merged_dict = stripped_catalog.__dict__
    merged_dict['back-matter'] = back_matter
    merged_catalog = merged_catalog_type(**merged_dict)

    element = Element(merged_catalog, merged_catalog_alias)

    # Create hand-crafter merge plan
    reset_destination_action = CreatePathAction(catalog_file.absolute(), clear_content=True)
    write_destination_action = WriteFileAction(catalog_file, element, content_type=content_type)
    delete_element_action = RemovePathAction(back_matter_file.absolute())

    expected_plan: Plan = Plan()
    expected_plan.add_action(reset_destination_action)
    expected_plan.add_action(write_destination_action)
    expected_plan.add_action(delete_element_action)

    # Call merged()

    generated_plan = MergeCmd.merge(ElementPath('catalog.back-matter'))

    # Assert the generated plan matches the expected plan'
    assert generated_plan == expected_plan


def test_merge_expanded_metadata_into_catalog(testdata_dir, tmp_trestle_dir):
    """Test '$mycatalog$ trestle merge -e catalog.metadata' when metadata is already split."""
    # Assume we are running a command like below
    # trestle merge -e catalog.back-matter
    content_type = FileContentType.JSON
    fext = FileContentType.to_file_extension(content_type)

    # prepare trestle project dir with the file
    test_utils.ensure_trestle_config_dir(tmp_trestle_dir)

    test_data_source = testdata_dir / 'split_merge/step4_split_groups_array/catalogs'
    catalogs_dir = Path('catalogs/')
    mycatalog_dir = catalogs_dir / 'mycatalog'
    catalog_dir = mycatalog_dir / 'catalog'

    # Copy files from test/data/split_merge/step4
    shutil.rmtree(catalogs_dir)
    shutil.copytree(test_data_source, catalogs_dir)

    # Change directory to mycatalog_dir
    os.chdir(mycatalog_dir)
    catalog_file = Path(f'catalog{fext}')
    catalog_dir = Path('catalog/')
    metadata_dir = catalog_dir / 'metadata'
    metadata_file = catalog_dir / f'metadata{fext}'

    assert catalog_file.exists()
    assert metadata_dir.exists()
    assert metadata_file.exists()

    # Read files

    # Create hand-crafter merge plan
    expected_plan: Plan = Plan()

    reset_destination_action = CreatePathAction(catalog_file.absolute(), clear_content=True)
    expected_plan.add_action(reset_destination_action)

    _, _, merged_metadata_instance = load_distributed(metadata_file)
    merged_catalog_type, merged_catalog_alias = fs.get_stripped_contextual_model(
        catalog_file.absolute(), aliases_not_to_be_stripped=['metadata'])
    stripped_catalog_type, _ = fs.get_stripped_contextual_model(catalog_file.absolute())
    stripped_catalog = stripped_catalog_type.oscal_read(catalog_file)
    merged_catalog_dict = stripped_catalog.__dict__
    merged_catalog_dict['metadata'] = merged_metadata_instance
    merged_catalog = merged_catalog_type(**merged_catalog_dict)
    element = Element(merged_catalog)
    write_destination_action = WriteFileAction(catalog_file, element, content_type=content_type)
    expected_plan.add_action(write_destination_action)
    delete_element_action = RemovePathAction(metadata_file.absolute())
    expected_plan.add_action(delete_element_action)

    # Call merged()
    generated_plan = MergeCmd.merge(ElementPath('catalog.metadata'))

    # Assert the generated plan matches the expected plan'
    assert generated_plan == expected_plan


def test_merge_everything_into_catalog(testdata_dir, tmp_trestle_dir):
    """Test '$mycatalog$ trestle merge -e catalog.*' when metadata and catalog is already split."""
    # Assume we are running a command like below
    # trestle merge -e catalog.back-matter
    content_type = FileContentType.JSON
    fext = FileContentType.to_file_extension(content_type)

    # prepare trestle project dir with the file
    test_utils.ensure_trestle_config_dir(tmp_trestle_dir)

    test_data_source = testdata_dir / 'split_merge/step4_split_groups_array/catalogs'
    catalogs_dir = Path('catalogs/')
    mycatalog_dir = catalogs_dir / 'mycatalog'
    catalog_dir = mycatalog_dir / 'catalog'

    # Copy files from test/data/split_merge/step4
    shutil.rmtree(catalogs_dir)
    shutil.copytree(test_data_source, catalogs_dir)

    # Change directory to mycatalog_dir
    os.chdir(mycatalog_dir)
    catalog_file = Path(f'catalog{fext}')
    catalog_dir = Path('catalog/')

    assert catalog_file.exists()

    # Read files

    # Create hand-crafter merge plan
    expected_plan: Plan = Plan()

    reset_destination_action = CreatePathAction(catalog_file.absolute(), clear_content=True)
    expected_plan.add_action(reset_destination_action)

    _, _, merged_catalog_instance = load_distributed(catalog_file)

    element = Element(merged_catalog_instance)
    write_destination_action = WriteFileAction(catalog_file, element, content_type=content_type)
    expected_plan.add_action(write_destination_action)

    # Call merged()
    generated_plan = MergeCmd.merge(ElementPath('catalog.*'))

    # Assert the generated plan matches the expected plan'
    assert generated_plan == expected_plan

