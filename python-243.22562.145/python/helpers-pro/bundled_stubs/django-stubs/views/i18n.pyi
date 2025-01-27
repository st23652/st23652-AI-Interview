from collections.abc import Callable
from pathlib import Path
from typing import Any

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.utils.translation.trans_real import DjangoTranslation
from django.views.generic import View

LANGUAGE_QUERY_PARAMETER: str

def builtin_template_path(name: str) -> Path: ...
def set_language(request: HttpRequest) -> HttpResponse: ...
def get_formats() -> dict[str, list[str] | int | str]: ...

class JavaScriptCatalog(View):
    head: Callable
    domain: str
    packages: list[str] | None
    translation: DjangoTranslation
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def get_paths(self, packages: list[str]) -> list[str]: ...
    def get_plural(self) -> list[str] | None: ...
    def get_catalog(self) -> dict[str, list[str] | str]: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
    def render_to_response(self, context: dict[str, Any], **response_kwargs: Any) -> HttpResponse: ...

class JSONCatalog(JavaScriptCatalog): ...
