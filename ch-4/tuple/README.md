# Tuples

## What is a Tuple?

A **tuple** is an ordered collection of items, like a list, but it **cannot be changed** after it is created (it is immutable).

## The Code

```python
a = (1, 2, 5, 6, False, )
b = (1, )
print(type(a))
#tuple is an immutable data type in python
```

## Output

```text
<class 'tuple'>
```

## Explanation

| Code | Meaning |
| ---- | ------- |
| `a = (1, 2, 5, 6, False, )` | A tuple with 5 items. The trailing comma is allowed. |
| `b = (1, )` | A tuple with **one** item. The comma is what makes it a tuple. |
| `type(a)` | Tells us `a` is a tuple. |

## One-Item Tuples

```python
b = (1,)    # tuple
c = (1)     # just the number 1

print(type(b))   # <class 'tuple'>
print(type(c))   # <class 'int'>
```

Without the comma, the brackets are just ordinary brackets.

## Indexing and Slicing

Works like lists and strings:

```python
a = (1, 2, 5, 6, False)

print(a[0])      # 1
print(a[-1])     # False
print(a[1:3])    # (2, 5)
print(len(a))    # 5
```

## Immutability

```python
a = (1, 2, 5)
# a[0] = 10      # TypeError: 'tuple' object does not support item assignment
```

## Why Use Tuples?

* They protect data from accidental changes.
* They are slightly faster and use less memory than lists.
* They can be used as dictionary keys (lists cannot).

## Summary

* Tuples use `( )` and are immutable.
* A single-item tuple needs a comma: `(1,)`.
* Indexing and slicing work exactly like lists.
