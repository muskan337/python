# Practice Problem 4: Sum of a List

## Problem

Find the sum of all numbers in a list.

## The Code

```python
list = [1, 3, 4, 5]

print(sum(list))
```

## Output

```text
13
```

## Explanation

`sum()` adds all the numbers in a list: 1 + 3 + 4 + 5 = 13.

## Important: Do Not Name a Variable `list`

`list` is a built-in name in Python. Using it as a variable name hides the built-in, and later code that needs `list(...)` will break:

```python
list = [1, 3, 4, 5]
# list((1, 2, 3))   # TypeError: 'list' object is not callable
```

Use a descriptive name instead:

```python
numbers = [1, 3, 4, 5]

print(sum(numbers))   # 13
```

## Related Built-ins

| Function | Result for `[1, 3, 4, 5]` |
| -------- | ------------------------- |
| `sum(numbers)` | `13` |
| `max(numbers)` | `5` |
| `min(numbers)` | `1` |
| `len(numbers)` | `4` |

## Summary

* `sum()` adds all numbers in a list (the items must be numbers).
* Never use `list`, `str`, `int`, `dict` and similar built-in names as variable names.
