# Tuple Methods

## The Code

```python
a = (1, 2, 5, 6, False, )
b = (1, )
print(type(a))
#tuple is an immutable data type in python

no = a.count(45)
print(no) # means no 45 in a
i = a.index(6)
print(i)
```

## Output

```text
<class 'tuple'>
0
3
```

## Explanation

| Code | Meaning | Result |
| ---- | ------- | ------ |
| `type(a)` | Type of `a` | `<class 'tuple'>` |
| `a.count(45)` | How many times `45` appears in `a` | `0` (not present) |
| `a.index(6)` | Index of the first `6` | `3` |

Index positions: `1`→0, `2`→1, `5`→2, `6`→3, `False`→4.

## The Only Two Tuple Methods

Because tuples are immutable, they have very few methods.

| Method | Meaning | Example | Result |
| ------ | ------- | ------- | ------ |
| `count(x)` | Number of times `x` appears | `(1, 2, 2).count(2)` | `2` |
| `index(x)` | Index of the first `x` | `(1, 2, 2).index(2)` | `1` |

## Error Case

`index()` raises an error when the value is missing, while `count()` just returns `0`:

```python
a = (1, 2, 5, 6)

print(a.count(45))    # 0
# print(a.index(45))  # ValueError: tuple.index(x): x not in tuple
```

## Methods That Do Not Exist for Tuples

```python
# a.append(7)     # AttributeError
# a.remove(1)     # AttributeError
# a.sort()        # AttributeError
```

Use a list if you need these.

## Note

The first three lines of this file are the same as in the [tuple](../tuple) folder. This file adds the `count()` and `index()` examples.

## Summary

* Tuples have only `count()` and `index()`.
* `count()` returns `0` for a missing item, but `index()` raises `ValueError`.
