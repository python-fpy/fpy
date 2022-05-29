# https://github.com/fantasyland/fantasy-land#semigroup=
from abc import ABC, abstractmethod
from dataclasses import dataclass

from fpy.type_classes.Functor import X


class AbstractSemigroup(ABC):
    """
    a['concat'](b)['concat'](c) = a['concat'](b['concat'](c)) (associativity)
    """

    @abstractmethod
    def concat(self, other):
        """concat :: Semigroup a => a ~> a -> a"""
        pass


@dataclass(eq=False, order=False)
class ListSemigroup(X, AbstractSemigroup):
    def concat(self, other):
        return self.__class__([*self.x, *other.x])


@dataclass(eq=False, order=False)
class SumSemigroup(X, AbstractSemigroup):
    def concat(self, other):
        return SumSemigroup(self.x + other.x)


@dataclass(eq=False, order=False)
class ProductSemigroup(X, AbstractSemigroup):
    def concat(self, other):
        return ProductSemigroup(self.x * other.x)
