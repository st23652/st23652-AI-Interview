from collections.abc import Callable, Iterable, Iterator
from io import BytesIO
from re import Match, Pattern
from typing import ClassVar, TypeVar, overload

from django.db.models.base import Model
from django.utils.functional import SimpleLazyObject, _StrOrPromise

_StrOrPromiseT = TypeVar("_StrOrPromiseT", bound=_StrOrPromise)
_StrOrPromiseOrNoneT = TypeVar("_StrOrPromiseOrNoneT", bound=_StrOrPromise | None)

def capfirst(x: _StrOrPromiseOrNoneT) -> _StrOrPromiseOrNoneT: ...

re_notag: Pattern[str]
re_prt: Pattern[str]

class WordsRegex:
    @staticmethod
    def search(text: str, pos: int) -> Match | FakeMatch: ...

class FakeMatch:
    def __init__(self, text: str, end: int) -> None: ...
    def __getitem__(self, group: int) -> str | None: ...
    def end(self, group: int = 0) -> int: ...

re_words: type[WordsRegex]
re_chars: Pattern[str]
re_tag: Pattern[str]
re_newlines: Pattern[str]
re_camel_case: Pattern[str]

def wrap(text: _StrOrPromiseT, width: int) -> _StrOrPromiseT: ...
def add_truncation_text(text: str, truncate: str | None = ...) -> str: ...

class Truncator(SimpleLazyObject):
    MAX_LENGTH_HTML: ClassVar[int]
    def __init__(self, text: Model | str) -> None: ...
    def chars(self, num: int, truncate: str | None = ..., html: bool = ...) -> str: ...
    def words(self, num: int, truncate: str | None = ..., html: bool = ...) -> str: ...

def get_valid_filename(name: _StrOrPromiseT) -> _StrOrPromiseT: ...
@overload
def get_text_list(list_: list[str], last_word: str = ...) -> str: ...
@overload
def get_text_list(list_: list[_StrOrPromise], last_word: _StrOrPromise = ...) -> _StrOrPromise: ...
def normalize_newlines(text: _StrOrPromiseT) -> _StrOrPromiseT: ...
def phone2numeric(phone: _StrOrPromiseT) -> _StrOrPromiseT: ...
def compress_string(s: bytes, *, max_random_bytes: int | None = ...) -> bytes: ...

class StreamingBuffer(BytesIO):
    vals: list[bytes]
    def read(self) -> bytes: ...  # type: ignore[override]

def compress_sequence(sequence: Iterable[bytes], *, max_random_bytes: int | None = ...) -> Iterator[bytes]: ...

smart_split_re: Pattern[str]

def smart_split(text: str) -> Iterator[str]: ...
def unescape_string_literal(s: _StrOrPromiseT) -> _StrOrPromiseT: ...
def slugify(value: _StrOrPromiseT, allow_unicode: bool = ...) -> _StrOrPromiseT: ...
def camel_case_to_spaces(value: str) -> str: ...

format_lazy: Callable[..., str]
