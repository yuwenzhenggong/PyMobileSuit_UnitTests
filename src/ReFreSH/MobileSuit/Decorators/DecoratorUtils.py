from . import DecoratorNames
from typing import Callable, Optional
from collections.abc import Iterable # 使用Iterable判断可迭代性

def get_alias(func: Callable):
    has_attr = hasattr(func, DecoratorNames.suit_alias)
    return getattr(func, DecoratorNames.suit_alias) if has_attr else []


def is_ignored(func: Callable):
    check_a = hasattr(func, DecoratorNames.suit_ignored)
    return check_a and getattr(func, DecoratorNames.suit_ignored)


def get_info(func: Callable) -> Optional[str]:
    (expr, resObj) = getattr(func, DecoratorNames.suit_info) if hasattr(func, DecoratorNames.suit_info) else (
    None, None)
    if expr is None:
        return None
    return getattr(resObj, expr) if resObj is not None and hasattr(resObj, expr) else expr


def get_parser(func: Callable, arg_name: str):
    dic = getattr(func, DecoratorNames.suit_parser) if hasattr(
        func, DecoratorNames.suit_parser) else {}
    
    if isinstance(dic, Iterable): # 改正了dic不可迭代时 not in 导致的错误
        if arg_name not in dic:
            return dic[arg_name]
    return None  
    # return None if arg_name not in dic else dic[arg_name]


def get_injected(func: Callable, arg_name: str) -> bool:
    arr = getattr(func, DecoratorNames.suit_injected) if hasattr(
        func, DecoratorNames.suit_injected) else []
    return arg_name in arr
