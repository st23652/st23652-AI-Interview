from collections.abc import Awaitable, Callable
from logging import Logger
from typing import Any

import _typeshed
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBase
from django.urls.resolvers import ResolverMatch

logger: Logger

class BaseHandler:
    def load_middleware(self, is_async: bool = ...) -> None: ...
    def adapt_method_mode(
        self,
        is_async: bool,
        method: Callable[[HttpRequest], HttpResponseBase | Awaitable[HttpResponseBase]],
        method_is_async: bool | None = ...,
        debug: bool = ...,
        name: str | None = ...,
    ) -> Callable[[HttpRequest], HttpResponseBase | Awaitable[HttpResponseBase]]: ...
    def get_response(self, request: HttpRequest) -> HttpResponseBase: ...
    async def get_response_async(self, request: HttpRequest) -> HttpResponseBase: ...
    def resolve_request(self, request: HttpRequest) -> ResolverMatch: ...
    def check_response(self, response: HttpResponseBase, callback: Any, name: str | None = ...) -> None: ...
    def make_view_atomic(self, view: Callable[..., HttpResponseBase]) -> Callable[..., HttpResponseBase]: ...
    def process_exception_by_middleware(self, exception: Exception, request: HttpRequest) -> HttpResponse: ...

def reset_urlconf(sender: _typeshed.Unused, **kwargs: Any) -> None: ...
