from typing import Any, AnyStr

from django.contrib.gis.gdal import CoordTransform, SpatialReference
from django.contrib.gis.gdal.base import GDALBase
from django.contrib.gis.gdal.envelope import Envelope
from django.contrib.gis.gdal.geomtype import OGRGeomType
from django.contrib.gis.geos import GEOSGeometry

class OGRGeometry(GDALBase):
    destructor: Any
    ptr: Any
    srs: SpatialReference | None
    def __init__(self, geom_input: Any, srs: SpatialReference | None = ...) -> None: ...
    @classmethod
    def from_bbox(cls, bbox: tuple[float, float, float, float]) -> OGRGeometry: ...
    @staticmethod
    def from_json(geom_input: AnyStr) -> OGRGeometry: ...
    @classmethod
    def from_gml(cls, gml_string: AnyStr) -> OGRGeometry: ...
    def __or__(self, other: OGRGeometry) -> OGRGeometry: ...
    def __and__(self, other: OGRGeometry) -> OGRGeometry: ...
    def __sub__(self, other: OGRGeometry) -> OGRGeometry: ...
    def __xor__(self, other: OGRGeometry) -> OGRGeometry: ...
    def __eq__(self, other: object) -> bool: ...
    @property
    def dimension(self) -> int: ...
    coord_dim: int
    @property
    def geom_count(self) -> int: ...
    @property
    def point_count(self) -> int: ...
    @property
    def num_points(self) -> int: ...
    @property
    def num_coords(self) -> int: ...
    @property
    def geom_type(self) -> OGRGeomType: ...
    @property
    def geom_name(self) -> str: ...
    @property
    def area(self) -> float: ...
    @property
    def envelope(self) -> Envelope: ...
    @property
    def empty(self) -> bool: ...
    @property
    def extent(self) -> tuple[float, float, float, float]: ...
    srid: int | None
    @property
    def geos(self) -> GEOSGeometry: ...
    @property
    def gml(self) -> str: ...
    @property
    def hex(self) -> bytes: ...
    @property
    def json(self) -> str: ...
    geojson: str
    @property
    def kml(self) -> str: ...
    @property
    def wkb_size(self) -> int: ...
    @property
    def wkb(self) -> memoryview: ...
    @property
    def wkt(self) -> str: ...
    @property
    def ewkt(self) -> str: ...
    def clone(self) -> Any: ...
    def close_rings(self) -> None: ...
    def transform(self, coord_trans: CoordTransform | SpatialReference | str | int, clone: bool = ...) -> Any: ...
    def intersects(self, other: OGRGeometry) -> bool: ...
    def equals(self, other: OGRGeometry) -> bool: ...
    def disjoint(self, other: OGRGeometry) -> bool: ...
    def touches(self, other: OGRGeometry) -> bool: ...
    def crosses(self, other: OGRGeometry) -> bool: ...
    def within(self, other: OGRGeometry) -> bool: ...
    def contains(self, other: OGRGeometry) -> bool: ...
    def overlaps(self, other: OGRGeometry) -> bool: ...
    @property
    def boundary(self) -> OGRGeometry: ...
    @property
    def convex_hull(self) -> OGRGeometry: ...
    def difference(self, other: OGRGeometry) -> OGRGeometry: ...
    def intersection(self, other: OGRGeometry) -> OGRGeometry: ...
    def sym_difference(self, other: OGRGeometry) -> OGRGeometry: ...
    def union(self, other: OGRGeometry) -> OGRGeometry: ...

class Point(OGRGeometry):
    @property
    def x(self) -> float: ...
    @property
    def y(self) -> float: ...
    @property
    def z(self) -> float | None: ...
    @property
    def coords(self) -> tuple[float, float] | tuple[float, float, float]: ...
    @property
    def tuple(self) -> tuple[float, float] | tuple[float, float, float]: ...

class LineString(OGRGeometry):
    def __getitem__(self, index: int) -> tuple[float, ...]: ...
    def __len__(self) -> int: ...
    @property
    def tuple(self) -> tuple[tuple[float, ...]]: ...
    coords: Any
    @property
    def x(self) -> list[float]: ...
    @property
    def y(self) -> list[float]: ...
    @property
    def z(self) -> list[float] | None: ...

class LinearRing(LineString): ...

class Polygon(OGRGeometry):
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> OGRGeometry: ...
    @property
    def shell(self) -> OGRGeometry: ...
    exterior_ring: OGRGeometry
    @property
    def coords(self) -> tuple[tuple[tuple[float, ...]]]: ...
    @property
    def tuple(self) -> tuple[tuple[tuple[float, ...]]]: ...
    @property
    def point_count(self) -> int: ...
    @property
    def centroid(self) -> Point: ...

class GeometryCollection(OGRGeometry):
    def __getitem__(self, index: int) -> OGRGeometry: ...
    def __len__(self) -> int: ...
    def add(self, geom: OGRGeometry | str) -> None: ...
    @property
    def point_count(self) -> int: ...
    @property
    def coords(self) -> tuple[Any, ...]: ...
    @property
    def tuple(self) -> tuple[Any, ...]: ...

class MultiPoint(GeometryCollection): ...
class MultiLineString(GeometryCollection): ...
class MultiPolygon(GeometryCollection): ...

GEO_CLASSES: Any
