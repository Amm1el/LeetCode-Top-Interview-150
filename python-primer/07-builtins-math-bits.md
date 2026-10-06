# 07 · Built-ins, itertools, math, bits

Exercises: [`exercises/ex07_builtins_math_bits.py`](exercises/ex07_builtins_math_bits.py)

## Built-ins that replace loops

```python
sum(nums), min(nums), max(nums)             # O(n); min/max of empty raise ValueError
max(nums, default=0)                        # safe on empty
min(words, key=len)
any(x < 0 for x in nums)                    # short-circuits
all(c.isdigit() for c in s)
sum(1 for x in nums if x > 0)               # count matching
divmod(17, 5)                               # (3, 2)
abs(x)
```

`map(int, parts)` and generator expressions (`x * x for x in nums`) are lazy; wrap in `list()` if you need to index.

## itertools

```python
from itertools import accumulate, combinations, permutations, product, groupby, pairwise

list(accumulate([1, 2, 3]))               # [1, 3, 6]          running sums
list(accumulate([1, 2, 3], initial=0))    # [0, 1, 3, 6]       prefix-sum array
list(accumulate(nums, max))               # running max
list(combinations([1, 2, 3], 2))          # [(1, 2), (1, 3), (2, 3)]
list(permutations([1, 2, 3]))             # all 6 orderings
list(product("ab", repeat=2))             # [('a','a'), ('a','b'), ('b','a'), ('b','b')]
[(k, len(list(g))) for k, g in groupby("aaabcc")]   # [('a', 3), ('b', 1), ('c', 2)]
list(pairwise([1, 2, 4]))                 # [(1, 2), (2, 4)]   adjacent pairs
```

In an interview, using `permutations` for a Permutations problem misses the point; the interviewer wants the backtracking. Use these for the parts of a solution that aren't the point.

## math

```python
import math
math.gcd(12, 18)        # 6        math.gcd(*nums) works on many
math.lcm(4, 6)          # 12
math.isqrt(17)          # 4        exact integer square root, no float error
math.comb(5, 2)         # 10       n choose k
math.inf
math.ceil(7 / 2)        # 4
-(-7 // 2)              # 4        ceiling division with integers only (no float)
```

## Bits

| Expression | Meaning |
|---|---|
| `x & 1` | 1 if odd |
| `x >> 1`, `x << 1` | halve (floor), double |
| `x & (x - 1)` | x with its lowest set bit cleared |
| `x & -x` | only the lowest set bit |
| `x > 0 and x & (x - 1) == 0` | power of two |
| `a ^ a == 0`, `a ^ 0 == a` | XOR cancels pairs (Single Number) |
| `bin(x).count("1")` or `x.bit_count()` | number of 1 bits |
| `(x >> i) & 1` | bit i |
| `x | (1 << i)` | set bit i |

**The Python-specific trap:** integers have unlimited precision, so negative numbers behave as if they have infinitely many leading 1s. `~5 == -6`. `-1 >> 1 == -1` forever. Problems that assume 32-bit integers (Reverse Bits, Sum of Two Integers, Number of 1 Bits on a negative) need a mask:

```python
MASK = 0xFFFFFFFF
x &= MASK                                   # keep only the low 32 bits
if x > 0x7FFFFFFF:                          # convert back to a signed 32-bit value
    x = ~(x ^ MASK)
```

## Predict the output

1. `print(list(accumulate([3, 1, 4], initial=0)))`
2. `print(12 & 11, 12 & -12, 5 ^ 3 ^ 5)`
3. `print(-(-10 // 3), 10 // 3)`
4. `print(any([]), all([]))`
5. `print(max([], default=-1), sum(x for x in range(4)))`

<details><summary>Answers</summary>

1. `[0, 3, 4, 8]`
2. `8 4 3`
3. `4 3`
4. `False True` (all of nothing is vacuously true)
5. `-1 6`
</details>
