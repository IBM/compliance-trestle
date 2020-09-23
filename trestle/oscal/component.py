# modified by fix_any.py
# generated by datamodel-codegen:
#   filename:  oscal_component_schema.json
#   timestamp: 2020-09-23T00:16:09+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyUrl, EmailStr, Field, constr

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


class IncorporatesComponent(OscalBaseModel):
    description: Description


class Value(OscalBaseModel):
    __root__: str


class ImportComponentDefinition(OscalBaseModel):
    href: str = Field(
        ...,
        description='A link to a resource that defines a set of components and/or capabilities to import into this collection.',
        title='Hyperlink Reference',
    )


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


class ImplementedRequirement(OscalBaseModel):
    uuid: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    control_id: Optional[str] = Field(
        None,
        alias='control-id',
        description='A reference to a control identifier.',
        title='Control Identifier Reference',
    )
    description: Optional[Description] = None
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    responsible_roles: Optional[Dict[str, ResponsibleRole]] = Field(None, alias='responsible-roles')
    set_parameters: Optional[Dict[str, SetParameter]] = Field(None, alias='set-parameters')
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


class ControlImplementation(OscalBaseModel):
    uuid: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A unique identifier for the set of implemented controls.',
        title='Control Implementation Set Identifier',
    )
    source: str = Field(
        ...,
        description='A URL reference to the source catalog or profile for which this component is implementing controls for.',
    )
    description: Description
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
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


class Capability(OscalBaseModel):
    name: str = Field(
        ...,
        description="The capability's human-readable name.",
        title='Capability Name',
    )
    description: Description
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    incorporates_components: Optional[Dict[str, IncorporatesComponent]] = Field(
        None, alias='incorporates-components'
    )
    control_implementations: Optional[List[ControlImplementation]] = Field(
        None, alias='control-implementations'
    )
    remarks: Optional[Remarks] = None


class Component(OscalBaseModel):
    name: str = Field(
        ...,
        description="The component's short, human-readable name.",
        title='Component Name',
    )
    component_type: str = Field(
        ...,
        alias='component-type',
        description='A category describing the purpose of the component.',
        title='Component Type',
    )
    title: Title
    description: Description
    properties: Optional[List[Prop]] = None
    links: Optional[List[Link]] = None
    responsible_parties: Optional[Dict[str, ResponsibleParty]] = Field(
        None, alias='responsible-parties'
    )
    control_implementations: Optional[List[ControlImplementation]] = Field(
        None, alias='control-implementations'
    )
    remarks: Optional[Remarks] = None


class ComponentDefinition(OscalBaseModel):
    metadata: Metadata
    import_component_definitions: Optional[List[ImportComponentDefinition]] = Field(
        None, alias='import-component-definitions'
    )
    components: Optional[Dict[str, Component]] = None
    capabilities: Optional[Dict[str, Capability]] = None
    back_matter: Optional[BackMatter] = Field(None, alias='back-matter')


class Model(OscalBaseModel):
    component_definition: ComponentDefinition = Field(..., alias='component-definition')
