# -*- mode:python; coding:utf-8 -*-
# Copyright (c) 2021 IBM Corp. All rights reserved.
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
"""Facilitate Tanium report to NIST OSCAL json transformation."""

import datetime
import logging
import uuid
from typing import Any, Dict, List, Union, ValuesView

from trestle.oscal.assessment_results import ControlSelection
from trestle.oscal.assessment_results import Finding
from trestle.oscal.assessment_results import Inventory
from trestle.oscal.assessment_results import LocalDefinitions
from trestle.oscal.assessment_results import Observation
from trestle.oscal.assessment_results import Property
from trestle.oscal.assessment_results import RelatedObservation
from trestle.oscal.assessment_results import Result
from trestle.oscal.assessment_results import ReviewedControls
from trestle.oscal.assessment_results import Subject

logger = logging.getLogger(__name__)

t_analysis = Dict[str, Any]
t_control = str
t_control_selection = ControlSelection
t_finding = Finding
t_inventory = Inventory
t_inventory_ref = str
t_ip = str
t_json = str
t_local_definitions = LocalDefinitions
t_observation = Observation
t_oscal = Union[str, Dict[str, Any]]
t_tanium_row = Dict[str, Any]
t_timestamp = str
t_resource = Dict[str, Any]
t_result = Result
t_reviewed_controls = ReviewedControls

t_inventory_map = Dict[t_ip, t_inventory]
t_observation_list = List[Observation]
t_findings_map = Dict[t_control, Any]


class RuleUse():
    """Represents one row of Tanium data."""

    def __init__(self, tanium_row: t_tanium_row, default_timestamp: t_timestamp) -> None:
        """Initialize given specified args."""
        logger.debug(f'tanium-row: {tanium_row}')
        keys = tanium_row.keys()
        for key in keys:
            if key.startswith('Comply'):
                key_comply = key
                break
        self.ip = tanium_row['IP Address']
        self.computer = tanium_row['Computer Name']
        self.count = tanium_row['Count']
        self.age = tanium_row['Age']
        self.benchmark = tanium_row[key_comply][0]['Benchmark']
        self.benchmark_version = tanium_row[key_comply][0]['Benchmark Version']
        self.profile = tanium_row[key_comply][0]['Profile']
        self.id = tanium_row[key_comply][0]['ID']
        self.result = tanium_row[key_comply][0]['Result']
        self.custom_id = tanium_row[key_comply][0]['Custom ID']
        self.version = tanium_row[key_comply][0]['Version']
        self.time = tanium_row[key_comply][0].get('Timestamp', default_timestamp)


