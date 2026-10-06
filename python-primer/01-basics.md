# 01 · Basics, coming from Java

Exercises: [`exercises/ex01_basics.py`](exercises/ex01_basics.py)

## Blocks, variables, no types

```python
x = 5            # no type, no semicolon
if x > 3:        # colon, then indentation is the block (4 spaces)
    print("big")
elif x == 3:     # elif, not else if
    print("three")
else:
    print("small")
```

Types still exist, they're just on the values. LeetCode signatures carry hints like `nums: List[int]`; Python ignores them at runtime.

## Truthiness

These are all falsy: `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None`, `False`. Everything else is truthy.

```python
if not nums:          # empty list check, the idiomatic way
    return 0
while stack:          # loop until the stack is empty
    node = stack.pop()
if node is None:      # compare to None with `is`, not ==
    ...
```

Trap: `if x:` is false when `x == 0`. If 0 is a valid value (an index, a node value), write `if x is not None:`.

## Operators that differ from Java

| Python | Java | Note |
|---|---|---|
| `and`, `or`, `not` | `&&`, `\|\|`, `!` | |
| `7 / 2 == 3.5` | `7 / 2 == 3` | `/` is always float division |
| `7 // 2 == 3` | | floor division |
| `-7 // 2 == -4` | `-7 / 2 == -3` | **floors toward −∞**, Java truncates toward 0 |
| `int(-7 / 2) == -3` | | truncation, when you need Java behavior |
| `-7 % 3 == 2` | `-7 % 3 == -1` | result takes the divisor's sign |
| `2 ** 10 == 1024` | `Math.pow` | power |
| `0 <= i < n` | `0 <= i && i < n` | chained comparisons |
| `x if cond else y` | `cond ? x : y` | ternary |
| `i += 1` | `i++` | no `++` or `--` |

Integers never overflow. That's mostly a gift, but problems like Reverse Integer say "return 0 if outside 32-bit range" and you have to check that yourself: `-2**31 <= x <= 2**31 - 1`.

Infinity for running min/max: `float('inf')`, `float('-inf')` (or `math.inf`).

## Loops

```python
for i in range(n):              # 0 .. n-1
for i in range(2, n):           # 2 .. n-1
for i in range(n - 1, -1, -1):  # n-1 down to 0 (stop is exclusive, so -1)
for i in range(0, n, 2):        # step 2
for x in nums:                  # for-each
while lo <= hi:
    ...
```

`break` and `continue` work like Java. There's no C-style `for (;;)`; if the index moves irregularly, use `while`.

## Multiple assignment

```python
a, b = b, a            # swap, no temp
a, b = b, a + b        # Fibonacci step
lo, hi = 0, len(nums) - 1
```

The whole right side is evaluated first, then assigned left to right. That matters with linked lists:

```python
prev, cur.next, cur = cur, prev, cur.next   # works
cur, cur.next, prev = cur.next, prev, cur   # breaks: cur is reassigned before cur.next is set
```

Until it's second nature, use a temp variable in linked-list code. Clarity beats cleverness in an interview.

## Printing while debugging

```python
print(f"i={i} lo={lo} window={nums[lo:i+1]}")
```

## Predict the output

Answer before opening each one.

1. `print(-9 // 4, -9 % 4)`
2. `print(bool([0]), bool(0), bool(""), bool(" "))`
3. `print(1 < 3 > 2)`
4. ```python
   x = 0
   if x:
       print("A")
   elif x is not None:
       print("B")
   ```
5. `print(list(range(5, 0, -2)))`

<details><summary>Answers</summary>

1. `-3 3` (floor of −2.25 is −3; −9 − (4 × −3) = 3)
2. `True False False True` (a list containing 0 is non-empty; a space is a non-empty string)
3. `True` (means `1 < 3 and 3 > 2`)
4. `B`
5. `[5, 3, 1]`
</details>
