# pylint: disable=too-many-lines,redefined-outer-name,redefined-builtin

from typing import Callable, TypeVar, AsyncIterable
from functools import partial

from asyncrx.core.typing import AsyncObservable

T = TypeVar('T')
T1 = TypeVar('T1')
T2 = TypeVar('T2')


"""A collection of partially appliable and lazy loaded operators."""

def debounce(seconds: float) -> Callable[[AsyncObservable[T]], AsyncObservable[T]]:
    """Debounce source stream.

    Ignores values from a source stream which are followed by
    another value before seconds has elapsed.

    Example:
    partial = debounce(5) # 5 seconds

    Keyword arguments:
    seconds -- Duration of the throttle period for each value

    Returns a partially applied function that takes a source stream to
    debounce."""

    from asyncrx.core.operators.debounce import Debounce
    return partial(Debounce, seconds)

def delay(seconds: float) -> Callable[[AsyncObservable[T]], AsyncObservable[T]]:
    from asyncrx.core.operators.delay import Delay
    return partial(Delay, seconds)

def filter(predicate: Callable[[T], bool]) -> Callable[[AsyncObservable[T]], AsyncObservable[T]]:
    from asyncrx.core.operators.filter import Filter
    return partial(Filter, predicate)

def flat_map(fn: Callable[[T], AsyncObservable]) -> Callable[[AsyncObservable], AsyncObservable]:
    from asyncrx.core.operators.flat_map import FlatMap
    return partial(FlatMap, fn)

def map(fn: Callable) -> Callable[[AsyncObservable[T1]], AsyncObservable[T2]]:
    from asyncrx.core.operators.map import map as _map
    return partial(_map, fn)

def merge(other: AsyncObservable) -> Callable[[AsyncObservable], AsyncObservable]:
def merge(source: AsyncObservable, max_concurrent: int=42) -> AsyncObservable:
    """Merges a source stream of source streams.

    Keyword arguments:
    source -- source stream to merge.
    max_concurrent -- Max number of streams to process concurrently.
        Default value is 42. Setting this to 1 turns merge into concat.

    Returns flattened source stream.
    """
    return Merge(source, max_concurrent)
    from asyncrx.core.operators.merge import Merge
    return partial(Merge, other)



def with_latest_from(mapper: Callable, other: AsyncObservable) -> Callable[[AsyncObservable], AsyncObservable]:
    from asyncrx.core.operators.with_latest_from import with_latest_from
    return partial(with_latest_from, mapper, other)

def distinct_until_changed() -> Callable[[AsyncObservable], AsyncObservable]:
    from asyncrx.core.operators.distinct_until_changed import distinct_until_changed
    return partial(distinct_until_changed)

def switch_latest() -> Callable[[AsyncObservable], AsyncObservable]:
    from asyncrx.core.operators.switch_latest import switch_latest
    return partial(switch_latest)

def to_async_iterable() -> Callable[[AsyncObservable], AsyncIterable]:
    from asyncrx.core.operators.to_async_iterable import to_async_iterable
    return partial(to_async_iterable)
