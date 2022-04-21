[Fantasy Land Specs](https://github.com/fantasyland/fantasy-land)

| #  | Name          | in Other Type                 | functions                |
|----|---------------|-------------------------------|--------------------------|
| 1  | Functor       | -                             | map                      |
| 2  | Alt           | Functor + alt                 | map, alt                 |
| 3  | Plus          | Alt + zero                    | map, alt, zero           |
| 4  | Alternative   | Plus + Applicative            | map, alt, zero, ap, of   |
| 5  | Apply         | Functor + ap                  | map, ap                  |
| 6  | Applicative   | Apply + of                    | map, ap, of              |
| 7  | Chain         | Apply + chain                 | map, ap, chain           |
| 8  | ChainRec      | Chain + chainRec              | map, ap, chain, chainRec |
| 9  | Monad         | Applicative + Chain           | map, ap, of, chain       |
| 10 | Bifunctor     | Functor + bimap               | map, bimap               |
| 11 | Extend        | Functor + extend              | map, extend              |
| 12 | Comonad       | Extend + extract              | map, extend, extract     |
| 13 | Profunctor    | Functor + promap              | map, promap              |
| 14 | Foldable      | reduce                        | reduce                   |
| 15 | Traversable   | Functor + Foldable + traverse | map, reduce, traverse    |
| 16 | Semigroupid   | compose                       | compose                  |
| 17 | Category      | Semigroupid + id              | compose, id              |
| 18 | Contravariant | contramap                     | contramap                |
| 19 | Filterable    | filter                        | filter                   |
| 20 | Semigroup     | concat                        | concat                   |
| 21 | Monoid        | Semigroup + empty             | concat, empty            |
| 22 | Group         | Monoid + invert               | concat, empty, invert    |
| 23 | Setiod        | equals                        | equals                   |
| 24 | Ord           | Setiod + lte                  | equals, lte              |

### Derivations
- map = ap and of
- map = chain and of 
