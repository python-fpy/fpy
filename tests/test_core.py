from functools import partial
from operator import add, mul

from fpy.core import (always, composable_filter, composable_map, compose,
                      curry, do, filter_falsy, first, flatten, flip, identity,
                      last, nth, pipe, second, tail)

multiply_10 = partial(mul, 10)
add_10 = partial(add, 10)


def test_identity():
    for i in [1, "one", None, 1.1]:
        assert i == identity(i)


def test_compose():
    calc = (2 + 10) * 10
    assert compose(multiply_10, add_10)(2) == calc


def test_curry():
    def summed(a, b, c, d, e):
        return a + b + c + d + e

    sum5 = curry(summed)

    assert sum5(1, 2, 3, 4, 5) == sum5(1, 2)(3, 4)(5) == sum5(1, 2, 3)(4)(5)


def test_flip():
    def fun(x, y, z):
        return f"{x}:{y}:{z}"

    nuf = flip(fun)
    curry_nuf = curry(nuf)
    assert "3:2:1" == nuf(1, 2, 3) == curry_nuf(1, 2)(3)


def test_always():
    always_3 = always(3)
    assert 3 == always_3()


def test_composable_filter():

    assert [0, 1, 2, 3, 4, 5] == composable_filter(lambda x: x <= 5)(range(0, 10))


def test_composable_map():
    assert [10, 11, 12, 13, 14] == composable_map(add_10)(range(0, 5))


def test_filter_falsy():
    falsy_list = [None, 0, "", [], {}, ()]
    assert [] == filter_falsy(falsy_list)


def test_pipe():
    assert 120 == pipe(2, add_10, multiply_10)


def test_do():
    assert 10 == do(add_10, 10)


int_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


def test_nth():
    fourth = nth(4)
    assert 40 == fourth(int_list)


def test_first():
    assert first(int_list) == 0


def test_second():
    assert 10 == second(int_list)


def test_tail():
    assert [90, 100] == tail(2)(int_list)


def test_last():
    assert 100 == last(int_list)


def test_flatten():
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9] == list(
        flatten([1, [2, 3, [4, 5, 6, [7, 8, [9]]]]])
    )
