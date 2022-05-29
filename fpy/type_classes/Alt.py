# https://github.com/fantasyland/fantasy-land#alt=
from abc import abstractmethod
from dataclasses import dataclass
from typing import Callable

from fpy.type_classes.Functor import AbstractFunctor, X

# Alt = Functor + alt
# Laws
# Associativity
# a.alt(b).alt(c) == a.alt(b.alt(c))

# Distributivity
# a.alt(b).map(f) == a.map(f).alt(b.map(f))


class AbstractAlt(AbstractFunctor):
    """
    a['alt'](b)['alt'](c) == a['alt'](b['alt'](c)) (associativity)
    a['alt'](b)['map'](f) == a['map'](f)['alt'](b['map'](f)) (distributivity)
    """

    @abstractmethod
    def alt(self, other):
        """
        alt :: Alt f => f a ~> f a -> f a
        """
        pass


@dataclass(eq=False)
class Alt(X, AbstractAlt):
    def map(self, f: Callable):
        """
        map :: Functor f => f a ~> (a -> b) -> f b
        """
        return self.__class__(f(self.x))

    def alt(self, other):
        """
        alt :: Alt f => f a ~> f a -> f a
        """
        return self if self.x else other
