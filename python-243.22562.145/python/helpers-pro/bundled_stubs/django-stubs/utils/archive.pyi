from collections.abc import Iterable, Sequence
from types import TracebackType
from typing import Any

from typing_extensions import Self

class ArchiveException(Exception): ...
class UnrecognizedArchiveFormat(ArchiveException): ...

def extract(path: str, to_path: str) -> None: ...

class Archive:
    def __init__(self, file: str) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None: ...
    def extract(self, to_path: str) -> None: ...
    def list(self) -> None: ...
    def close(self) -> None: ...

class BaseArchive:
    def split_leading_dir(self, path: str) -> Sequence[str]: ...
    def has_leading_dir(self, paths: Iterable[str]) -> bool: ...
    def target_filename(self, to_path: str, name: str) -> str: ...
    def extract(self, to_path: str) -> None: ...
    def list(self, *args: Any, **kwargs: Any) -> None: ...

class TarArchive(BaseArchive):
    def __init__(self, file: str) -> None: ...
    def list(self, *args: Any, **kwargs: Any) -> None: ...
    def close(self) -> None: ...
    def extract(self, to_path: str) -> None: ...

class ZipArchive(BaseArchive):
    def __init__(self, file: str) -> None: ...
    def list(self, *args: Any, **kwargs: Any) -> None: ...
    def extract(self, to_path: str) -> None: ...
    def close(self) -> None: ...

extension_map: dict[str, type[BaseArchive]]
