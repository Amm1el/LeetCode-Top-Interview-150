# 04 · Dicts and sets

Exercises: [`exercises/ex04_dicts_sets.py`](exercises/ex04_dicts_sets.py)

`dict` is `HashMap`, `set` is `HashSet`. Lookups, inserts and `in` are O(1) on average. This is the single most-used tool in LeetCode: "have I seen this before?" and "how many times?"

## dict

```python
d = {}                     # or {"a": 1, "b": 2}
d["a"] = 1                 # insert / overwrite
d["z"]                     # KeyError if missing
d.get("z")                 # None if missing
d.get("z", 0)              # default if missing
"a" in d                   # key membership, O(1)
del d["a"]                 # remove (KeyError if missing)
d.pop("a", None)           # remove, no error if missing
for k in d: ...            # keys
for k, v in d.items(): ... # pairs
list(d.values())
```

Dicts keep insertion order.

Counting by hand:

```python
count = {}
for x in nums:
    count[x] = count.get(x, 0) + 1
```

## Counter and defaultdict

```python
from collections import Counter, defaultdict

c = Counter("banana")          # Counter({'a': 3, 'n': 2, 'b': 1})
c["z"]                         # 0, missing keys read as 0 (and are NOT inserted)
c.most_common(2)               # [('a', 3), ('n', 2)]
Counter(s) == Counter(t)       # anagram check in one line
c1 - c2                        # subtract, drops counts <= 0

groups = defaultdict(list)     # missing key -> new empty list
groups[key].append(word)
seen = defaultdict(int)        # missing key -> 0
seen[x] += 1
```

Trap: with `defaultdict`, even *reading* a missing key (`groups[k]`) inserts it. Use `k in groups` to test.

On LeetCode, `collections`, `heapq`, `bisect`, `math`, `itertools` and `functools` are already imported. In an interview, write the import anyway.

## Keys must be hashable

Ints, strings, tuples of hashables: fine. Lists, sets, dicts: not allowed as keys or set members.

```python
d[tuple(sorted(word))] = ...    # list -> tuple to use as a key
visited.add((r, c))             # grid cells as tuples
```

## set

```python
s = set()                  # NOT {} — that's an empty dict
s = {1, 2, 3}
s.add(4)
s.remove(9)                # KeyError if missing
s.discard(9)               # no error
x in s                     # O(1)
a | b, a & b, a - b        # union, intersection, difference
len(set(nums)) != len(nums)   # has duplicates
```

## The two core moves

**Seen-set:** walk once, check before adding.

```python
seen = set()
for x in nums:
    if x in seen:
        return True
    seen.add(x)
```

**Value → index map:** Two Sum. Check for the complement *before* inserting the current value, so an element never pairs with itself.

```python
index = {}
for i, x in enumerate(nums):
    if target - x in index:
        return [index[target - x], i]
    index[x] = i
```

## Don't mutate while iterating

Adding or removing keys while looping over a dict or set raises `RuntimeError`. Loop over `list(d)` if you need to delete.

## Predict the output

1. ```python
   d = {}
   d["a"] = d.get("a", 0) + 1
   d["a"] = d.get("a", 0) + 1
   print(d)
   ```
2. `print(type({}), type({1}))`
3. ```python
   from collections import defaultdict
   g = defaultdict(list)
   if g["x"]:
       pass
   print(len(g))
   ```
4. `print(Counter("aab") - Counter("abbb"))`
5. `print({[1, 2]: "a"})`

<details><summary>Answers</summary>

1. `{'a': 2}`
2. `<class 'dict'> <class 'set'>`
3. `1` (the read inserted `"x"`)
4. `Counter({'a': 1})` (b would be −2, so it's dropped)
5. `TypeError: unhashable type: 'list'`
</details>
