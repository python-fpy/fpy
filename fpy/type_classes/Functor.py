# https://github.com/fantasyland/fantasy-land#functor=

# Laws
# Identity
# u.map(identity) === u

# Composition:
# u.map(f).map(g) === u.map(x => g(f(x)))

# U is a functor
# U(x).map(f) === U(f(x))


from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Callable


@dataclass(eq=False, slots=False, order=False)
class X:
    x: Any


@dataclass(eq=False, slots=False, order=False)
class Y:
    y: Any


class AbstractFunctor(ABC):
    """
    u['map'](a => a) == u (identity)
    u['map'](x => f(g(x))) == u['map'](g)['map'](f) (composition)
    """

    @abstractmethod
    def map(self, fn: Callable):
        """
        map :: Functor f => f a ~> (a -> b) -> f b
        """
        pass


@dataclass(eq=False, order=False)
class Functor(X, AbstractFunctor):
    def map(self, fn: Callable):
        """
        map :: Functor f => f a ~> (a -> b) -> f b
        """
        return self.__class__(fn(self.x))
