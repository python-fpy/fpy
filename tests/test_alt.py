from fpy.type_classes.Alt import Alt

# Associativity
# a.alt(b).alt(c) == a.alt(b.alt(c))

# Distributivity
# a.alt(b).map(f) == a.map(f).alt(b.map(f))

a1 = Alt(None)
a2 = Alt("")
a3 = Alt(2)


def test_associativity():
    assert a1.alt(a2).alt(a3).x == a1.alt(a2.alt(a3)).x


def test_distributivity():
    a1 = Alt(3)
    a2 = Alt(5)
    assert a1.alt(a2).map(str).x == a1.map(str).alt(a2.map(str)).x
