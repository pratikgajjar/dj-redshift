from abc import ABC
from copy import deepcopy

from django.contrib.postgres.fields.jsonb import JSONField
from django_redshift_backend.base import (
    DatabaseSchemaEditor as OrigDatabaseSchemaEditor,
    DatabaseWrapper as OrigDatabaseWrapper
)

"""
To override inbuilt postgres data types
from django.db import models <- One of the data type from this module
"""
new_redshift_data_types_up = {
    "UUIDField": "varchar(40)",
}

"""
Use custom class to override custom field
Ex. Gis field, django contrib field. 
"""


class RedshiftJson(JSONField):
    def db_type(self, connection):
        return 'SUPER'


class CustomDatabaseSchemaEditor(OrigDatabaseSchemaEditor, ABC):

    def column_sql(self, model, field, include_default=False):
        field.null = True
        field.primary_key = False
        if issubclass(RedshiftJson, field.__class__):
            field.db_parameters = RedshiftJson(blank=True).db_parameters
        return super().column_sql(model, field, include_default)


class DatabaseWrapper(OrigDatabaseWrapper, ABC):
    SchemaEditorClass = CustomDatabaseSchemaEditor

    data_types = deepcopy(OrigDatabaseWrapper.data_types)
    data_types.update(new_redshift_data_types_up)
