from collections.abc import Callable, Generator
from contextlib import contextmanager
from typing import Any

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test.selenium import SeleniumTestCase
from django.utils.deprecation import MiddlewareMixin

class CSPMiddleware(MiddlewareMixin): ...

class AdminSeleniumTestCase(SeleniumTestCase, StaticLiveServerTestCase):
    def wait_until(self, callback: Callable, timeout: int = ...) -> None: ...
    def wait_for_and_switch_to_popup(self, num_windows: int = ..., timeout: int = ...) -> None: ...
    def wait_for(self, css_selector: str, timeout: int = ...) -> None: ...
    def wait_for_text(self, css_selector: str, text: str, timeout: int = ...) -> None: ...
    def wait_for_value(self, css_selector: str, text: str, timeout: int = ...) -> None: ...
    def wait_until_visible(self, css_selector: str, timeout: int = ...) -> None: ...
    def wait_until_invisible(self, css_selector: str, timeout: int = ...) -> None: ...
    def wait_page_ready(self, timeout: int = ...) -> None: ...
    @contextmanager
    def wait_page_loaded(self, timeout: int = ...) -> Generator[None, None, None]: ...
    def admin_login(self, username: str, password: str, login_url: str = ...) -> None: ...
    def select_option(self, selector: str, value: Any) -> None: ...
    def deselect_option(self, selector: str, value: Any) -> None: ...
    def assertSelectOptions(self, selector: str, values: Any) -> None: ...
    def assertSelectedOptions(self, selector: str, values: Any) -> None: ...
    def has_css_class(self, selector: str, klass: str) -> bool: ...
