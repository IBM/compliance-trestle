# modified by fix_any.py
# generated by datamodel-codegen:
#   filename:  oscal_ssp_schema.json
#   timestamp: 2020-09-23T03:11:55+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyUrl, EmailStr, Field, conint, constr
from trestle.core.base_model import OscalBaseModel


class Link(OscalBaseModel):
    href: str = Field(
        ...,
        description='A link to a document or document fragment (actual, nominal or projected)',
        title='hypertext reference',
    )
    rel: Optional[str] = Field(
        None,
        description="Describes the type of relationship provided by the link. This can be an indicator of the link's purpose.",
        title='Relation',
    )
    media_type: Optional[str] = Field(
        None,
        alias='media-type',
        description='Describes the media type of the linked resource',
        title='Media type',
    )
    text: str


class Published(OscalBaseModel):
    __root__: datetime


class LastModified(OscalBaseModel):
    __root__: datetime


class Version(OscalBaseModel):
    __root__: str


class OscalVersion(OscalBaseModel):
    __root__: str


class DocId(OscalBaseModel):
    type: str = Field(..., description='Qualifies the kind of document identifier.')
    identifier: str


class Prop(OscalBaseModel):
    name: str = Field(
        ...,
        description='Identifying the purpose and intended use of the property, part or other object.',
        title='Name',
    )
    uuid: Optional[
        constr(
            regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
        )
    ] = Field(
        None,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    ns: Optional[str] = Field(
        None, description='A namespace qualifying the name.', title='Namespace'
    )
    class_: Optional[str] = Field(
        None,
        alias='class',
        description='Indicating the type or classification of the containing object',
        title='Class',
    )
    value: str


class LocationUuid(OscalBaseModel):
    __root__: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    )


class Type(Enum):
    person = 'person'
    organization = 'organization'


class PartyUuid(OscalBaseModel):
    __root__: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    )


class ExternalId(OscalBaseModel):
    type: str = Field(
        ...,
        description='Indicating the type of identifier, address, email or other data item.',
        title='Type',
    )
    id: str


class MemberOfOrganization(OscalBaseModel):
    __root__: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    )


class PartyName(OscalBaseModel):
    __root__: str


class ShortName(OscalBaseModel):
    __root__: str


class AddrLine(OscalBaseModel):
    __root__: str


class City(OscalBaseModel):
    __root__: str


class State(OscalBaseModel):
    __root__: str


class PostalCode(OscalBaseModel):
    __root__: str


class Country(OscalBaseModel):
    __root__: str


class Email(OscalBaseModel):
    __root__: EmailStr


class Phone(OscalBaseModel):
    type: Optional[str] = Field(None, description='Indicates the type of phone number.')
    number: str


class Url(OscalBaseModel):
    __root__: AnyUrl


class Desc(OscalBaseModel):
    __root__: str


class Text(OscalBaseModel):
    __root__: str


class Biblio(OscalBaseModel):
    pass


class Citation(OscalBaseModel):
    text: Text
    properties: Optional[List[Prop]] = None
    biblio: Optional[Biblio] = None


class Hash(OscalBaseModel):
    algorithm: str = Field(
        ..., description='Method by which a hash is derived', title='Hash algorithm'
    )
    value: str


class Title(OscalBaseModel):
    __root__: str


class Base64(OscalBaseModel):
    filename: Optional[str] = Field(
        None,
        description='Name of the file before it was encoded as Base64 to be embedded in a resource. This is the name that will be assigned to the file when the file is decoded.',
        title='File Name',
    )
    media_type: Optional[str] = Field(
        None,
        alias='media-type',
        description='Describes the media type of the linked resource',
        title='Media type',
    )
    value: str


class Description(OscalBaseModel):
    __root__: str


class Remarks(OscalBaseModel):
    __root__: str


class Value(OscalBaseModel):
    __root__: str


class ImportProfile(OscalBaseModel):
    href: str = Field(
        ...,
        description='A link to a document or document fragment (actual, nominal or projected)',
        title='hypertext reference',
    )
    remarks: Optional[Remarks] = None


class SystemId(OscalBaseModel):
    identifier_type: Optional[AnyUrl] = Field(
        None,
        alias='identifier-type',
        description='Identifies the identification system from which the provided identifier was assigned.',
        title='Identification System Type',
    )
    id: str


