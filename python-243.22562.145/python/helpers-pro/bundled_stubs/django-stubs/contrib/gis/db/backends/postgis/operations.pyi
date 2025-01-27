from typing import Any, Literal, MutableMapping

from django.contrib.gis.db.backends.base.operations import BaseSpatialOperations
from django.contrib.gis.db.backends.utils import SpatialOperator
from django.contrib.gis.db.models.fields import GeometryField
from django.contrib.gis.db.models.lookups import GISLookup
from django.db.backends.postgresql.operations import DatabaseOperations
from django.db.models import Func
from django.utils.functional import cached_property

BILATERAL: Literal["bilateral"]

class PostGISOperator(SpatialOperator):
    geography: Any
    raster: bool | Literal["bilateral"]
    def __init__(self, geography: bool = ..., raster: bool | Literal["bilateral"] = ..., **kwargs: Any) -> None: ...
    def check_raster(self, lookup: Any, template_params: Any) -> Any: ...
    def check_geography(
        self,
        lookup: GISLookup,
        template_params: MutableMapping[str, Any],
    ) -> MutableMapping[str, Any]: ...

class ST_Polygon(Func):
    function: str
    def __init__(self, expr: Any) -> None: ...
    @cached_property
    def output_field(self) -> GeometryField: ...

class PostGISOperations(BaseSpatialOperations, DatabaseOperations):
    name: str
    postgis: bool
    geography: bool
    geom_func_prefix: str
    Adapter: Any
    collect: Any
    extent: Any
    extent3d: Any
    length3d: Any
    makeline: Any
    perimeter3d: Any
    unionagg: Any
    gis_operators: Any
    unsupported_functions: Any
    select: str
    select_extent: Any
    @property
    def function_names(self) -> Any: ...
    @property
    def spatial_version(self) -> Any: ...
    def geo_db_type(self, f: Any) -> Any: ...
    def get_distance(self, f: Any, dist_val: Any, lookup_type: Any) -> Any: ...
    def get_geom_placeholder(self, f: Any, value: Any, compiler: Any) -> Any: ...
    def postgis_geos_version(self) -> Any: ...
    def postgis_lib_version(self) -> Any: ...
    def postgis_proj_version(self) -> Any: ...
    def postgis_version(self) -> Any: ...
    def postgis_full_version(self) -> Any: ...
    def postgis_version_tuple(self) -> Any: ...
    def proj_version_tuple(self) -> Any: ...
    def spatial_aggregate_name(self, agg_name: Any) -> Any: ...
    def geometry_columns(self) -> Any: ...
    def spatial_ref_sys(self) -> Any: ...
    def parse_raster(self, value: Any) -> Any: ...
    def distance_expr_for_lookup(self, lhs: Any, rhs: Any, **kwargs: Any) -> Any: ...
    def get_geometry_converter(self, expression: Any) -> Any: ...
    def get_area_att_for_field(self, field: Any) -> Any: ...
