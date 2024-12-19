from collections.abc import Sequence
from typing import Any

from django.db.models.sql.where import NothingNode
from typing_extensions import TypeAlias

_NodeChildren: TypeAlias = list[Node | NothingNode | Sequence[Any]]

class Node:
    children: _NodeChildren
    default: str
    connector: str
    negated: bool
    def __init__(
        self, children: _NodeChildren | None = ..., connector: str | None = ..., negated: bool = ...
    ) -> None: ...
    @classmethod
    def create(cls, children: _NodeChildren | None = ..., connector: str | None = ..., negated: bool = ...) -> Node: ...
    def copy(self) -> Node: ...
    def __copy__(self) -> Node: ...
    def __deepcopy__(self, memodict: dict[Any, Any]) -> Node: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __contains__(self, other: tuple[str, int]) -> bool: ...
    def __hash__(self) -> int: ...
    def add(self, data: Any, conn_type: str) -> Any: ...
    def negate(self) -> None: ...
