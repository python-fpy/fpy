# https://en.wikipedia.org/wiki/Transducer
from typing import Callable


def mapper(fn: Callable, acc_fn: Callable):
    def mapper_(acc, x):
        return acc_fn(acc, fn(x))

    return mapper_


def filterer(fn: Callable, acc_fn: Callable):
    def filterer_(acc, x):
        return acc_fn(acc, x) if fn(x) else acc

    return filterer_


# TODO Monoidal tranducers
