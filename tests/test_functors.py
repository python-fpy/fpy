from functools import partial
from operator import add

from fpy.core import compose, identity
from fpy.type_classes.Functor import Functor

add1 = partial(add, 1)
add3 = partial(add, 3)


def test_associativity():
    f1 = Functor(2).map(compose(add1, add3))
    f2 = Functor(2).map(add1).map(add3)
    assert f1.x == f2.x


def test_identity():
    f1 = Functor(3)
    f2 = Functor(3).map(identity)
    assert f1.x == f2.x
