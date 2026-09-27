# Practice Problem 5: Count Items in a Tuple

## Problem

Count how many times `0` appears in a tuple.

## The Code

```python
a = (1, 0, 0, 0 )

n = a.count(0)
print(n)
```

## Output

```text
3
```

## Explanation

| Code | Meaning |
| ---- | ------- |
| `a = (1, 0, 0, 0)` | A tuple with four items. |
| `a.count(0)` | Counts how many items equal `0`. |
| `print(n)` | Prints `3`. |

## Interesting Detail

In Python, `False == 0` is `True`. So `count(0)` also counts `False`:

```python
b = (1, 0, False, 0)
print(b.count(0))    # 3
```

## Tuple Methods

| Method | Meaning | Example | Result |
| ------ | ------- | ------- | ------ |
| `count(x)` | How many times `x` appears | `(1,0,0).count(0)` | `2` |
| `index(x)` | Position of the first `x` | `(5,6,7).index(7)` | `2` |

## Summary

* Tuples have only two methods: `count()` and `index()`.
* `count()` returns `0` if the item is not present.
