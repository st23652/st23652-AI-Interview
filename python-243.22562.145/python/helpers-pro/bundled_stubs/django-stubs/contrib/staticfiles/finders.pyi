from collections.abc import Iterable, Iterator, Sequence
from typing import Any, Literal, overload

from django.core.checks.messages import CheckMessage
from django.core.files.storage import FileSystemStorage, Storage

searched_locations: Any

class BaseFinder:
    def check(self, **kwargs: Any) -> list[CheckMessage]: ...
    @overload
    def find(self, path: str, all: Literal[False] = ...) -> str | None: ...
    @overload
    def find(self, path: str, all: Literal[True]) -> list[str]: ...
    def list(self, ignore_patterns: Iterable[str] | None) -> Iterable[Any]: ...

class FileSystemFinder(BaseFinder):
    locations: list[tuple[str, str]]
    storages: dict[str, Any]
    def __init__(self, app_names: Sequence[str] | None = ..., *args: Any, **kwargs: Any) -> None: ...
    def find_location(self, root: str, path: str, prefix: str | None = ...) -> str | None: ...
    @overload
    def find(self, path: str, all: Literal[False] = ...) -> str | None: ...
    @overload
    def find(self, path: str, all: Literal[True]) -> list[str]: ...
    def list(self, ignore_patterns: Iterable[str] | None) -> Iterable[Any]: ...

class AppDirectoriesFinder(BaseFinder):
    storage_class: type[FileSystemStorage]
    source_dir: str
    apps: list[str]
    storages: dict[str, FileSystemStorage]
    def __init__(self, app_names: Iterable[str] | None = ..., *args: Any, **kwargs: Any) -> None: ...
    def find_in_app(self, app: str, path: str) -> str | None: ...
    @overload
    def find(self, path: str, all: Literal[False] = ...) -> str | None: ...
    @overload
    def find(self, path: str, all: Literal[True]) -> list[str]: ...
    def list(self, ignore_patterns: Iterable[str] | None) -> Iterable[Any]: ...

class BaseStorageFinder(BaseFinder):
    storage: Storage
    def __init__(self, storage: Storage | None = ..., *args: Any, **kwargs: Any) -> None: ...
    @overload
    def find(self, path: str, all: Literal[False] = ...) -> str | None: ...
    @overload
    def find(self, path: str, all: Literal[True]) -> list[str]: ...
    def list(self, ignore_patterns: Iterable[str] | None) -> Iterable[Any]: ...

class DefaultStorageFinder(BaseStorageFinder):
    storage: Storage
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

@overload
def find(path: str, all: Literal[False] = ...) -> str | None: ...
@overload
def find(path: str, all: Literal[True]) -> list[str]: ...
def get_finders() -> Iterator[BaseFinder]: ...
def get_finder(import_path: str) -> BaseFinder: ...
