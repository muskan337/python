# Sets

## What is a Set?

A **set** is a collection of **unique** items with **no fixed order**. Duplicates are removed automatically.

## The Code

```python
# Collectionn of non-repetitive elements

d = {1, 4, 56}

#empty set
```

## Output

Nothing is printed, because the file has no `print()` statement. The section `#empty set` is only a comment, so the code for it is not written yet.

## Explanation

| Code | Meaning |
| ---- | ------- |
| `d = {1, 4, 56}` | Creates a set with three unique numbers. |
| `#empty set` | A comment. The idea was to show how to create an empty set. |

## Creating an Empty Set

`{}` creates an empty **dictionary**, not a set. Use `set()`:

```python
e = set()
f = {}

print(type(e))   # <class 'set'>
print(type(f))   # <class 'dict'>
```

You can complete the file with:

```python
d = {1, 4, 56}
print(d, type(d))    # {1, 4, 56} <class 'set'>

e = set()
print(e)             # set()
```

## Properties

| Property | Detail |
| -------- | ------ |
| Unique | `{1, 1, 2}` becomes `{1, 2}` |
| Unordered | No index, so `d[0]` gives a `TypeError` |
| Mutable | You can add and remove items |
| Items must be immutable | Numbers, strings, tuples are fine. Lists are not. |

## Common Methods

```python
d = {1, 4, 56}

d.add(7)          # {1, 4, 56, 7}
d.remove(4)       # {1, 56, 7}   (KeyError if missing)
d.discard(100)    # no error even if missing
print(len(d))     # 3
```

## Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # {1, 2, 3, 4, 5}   union
print(a & b)   # {3}               intersection
print(a - b)   # {1, 2}            difference
```

## Removing Duplicates

```python
numbers = [1, 2, 2, 3, 3, 3]
print(list(set(numbers)))   # [1, 2, 3]
```

## Common Mistakes

| Mistake | Fix |
| ------- | --- |
| Using `{}` for an empty set | Use `set()`. |
| Trying `d[0]` | Sets have no positions. Loop over it or use `in`. |
| Expecting order to be preserved | Sets are unordered. |
| Putting a list inside a set | Lists are mutable and not allowed. Use a tuple. |

## Summary

* Sets hold unique, unordered items.
* Create an empty set with `set()`.
* Use sets to remove duplicates and to do union, intersection and difference.
