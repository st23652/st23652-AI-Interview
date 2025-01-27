from typing import Any

def cached_import(module_path: str, class_name: str) -> Any: ...
def import_string(dotted_path: str) -> Any: ...
def autodiscover_modules(*args: Any, **kwargs: Any) -> None: ...
def module_has_submodule(package: Any, module_name: str) -> bool: ...
def module_dir(module: Any) -> str: ...
