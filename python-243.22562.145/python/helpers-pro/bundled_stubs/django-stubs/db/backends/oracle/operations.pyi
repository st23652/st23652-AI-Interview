from typing import Any

from django.db.backends.base.operations import BaseDatabaseOperations
from django.db.backends.oracle.base import DatabaseWrapper

class DatabaseOperations(BaseDatabaseOperations):
    connection: DatabaseWrapper
    integer_field_ranges: Any
    set_operators: Any
    cast_char_field_without_max_length: str
    cast_data_types: Any
    def cache_key_culling_sql(self) -> str: ...
    def date_extract_sql(self, lookup_type: str, sql: str, params: Any) -> tuple[str, Any]: ...
    def date_trunc_sql(self, lookup_type: str, sql: str, params: Any, tzname: str | None = ...) -> tuple[str, Any]: ...
    def datetime_cast_date_sql(self, sql: str, params: Any, tzname: str | None) -> tuple[str, Any]: ...
    def datetime_cast_time_sql(self, sql: str, params: Any, tzname: str | None) -> tuple[str, Any]: ...
    def datetime_extract_sql(self, lookup_type: str, sql: str, params: Any, tzname: str | None) -> tuple[str, Any]: ...
    def datetime_trunc_sql(self, lookup_type: str, sql: str, params: Any, tzname: str | None) -> str: ...
    def time_trunc_sql(self, lookup_type: str, sql: str, params: Any, tzname: str | None = ...) -> str: ...
    def get_db_converters(self, expression: Any) -> list[Any]: ...
    def convert_textfield_value(self, value: Any, expression: Any, connection: Any) -> Any: ...
    def convert_binaryfield_value(self, value: Any, expression: Any, connection: Any) -> Any: ...
    def convert_booleanfield_value(self, value: Any, expression: Any, connection: Any) -> Any: ...
    def convert_datetimefield_value(self, value: Any, expression: Any, connection: Any) -> Any: ...
    def convert_datefield_value(self, value: Any, expression: Any, connection: Any) -> Any: ...
    def convert_timefield_value(self, value: Any, expression: Any, connection: Any) -> Any: ...
    def convert_uuidfield_value(self, value: Any, expression: Any, connection: Any) -> Any: ...
    @staticmethod
    def convert_empty_string(value: Any, expression: Any, connection: Any) -> Any: ...
    @staticmethod
    def convert_empty_bytes(value: Any, expression: Any, connection: Any) -> Any: ...
    def deferrable_sql(self) -> str: ...
    def fetch_returned_insert_columns(self, cursor: Any, returning_params: Any) -> Any: ...
    def field_cast_sql(self, db_type: Any, internal_type: Any) -> str: ...
    def no_limit_value(self) -> str | None: ...
    def limit_offset_sql(self, low_mark: Any, high_mark: Any) -> str: ...
    def last_executed_query(self, cursor: Any, sql: Any, params: Any) -> str: ...
    def last_insert_id(self, cursor: Any, table_name: Any, pk_name: Any) -> Any: ...
    def lookup_cast(self, lookup_type: str, internal_type: Any | None = ...) -> str: ...
    def max_in_list_size(self) -> int: ...
    def max_name_length(self) -> int: ...
    def pk_default_value(self) -> str: ...
    def prep_for_iexact_query(self, x: Any) -> str: ...
    def process_clob(self, value: Any) -> Any: ...
    def quote_name(self, name: str) -> str: ...
    def regex_lookup(self, lookup_type: str) -> str: ...
    def return_insert_columns(self, fields: Any) -> Any: ...
    def sequence_reset_by_name_sql(self, style: Any, sequences: Any) -> list[str]: ...
    def sequence_reset_sql(self, style: Any, model_list: Any) -> list[str]: ...
    def start_transaction_sql(self) -> str: ...
    def tablespace_sql(self, tablespace: Any, inline: bool = ...) -> str: ...
    def adapt_datefield_value(self, value: Any) -> Any: ...
    def adapt_datetimefield_value(self, value: Any) -> Any: ...
    def adapt_timefield_value(self, value: Any) -> Any: ...
    def combine_expression(self, connector: Any, sub_expressions: Any) -> Any: ...
    def bulk_insert_sql(self, fields: Any, placeholder_rows: Any) -> str: ...
    def subtract_temporals(self, internal_type: Any, lhs: Any, rhs: Any) -> Any: ...
    def bulk_batch_size(self, fields: Any, objs: Any) -> int: ...
    def conditional_expression_supported_in_where_clause(self, expression: Any) -> bool: ...
