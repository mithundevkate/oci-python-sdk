# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Configuration(object):
    """
    The set of MySQL variables to be used when deploying a MySQL Database Service DB System.
    """

    #: A constant which can be used with the type property of a Configuration.
    #: This constant has a value of "DEFAULT"
    TYPE_DEFAULT = "DEFAULT"

    #: A constant which can be used with the type property of a Configuration.
    #: This constant has a value of "CUSTOM"
    TYPE_CUSTOM = "CUSTOM"

    #: A constant which can be used with the lifecycle_state property of a Configuration.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Configuration.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new Configuration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Configuration.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Configuration.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this Configuration.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this Configuration.
        :type display_name: str

        :param shape_name:
            The value to assign to the shape_name property of this Configuration.
        :type shape_name: str

        :param type:
            The value to assign to the type property of this Configuration.
            Allowed values for this property are: "DEFAULT", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param time_created:
            The value to assign to the time_created property of this Configuration.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Configuration.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Configuration.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param variables:
            The value to assign to the variables property of this Configuration.
        :type variables: ConfigurationVariables

        :param parent_configuration_id:
            The value to assign to the parent_configuration_id property of this Configuration.
        :type parent_configuration_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Configuration.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Configuration.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'display_name': 'str',
            'shape_name': 'str',
            'type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'variables': 'ConfigurationVariables',
            'parent_configuration_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'display_name': 'displayName',
            'shape_name': 'shapeName',
            'type': 'type',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'variables': 'variables',
            'parent_configuration_id': 'parentConfigurationId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._description = None
        self._display_name = None
        self._shape_name = None
        self._type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._variables = None
        self._parent_configuration_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Configuration.
        The OCID of the Configuration.


        :return: The id of this Configuration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Configuration.
        The OCID of the Configuration.


        :param id: The id of this Configuration.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Configuration.
        OCID of the Compartment the Configuration exists in.


        :return: The compartment_id of this Configuration.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Configuration.
        OCID of the Compartment the Configuration exists in.


        :param compartment_id: The compartment_id of this Configuration.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this Configuration.
        User-provided data about the Configuration.


        :return: The description of this Configuration.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Configuration.
        User-provided data about the Configuration.


        :param description: The description of this Configuration.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this Configuration.
        The display name of the Configuration.


        :return: The display_name of this Configuration.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Configuration.
        The display name of the Configuration.


        :param display_name: The display_name of this Configuration.
        :type: str
        """
        self._display_name = display_name

    @property
    def shape_name(self):
        """
        **[Required]** Gets the shape_name of this Configuration.
        The name of the associated Shape.


        :return: The shape_name of this Configuration.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this Configuration.
        The name of the associated Shape.


        :param shape_name: The shape_name of this Configuration.
        :type: str
        """
        self._shape_name = shape_name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Configuration.
        The Configuration type, DEFAULT or CUSTOM.

        Allowed values for this property are: "DEFAULT", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this Configuration.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Configuration.
        The Configuration type, DEFAULT or CUSTOM.


        :param type: The type of this Configuration.
        :type: str
        """
        allowed_values = ["DEFAULT", "CUSTOM"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Configuration.
        The date and time the Configuration was created, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this Configuration.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Configuration.
        The date and time the Configuration was created, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this Configuration.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this Configuration.
        The date and time the Configuration was last updated, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this Configuration.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Configuration.
        The date and time the Configuration was last updated, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this Configuration.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Configuration.
        The current state of the Configuration.

        Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Configuration.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Configuration.
        The current state of the Configuration.


        :param lifecycle_state: The lifecycle_state of this Configuration.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def variables(self):
        """
        **[Required]** Gets the variables of this Configuration.

        :return: The variables of this Configuration.
        :rtype: ConfigurationVariables
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """
        Sets the variables of this Configuration.

        :param variables: The variables of this Configuration.
        :type: ConfigurationVariables
        """
        self._variables = variables

    @property
    def parent_configuration_id(self):
        """
        Gets the parent_configuration_id of this Configuration.
        The OCID of the Configuration from which this Configuration is
        \"derived\". This is entirely a metadata relationship. There is no
        relation between the values in this Configuration and its parent.


        :return: The parent_configuration_id of this Configuration.
        :rtype: str
        """
        return self._parent_configuration_id

    @parent_configuration_id.setter
    def parent_configuration_id(self, parent_configuration_id):
        """
        Sets the parent_configuration_id of this Configuration.
        The OCID of the Configuration from which this Configuration is
        \"derived\". This is entirely a metadata relationship. There is no
        relation between the values in this Configuration and its parent.


        :param parent_configuration_id: The parent_configuration_id of this Configuration.
        :type: str
        """
        self._parent_configuration_id = parent_configuration_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Configuration.
        Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Configuration.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Configuration.
        Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Configuration.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Configuration.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Configuration.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Configuration.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Configuration.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other