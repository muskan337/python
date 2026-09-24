# Practice Problem 3: Tuples Cannot Be Changed

## Problem

Show that a tuple item cannot be modified after the tuple is created.

## The Code

```python
a = (1, 3, "muskan", False)
# a[2 ] =  "garvit"
# print(a[2])
```

## Output

Nothing is printed, because the last two lines are commented out.

## What Happens If You Remove the `#`?

```python
a = (1, 3, "muskan", False)
a[2] = "garvit"
```

```text
TypeError: 'tuple' object does not support item assignment
```

Tuples are **immutable**, so item assignment is not allowed.

## How to "Change" a Tuple

Convert to a list, change it, and convert back:

```python
a = (1, 3, "muskan", False)

temp = list(a)         # tuple -> list
temp[2] = "garvit"     # change the item
a = tuple(temp)        # list -> tuple

print(a)               # (1, 3, 'garvit', False)
```

This creates a **new** tuple. The old one is not modified.

## Summary

* Tuples are immutable: no assignment, no `append`, no `remove`.
* To modify, convert to a list first, then back to a tuple.
* Use tuples for data that should not change.
