from fpy.type_classes.Semigroup import (ListSemigroup, ProductSemigroup,
                                        SumSemigroup)


def associativity_check(first, second, third):
    assert first.concat(second).concat(third).x == first.concat(second.concat(third)).x


def test_sum_semigroup():
    a = SumSemigroup(5)
    b = SumSemigroup(20)
    c = SumSemigroup(1)

    assert a.concat(b).concat(c).x == 26

    associativity_check(a, b, c)


def test_product_semigroup():
    a = ProductSemigroup(5)
    b = ProductSemigroup(20)
    c = ProductSemigroup(1)

    assert a.concat(b).concat(c).x == 100

    associativity_check(a, b, c)


def test_list_semigroup():
    a = ListSemigroup([1, 2])
    b = ListSemigroup([3, 4])
    c = ListSemigroup([5, 6])

    assert a.concat(a).concat(b).concat(c).x == [1, 2, 1, 2, 3, 4, 5, 6]

    associativity_check(a, b, c)
