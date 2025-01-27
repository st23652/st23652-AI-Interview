from typing import Any

class PostGISAdapter:
    is_geometry: Any
    ewkb: Any
    srid: Any
    geography: Any
    def __init__(self, obj: Any, geography: bool = ...) -> None: ...
    def __conform__(self, proto: Any) -> Any: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def prepare(self, conn: Any) -> None: ...
    def getquoted(self) -> Any: ...