class ResultsMgr():
    """Represents collection of data to be transformed into an AssessmentResult.results."""

    # the current time for consistent timestamping
    timestamp = datetime.datetime.utcnow().replace(microsecond=0).replace(tzinfo=datetime.timezone.utc).isoformat()

    @staticmethod
    def set_timestamp(value: str) -> None:
        """Set the default timestamp value."""
        datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S%z')
        ResultsMgr.timestamp = value

    @staticmethod
    def get_timestamp() -> str:
        """Get the default timestamp value."""
        return ResultsMgr.timestamp

    def __init__(self) -> None:
        """Initialize."""
        self.inventory_map: t_inventory_map = {}
        self.observation_list: t_observation_list = []
        self.findings_map: t_findings_map = {}

    @property
    def inventory(self) -> ValuesView[Inventory]:
        """OSCAL inventory."""
        return self.inventory_map.values()

    @property
    def observations(self) -> List[t_observation]:
        """OSCAL observations."""
        return self.observation_list

    @property
    def control_selections(self) -> List[t_control_selection]:
        """OSCAL control selections."""
        prop = []
        prop.append(ControlSelection())
        return prop

    def normalize(self, value: str) -> str:
        """Normalize result value."""
        result = None
        if value is not None:
            result = value.upper()
            if result not in ['PASS', 'FAIL']:
                result = 'ERROR'
        return result

    def aggregator(self, prev: str, curr: str) -> str:
        """Aggregate an overall result.

        If any FAIL then FAIL
        else if any ERROR then ERROR
        else any not PASS then ERROR
        else PASS
        """
        result = None
        nprev = self.normalize(prev)
        ncurr = self.normalize(curr)
        if nprev is None:
            result = ncurr
        elif 'FAIL' in [nprev, ncurr]:
            result = 'FAIL'
        elif 'ERROR' in [nprev, ncurr]:
            result = 'ERROR'
        elif nprev == 'PASS' and ncurr == 'PASS':
            result = 'PASS'
        else:
            result = 'ERROR'
        return result

    @property
    def findings(self) -> List[t_finding]:
        """OSCAL findings."""
        prop = []
        for control in self.findings_map.keys():
            aggregate = None
            related_observations = []
            finding = Finding(
                uuid=str(uuid.uuid4()), title=control, description=control, collected=ResultsMgr.timestamp
            )
            prop.append(finding)
            for rule in self.findings_map[control].keys():
                for rule_use in self.findings_map[control][rule]:
                    related_observations.append(RelatedObservation(observation_uuid=rule_use.observation.uuid))
                    aggregate = self.aggregator(aggregate, rule_use.result)
                    break
            props = [Property(name='result', value=aggregate, class_='STRVALUE')]
            finding.props = props
            logger.debug(f'{control}: {aggregate}')
            finding.related_observations = related_observations
        return prop

    @property
    def local_definitions(self) -> t_local_definitions:
        """OSCAL local definitions."""
        prop = LocalDefinitions()
        prop.inventory_items = list(self.inventory)
        return prop

    @property
    def reviewed_controls(self) -> t_reviewed_controls:
        """OSCAL reviewed controls."""
        prop = ReviewedControls(control_selections=self.control_selections)
        return prop

    @property
    def results(self) -> t_result:
        """OSCAL results."""
        prop = Result(
            uuid=str(uuid.uuid4()),
            title='Tanium',
            description='Tanium',
            start=ResultsMgr.timestamp,
            reviewed_controls=self.reviewed_controls,
            findings=self.findings,
            local_definitions=self.local_definitions,
            observations=self.observations
        )
        return prop

    @property
    def analysis(self) -> List[str]:
        """OSCAL statistics."""
        analysis = []
        analysis.append(f'inventory: {len(self.inventory)}')
        analysis.append(f'observations: {len(self.observations)}')
        analysis.append(f'findings: {len(self.findings_map)}')
        return analysis

    @property
    def json(self) -> t_json:
        """OSCAL results as json."""
        return self.results.json(exclude_none=True, by_alias=True, indent=2)

    def get_inventroy_ref(self, ip: t_ip) -> t_inventory_ref:
        """Get inventory reference for specified IP."""
        return self.inventory_map[ip].uuid

    def inventory_extract(self, rule_use: RuleUse) -> None:
        """Extract inventory from Tanium row."""
        if rule_use.ip not in self.inventory_map.keys():
            inventory = Inventory(uuid=str(uuid.uuid4()), description='?')
            inventory.props = [
                Property(name='target', value=rule_use.computer, class_='computer-name'),
                Property(name='target', value=rule_use.ip, class_='computer-ip'),
            ]
            self.inventory_map[rule_use.ip] = inventory
        rule_use.inventory = self.inventory_map[rule_use.ip]

    def observation_extract(self, rule_use: RuleUse) -> None:
        """Extract observation from Tanium row."""
        observation = Observation(uuid=str(uuid.uuid4()), description=rule_use.id, methods=['TEST-AUTOMATED'])
        subject = Subject(uuid_ref=self.get_inventroy_ref(rule_use.ip), type='inventory-item')
        observation.subjects = [subject]
        if rule_use.id.startswith('xccdf'):
            ns = 'dns://xccdf'
            props = [
                Property(name='rule', value=rule_use.id, ns=ns, class_='id'),
                Property(name='result', value=rule_use.result, ns=ns, class_='result'),
                Property(name='time', value=rule_use.time, ns=ns, class_='timestamp'),
            ]
        else:
            props = [
                Property(name='rule', value=rule_use.id, class_='id'),
                Property(name='result', value=rule_use.result, class_='result'),
                Property(name='time', value=rule_use.time, class_='timestamp'),
            ]
        observation.props = props
        self.observation_list.append(observation)
        rule_use.observation = observation

    def finding_extract(self, rule_use: RuleUse) -> None:
        """Extract finding from Tanium row."""
        control = rule_use.custom_id
        if control not in self.findings_map.keys():
            self.findings_map[control] = {}
        rule = rule_use.id
        if rule not in self.findings_map[control].keys():
            self.findings_map[control][rule] = []
        self.findings_map[control][rule].append(rule_use)

    def ingest(self, tanium: t_tanium_row) -> None:
        """Process one row of Tanium."""
        rule_use = RuleUse(tanium, ResultsMgr.timestamp)
        self.inventory_extract(rule_use)
        self.observation_extract(rule_use)
        self.finding_extract(rule_use)
