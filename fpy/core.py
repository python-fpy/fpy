from collections import deque
from functools import partial, reduce, update_wrapper, wraps
from inspect import getfullargspec, signature
from itertools import islice
from operator import add, itemgetter
from typing import Iterable

# Functions

# Trace function
# Primarily for debugging, printing data
def print_current(label):
    def printer(tag, value):
        print(f"{tag=}: {value=}")
        return value

    return partial(printer, label)


# identity function
# https://gist.github.com/tsangwpx/b9af7fa87a9aeb60651f6b7159680f0e
identity = partial(reduce, add, ())


# compose function
# https://stackoverflow.com/a/59232780
def compose(*fns):
    return reduce(lambda f, g: lambda x: g(f(x)), reversed(fns), identity)


# Curry
# https://github.com/fnpy/fn.py/blob/master/fn/func.py#L61=
def curry(func):
    """A decorator that makes the function curried
    Usage example:
    >>> @curried
    ... def sum5(a, b, c, d, e):
    ...     return a + b + c + d + e
    ...
    >>> sum5(1)(2)(3)(4)(5)
    15
    >>> sum5(1, 2, 3)(4, 5)
    15
    """

    @wraps(func)
    def _curried(*args, **kwargs):
        f = func
        count = 0
        while isinstance(f, partial):
            if f.args:
                count += len(f.args)
            f = f.func

        if count == len(signature(f).parameters) - len(args):
            return func(*args, **kwargs)

        para_func = partial(func, *args, **kwargs)
        update_wrapper(para_func, f)
        return curry(para_func)

    return _curried


def flip(function):
    if len(getfullargspec(function).args) < 1:
        return function

    @wraps(function)
    def new_function(*args):
        return function(*reversed(args))

    return new_function


# Always
# Aka const, constant or K
def always(x):
    def always_func():
        return x

    return always_func


# filter returns a filter object, we want it to return list
def composable_filter(func):
    return compose(list, partial(filter, func))


# map returns a map object, we want it to return list
def composable_map(func):
    return compose(list, partial(map, func))


# Create a generator expression for an iterable
def build_gen_exp(iterable):
    return (x for x in iterable)


filter_falsy = composable_filter(None)

# pipe function
def pipe(data, *functions):
    if not functions:
        return data
    for function in functions:
        data = function(data)
    return data


# do function
# calls function on parameter and returns parameter not the result of function call
# def do_n_times(func, times, *args):
#    return next(islice(starmap(func, repeat(args, times)), times, times), None)


def do(func, param):
    func(param)
    return param


# nth
# def nth(n):
#     return compose(iter, partial(do_n_times, next, n - 1), next)
@curry
def nth(n, iterable):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), None)


# first
# get the first item from the iterable
first = compose(next, iter)

# second
# get second item from the iterable
# second = nth(2)
second = compose(next, partial(do, next), iter)


# tail, get last n elements
def tail(n: int):
    return compose(list, partial(deque, maxlen=n), iter)


# last
last = compose(itemgetter(0), tail(1))

# Flatten
# https://github.com/dabeaz/python-cookbook/blob/master/src/4/how_to_flatten_a_nested_sequence/example.py
def flatten(nested_iterable, ignore_types=(str, bytes)):
    for x in nested_iterable:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x
