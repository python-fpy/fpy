from functools import reduce

from fpy.transducers import filterer, mapper


# Monoid = empty , concat
# Append is concat and empty == []
def append(lst, x):
    lst.append(x)
    return lst


def test_mapper():
    assert reduce(mapper(lambda x: -x, append), range(1, 4), []) == [-1, -2, -3]
    assert reduce(mapper(lambda x: x * 2, append), range(1, 4), []) == [2, 4, 6]


def test_filterer():

    assert reduce(filterer(lambda x: x < 2, append), range(4), []) == [0, 1]


def test_transducers():
    assert reduce(
        filterer(lambda x: x > 1, mapper(lambda x: x * 2, append)), range(4), []
    ) == [4, 6]

    assert reduce(
        mapper(lambda x: x * 10, filterer(lambda x: x > 10, append)), range(4), []
    ) == [20, 30]
