# Patterns

One entry per technique, added the first time a problem uses it and sharpened at each weekly review. The goal is recognition: reading a new problem and knowing which tool to reach for.

Each entry has:
- **Signals:** words or constraints in the prompt that point to this pattern.
- **Core idea and invariant:** what stays true at every step.
- **Template:** the skeleton, in the language you interview in.
- **Traps:** mistakes actually made, with the problem number.
- **Problems:** links to every problem that used it.

---

## Two pointers (read/write)

**Signals:** "in-place", "O(1) extra space", "remove", "return the new length k", array is sorted or the filter rule only looks backward.

**Core idea and invariant:** a fast pointer `i` reads every element; a slow pointer `k` marks where the next kept element goes. At every step, `nums[0..k)` is exactly the answer for everything read so far.

**Template:**
```python
k = START                      # how many elements are already guaranteed kept
for i in range(START, len(nums)):
    if KEEP(nums[i]):          # rule decides whether nums[i] belongs in the answer
        nums[k] = nums[i]
        k += 1
return k
```

| Problem | START | KEEP(nums[i]) |
|---|---|---|
| 27 Remove Element | 0 | `nums[i] != val` |
| 26 Remove Duplicates | 1 | `nums[i] != nums[k-1]` |
| 80 Remove Duplicates II | 2 | `nums[i] != nums[k-2]` |

The jump from 26 to 80 is the whole lesson: compare against the *written* region (`k - 2`), not the read position (`i - 2`), and "at most m copies" generalizes to `START = m`, compare with `nums[k-m]`.

**Traps:**
- 26 compares `nums[i]` with `nums[i-1]`, which works only because duplicates are adjacent in a sorted array. Comparing with `nums[k-1]` is the version that generalizes.

**Problems:** [26](problems/0026-remove-duplicates-from-sorted-array/NOTES.md), [27](problems/0027-remove-element/NOTES.md), [80](problems/0080-remove-duplicates-from-sorted-array-ii/NOTES.md)
