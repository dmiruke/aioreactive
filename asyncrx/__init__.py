from typing import Callable, TypeVar, Generic, Iterable

from asyncrx.abc import AsyncDisposable
from asyncrx.core.observables import AsyncObservable

T = TypeVar('T')
T1 = TypeVar('T1')
T2 = TypeVar('T2')


def from_iterable(iter: Iterable[T]) -> 'AsyncObservable[T]':
    from asyncrx.operators.from_iterable import from_iterable
    return from_iterable(iter)

def from_async_iterable(iter: Iterable[T]) -> 'AsyncObservable[T]':
    from asyncrx.operators.from_async_iterable import from_async_iterable
    from_async_iterable(iter)

def unit(value: T) -> 'AsyncObservable[T]':
    from asyncrx.operators.unit import unit
    unit(value)

def empty() -> 'AsyncObservable[T]':
    from asyncrx.operators.empty import empty
    empty()

def never() -> 'AsyncObservable[T]':
    from asyncrx.operators.never import never
    never()