class SystemName(OscalBaseModel):
    __root__: str


class SystemNameShort(OscalBaseModel):
    __root__: str


class SecuritySensitivityLevel(Enum):
    low = 'low'
    moderate = 'moderate'
    high = 'high'


class InformationTypeId(OscalBaseModel):
    id: str


class Base(Enum):
    fips_199_low = 'fips-199-low'
    fips_199_moderate = 'fips-199-moderate'
    fips_199_high = 'fips-199-high'


class Selected(Enum):
    fips_199_low = 'fips-199-low'
    fips_199_moderate = 'fips-199-moderate'
    fips_199_high = 'fips-199-high'


class AdjustmentJustification(OscalBaseModel):
    __root__: str


class SecurityObjectiveConfidentiality(Enum):
    fips_199_low = 'fips-199-low'
    fips_199_moderate = 'fips-199-moderate'
    fips_199_high = 'fips-199-high'


class SecurityObjectiveIntegrity(Enum):
    fips_199_low = 'fips-199-low'
    fips_199_moderate = 'fips-199-moderate'
    fips_199_high = 'fips-199-high'


class SecurityObjectiveAvailability(Enum):
    fips_199_low = 'fips-199-low'
    fips_199_moderate = 'fips-199-moderate'
    fips_199_high = 'fips-199-high'


class State1(Enum):
    operational = 'operational'
    under_development = 'under-development'
    under_major_modification = 'under-major-modification'
    disposition = 'disposition'
    other = 'other'


class Status(OscalBaseModel):
    state: State1 = Field(
        ..., description='The current operating status.', title='State'
    )
    remarks: Optional[Remarks] = None


class DateAuthorized(OscalBaseModel):
    __root__: constr(
        regex='^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))(Z|[+-][0-9]{2}:[0-9]{2})?$'
    )


class Caption(OscalBaseModel):
    __root__: str


class RoleId(OscalBaseModel):
    __root__: str


class FunctionPerformed(OscalBaseModel):
    __root__: str


class Transport(Enum):
    TCP = 'TCP'
    UDP = 'UDP'


class PortRange(OscalBaseModel):
    start: Optional[conint(ge=0, multiple_of=1)] = Field(
        None,
        description='Indicates the starting port number in a port range',
        title='Start',
    )
    end: Optional[conint(ge=0, multiple_of=1)] = Field(
        None,
        description='Indicates the ending port number in a port range',
        title='End',
    )
    transport: Optional[Transport] = Field(
        None, description='Indicates the transport type.', title='Transport'
    )


class Purpose(OscalBaseModel):
    __root__: str


class SystemInventory(OscalBaseModel):
    inventory_items: Dict[str, Any] = Field(..., alias='inventory-items')
    remarks: Optional[Remarks] = None


