# modified by fix_any.py
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
# generated by datamodel-codegen:
#   filename:  oscal_assessment-results_schema.json

from __future__ import annotations

from typing import List, Optional

from pydantic import Field
from trestle.core.base_model import OscalBaseModel
from trestle.oscal.assessment_results import Observation


class AssessmentResultsPartial(OscalBaseModel):
    observations: Optional[List[Observation]] = Field(None, min_items=1)
