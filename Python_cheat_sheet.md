# Python cheat sheet
.

# One liners
:small_orange_diamond: Get groups of n-th elements from each tuple
```python
data = [(1, 2, 3), (1, 2, 3), (1, 2, 3)]
l1 = []; l2 = []; l3 = []

res = list(zip(*data)))
# res: [(1, 1, 1), (2, 2, 2), (3, 3, 3)]
```
If groups have different number of elements use [itertools.zip_longest](https://docs.python.org/3/library/itertools.html#itertools.zip_longest).