from typing import Generic, TypeVar

from asyncrx import abc

T_out = TypeVar('T_out', covariant=True)
T_in = TypeVar('T_in', contravariant=True)


class Observable(Generic[T_out], abc.Observable):
    """A generic version of asyncrx.abc.Source."""

    __slots__ = ()


class AsyncObservable(Generic[T_out], abc.AsyncObservable):
    """A generic version of asyncrx.abc.AsyncObservable."""

    __slots__ = ()


class Observer(Generic[T_in], abc.Observer):
    """A generic version of asyncrx.abc.Sink."""

    __slots__ = ()


class AsyncObserver(Generic[T_out], abc.AsyncObserver):
    """A generic version of asyncrx.abc.AsyncObserver."""

    __slots__ = ()