class Annotation(OscalBaseModel):
    name: str = Field(
        ...,
        description='Identifying the purpose and intended use of the property, part or other object.',
        title='Name',
    )
    uuid: Optional[
        constr(
            regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
        )
    ] = Field(
        None,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    ns: Optional[str] = Field(
        None, description='A namespace qualifying the name.', title='Namespace'
    )
    value: Optional[str] = Field(
        None, description='Indicates the value of the characteristic.', title='Value'
    )
    remarks: Optional[Remarks] = None


class ResponsibleRole(OscalBaseModel):
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    party_uuids: Optional[List[PartyUuid]] = Field(None, alias='party-uuids')
    remarks: Optional[Remarks] = None


class ByComponent(OscalBaseModel):
    uuid: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    description: Description
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    responsible_roles: Optional[Dict[str, ResponsibleRole]] = Field(None, alias='responsible-roles')
    parameter_settings: Optional[Dict[str, ParameterSetting]] = Field(
        None, alias='parameter-settings'
    )
    remarks: Optional[Remarks] = None


class Statement(OscalBaseModel):
    uuid: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    description: Optional[Description] = None
    properties: Optional[List[Prop]] = None
    annotations: Optional[Union[Annotation, Annotation]] = None
    links: Optional[List[Link]] = None
    responsible_roles: Optional[Dict[str, ResponsibleRole]] = Field(None, alias='responsible-roles')
    by_components: Optional[Dict[str, ByComponent]] = Field(None, alias='by-components')
    remarks: Optional[Remarks] = None


class Revision(OscalBaseModel):
    title: Optional[Title] = None
    published: Optional[Published] = None
    last_modified: Optional[LastModified] = Field(None, alias='last-modified')
    version: Optional[Version] = None
    oscal_version: Optional[OscalVersion] = Field(None, alias='oscal-version')
    properties: Optional[List[Prop]] = None
    links: Optional[List[Link]] = None
    remarks: Optional[Remarks] = None


class Rlink(OscalBaseModel):
    href: str = Field(
        ...,
        description='A link to a document or document fragment (actual, nominal or projected)',
        title='hypertext reference',
    )
    media_type: Optional[str] = Field(
        None,
        alias='media-type',
        description='Describes the media type of the linked resource',
        title='Media type',
    )
    hashes: Optional[List[Hash]] = None


class Address(OscalBaseModel):
    type: Optional[str] = Field(None, description='Indicates the type of address.')
    postal_address: Optional[List[AddrLine]] = Field(None, alias='postal-address')
    city: Optional[City] = None
    state: Optional[State] = None
    postal_code: Optional[PostalCode] = Field(None, alias='postal-code')
    country: Optional[Country] = None


class Resource(OscalBaseModel):
    uuid: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    title: Optional[Title] = None
    desc: Optional[Desc] = None
    properties: Optional[List[Prop]] = None
    document_ids: Optional[List[DocId]] = Field(None, alias='document-ids')
    citation: Optional[Citation] = None
    rlinks: Optional[List[Rlink]] = None
    attachments: Optional[List[Base64]] = None
    remarks: Optional[Remarks] = None


class Role(OscalBaseModel):
    id: str = Field(
        ...,
        description='Unique identifier of the containing object',
        title='Identifier',
    )
    title: Title
    short_name: Optional[ShortName] = Field(None, alias='short-name')
    desc: Optional[Desc] = None
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    remarks: Optional[Remarks] = None


class ResponsibleParty(OscalBaseModel):
    party_uuids: List[PartyUuid] = Field(..., alias='party-uuids')
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    remarks: Optional[Remarks] = None


class SetParameter(OscalBaseModel):
    value: Value


class ConfidentialityImpact(OscalBaseModel):
    properties: Optional[List[Prop]] = None
    base: Base
    selected: Optional[Selected] = None
    adjustment_justification: Optional[AdjustmentJustification] = Field(
        None, alias='adjustment-justification'
    )


class IntegrityImpact(OscalBaseModel):
    properties: Optional[List[Prop]] = None
    base: Base
    selected: Optional[Selected] = None
    adjustment_justification: Optional[AdjustmentJustification] = Field(
        None, alias='adjustment-justification'
    )


class AvailabilityImpact(OscalBaseModel):
    properties: Optional[List[Prop]] = None
    base: Base
    selected: Optional[Selected] = None
    adjustment_justification: Optional[AdjustmentJustification] = Field(
        None, alias='adjustment-justification'
    )


class SecurityImpactLevel(OscalBaseModel):
    security_objective_confidentiality: Optional[
        SecurityObjectiveConfidentiality
    ] = Field(None, alias='security-objective-confidentiality')
    security_objective_integrity: Optional[SecurityObjectiveIntegrity] = Field(
        None, alias='security-objective-integrity'
    )
    security_objective_availability: Optional[SecurityObjectiveAvailability] = Field(
        None, alias='security-objective-availability'
    )


class LeveragedAuthorization(OscalBaseModel):
    uuid: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    title: Title
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    party_uuid: PartyUuid = Field(..., alias='party-uuid')
    date_authorized: DateAuthorized = Field(..., alias='date-authorized')
    remarks: Optional[Remarks] = None


class Diagram(OscalBaseModel):
    description: Optional[Description] = None
    properties: Optional[List[Prop]] = None
    links: Optional[List[Link]] = None
    caption: Optional[Caption] = None
    remarks: Optional[Remarks] = None


class AuthorizationBoundary(OscalBaseModel):
    description: Description
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    diagrams: Optional[Dict[str, Diagram]] = None
    remarks: Optional[Remarks] = None


class NetworkArchitecture(OscalBaseModel):
    description: Description
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    diagrams: Optional[Dict[str, Diagram]] = None
    remarks: Optional[Remarks] = None


class DataFlow(OscalBaseModel):
    description: Description
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    diagrams: Optional[Dict[str, Diagram]] = None
    remarks: Optional[Remarks] = None


class Component(OscalBaseModel):
    component_type: str = Field(
        ...,
        alias='component-type',
        description='A category describing the purpose of the component.',
        title='Component Type',
    )
    title: Title
    description: Description
    purpose: Optional[Purpose] = None
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    status: Status
    responsible_roles: Optional[Dict[str, ResponsibleRole]] = Field(None, alias='responsible-roles')
    protocols: Optional[List[Protocol]] = None
    remarks: Optional[Remarks] = None


class SystemImplementation(OscalBaseModel):
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    leveraged_authorizations: Optional[List[LeveragedAuthorization]] = Field(
        None, alias='leveraged-authorizations'
    )
    users: Dict[str, Any]
    components: Optional[Dict[str, Component]] = None
    system_inventory: Optional[SystemInventory] = Field(None, alias='system-inventory')
    remarks: Optional[Remarks] = None


class AuthorizedPrivilege(OscalBaseModel):
    title: Title
    description: Optional[Description] = None
    functions_performed: List[FunctionPerformed] = Field(
        ..., alias='functions-performed'
    )


class Protocol(OscalBaseModel):
    uuid: Optional[
        constr(
            regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
        )
    ] = Field(
        None,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    name: str = Field(..., description='The short name of the protocol (e.g., TLS).')
    title: Optional[Title] = None
    port_ranges: Optional[List[PortRange]] = Field(None, alias='port-ranges')


class ImplementedComponent(OscalBaseModel):
    use: Optional[str] = Field(
        None, description='The type of implementation', title='Implementation Use Type'
    )
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    responsible_parties: Optional[Dict[str, ResponsibleParty]] = Field(
        None, alias='responsible-parties'
    )
    remarks: Optional[Remarks] = None


class InventoryItem(OscalBaseModel):
    asset_id: str = Field(
        ...,
        alias='asset-id',
        description='Organizational asset identifier that is unique in the context of the system. This may be a reference to the identifier used in an asset tracking system or a vulnerability scanning tool.',
        title='Asset Identifier',
    )
    description: Description
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    responsible_parties: Optional[Dict[str, ResponsibleParty]] = Field(
        None, alias='responsible-parties'
    )
    implemented_components: Optional[Dict[str, ImplementedComponent]] = Field(
        None, alias='implemented-components'
    )
    remarks: Optional[Remarks] = None


class ImplementedRequirement(OscalBaseModel):
    uuid: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    control_id: str = Field(
        ...,
        alias='control-id',
        description='A reference to a control identifier.',
        title='Control Identifier Reference',
    )
    description: Optional[Description] = None
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    by_components: Optional[Dict[str, ByComponent]] = Field(None, alias='by-components')
    responsible_roles: Optional[Dict[str, ResponsibleRole]] = Field(None, alias='responsible-roles')
    parameter_settings: Optional[Dict[str, ParameterSetting]] = Field(
        None, alias='parameter-settings'
    )
    statements: Optional[Dict[str, Statement]] = None
    remarks: Optional[Remarks] = None


class BackMatter(OscalBaseModel):
    resources: Optional[List[Resource]] = None


class Location(OscalBaseModel):
    uuid: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    title: Optional[Title] = None
    address: Address
    email_addresses: Optional[List[Email]] = Field(None, alias='email-addresses')
    telephone_numbers: Optional[List[Phone]] = Field(None, alias='telephone-numbers')
    URLs: Optional[List[Url]] = None
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    remarks: Optional[Remarks] = None


class Party(OscalBaseModel):
    uuid: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    type: Type = Field(
        ...,
        description='A category describing the kind of party the object describes.',
        title='Party Type',
    )
    party_name: PartyName = Field(..., alias='party-name')
    short_name: Optional[ShortName] = Field(None, alias='short-name')
    external_ids: Optional[List[ExternalId]] = Field(None, alias='external-ids')
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    addresses: Optional[List[Address]] = None
    email_addresses: Optional[List[Email]] = Field(None, alias='email-addresses')
    telephone_numbers: Optional[List[Phone]] = Field(None, alias='telephone-numbers')
    member_of_organizations: Optional[List[MemberOfOrganization]] = Field(
        None, alias='member-of-organizations'
    )
    location_uuids: Optional[List[LocationUuid]] = Field(None, alias='location-uuids')
    remarks: Optional[Remarks] = None


class InformationType(OscalBaseModel):
    uuid: Optional[
        constr(
            regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
        )
    ] = Field(
        None,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    title: Title
    description: Description
    information_type_ids: Optional[Dict[str, InformationTypeId]] = Field(
        None, alias='information-type-ids'
    )
    properties: Optional[List[Prop]] = None
    confidentiality_impact: ConfidentialityImpact = Field(
        ..., alias='confidentiality-impact'
    )
    integrity_impact: IntegrityImpact = Field(..., alias='integrity-impact')
    availability_impact: AvailabilityImpact = Field(..., alias='availability-impact')


class User(OscalBaseModel):
    title: Optional[Title] = None
    short_name: Optional[ShortName] = Field(None, alias='short-name')
    description: Optional[Description] = None
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    role_ids: List[RoleId] = Field(..., alias='role-ids')
    authorized_privileges: Optional[List[AuthorizedPrivilege]] = Field(
        None, alias='authorized-privileges'
    )
    remarks: Optional[Remarks] = None


class ControlImplementation(OscalBaseModel):
    description: Description
    implemented_requirements: List[ImplementedRequirement] = Field(
        ..., alias='implemented-requirements'
    )


class Metadata(OscalBaseModel):
    title: Title
    published: Optional[Published] = None
    last_modified: LastModified = Field(..., alias='last-modified')
    version: Version
    oscal_version: OscalVersion = Field(..., alias='oscal-version')
    revision_history: Optional[List[Revision]] = Field(None, alias='revision-history')
    document_ids: Optional[List[DocId]] = Field(None, alias='document-ids')
    properties: Optional[List[Prop]] = None
    links: Optional[List[Link]] = None
    roles: Optional[List[Role]] = None
    locations: Optional[List[Location]] = None
    parties: Optional[List[Party]] = None
    responsible_parties: Optional[Dict[str, ResponsibleParty]] = Field(
        None, alias='responsible-parties'
    )
    remarks: Optional[Remarks] = None


class SystemInformation(OscalBaseModel):
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    information_types: List[InformationType] = Field(..., alias='information-types')


class SystemCharacteristics(OscalBaseModel):
    system_ids: List[SystemId] = Field(..., alias='system-ids')
    system_name: SystemName = Field(..., alias='system-name')
    system_name_short: Optional[SystemNameShort] = Field(
        None, alias='system-name-short'
    )
    description: Description
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    date_authorized: Optional[DateAuthorized] = Field(None, alias='date-authorized')
    security_sensitivity_level: SecuritySensitivityLevel = Field(
        ..., alias='security-sensitivity-level'
    )
    system_information: SystemInformation = Field(..., alias='system-information')
    security_impact_level: SecurityImpactLevel = Field(
        ..., alias='security-impact-level'
    )
    status: Status
    authorization_boundary: AuthorizationBoundary = Field(
        ..., alias='authorization-boundary'
    )
    network_architecture: Optional[NetworkArchitecture] = Field(
        None, alias='network-architecture'
    )
    data_flow: Optional[DataFlow] = Field(None, alias='data-flow')
    responsible_parties: Optional[Dict[str, ResponsibleParty]] = Field(
        None, alias='responsible-parties'
    )
    remarks: Optional[Remarks] = None


class SystemSecurityPlan(OscalBaseModel):
    uuid: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    metadata: Metadata
    import_profile: ImportProfile = Field(..., alias='import-profile')
    system_characteristics: SystemCharacteristics = Field(
        ..., alias='system-characteristics'
    )
    system_implementation: SystemImplementation = Field(
        ..., alias='system-implementation'
    )
    control_implementation: ControlImplementation = Field(
        ..., alias='control-implementation'
    )
    back_matter: Optional[BackMatter] = Field(None, alias='back-matter')


class Model(OscalBaseModel):
    system_security_plan: SystemSecurityPlan = Field(..., alias='system-security-plan')
