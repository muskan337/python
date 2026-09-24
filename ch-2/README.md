# Chapter 2: Python Basics

This chapter covers the building blocks of every Python program: variables, data types, input, operators, and type casting.

## Contents

| Folder / File | Topic |
| ------------- | ----- |
| [variables](variables) | Creating variables and printing them |
| [datatypes](datatypes) | Built-in data types (detailed notes) |
| [input](input) | `input()`, `int()`, f-strings |
| [operatorss](operatorss) | Operators |
| `typecasting and Type( )func` | Converting types and checking with `type()` |

---

## Type Casting and `type()` (the file without a folder)

The file `typecasting and Type( )func` has no `.py` extension, so it will not open as Python in most editors. Its content:

```python
a = 31.2
b = float(a)
t = type(b)

print(t)
```

### Explanation

| Line | Meaning |
| ---- | ------- |
| `a = 31.2` | `a` is a float. |
| `b = float(a)` | Converts `a` to float. Since it is **already** a float, nothing changes. |
| `t = type(b)` | Stores the type of `b`. |
| `print(t)` | Prints the type. |

### Output

```text
<class 'float'>
```

### Improvement

The example is more useful if you convert to a **different** type:

```python
a = 31.2
b = int(a)        # float -> int (decimal part is cut off)

print(b)          # 31
print(type(b))    # <class 'int'>
```

### Common Conversions

| Conversion | Example | Result |
| ---------- | ------- | ------ |
| int → float | `float(5)` | `5.0` |
| float → int | `int(3.9)` | `3` |
| string → int | `int("42")` | `42` |
| int → string | `str(100)` | `'100'` |

Suggestion: move this file to `ch-2/typecasting/typecasting.py` and add a README like the others.

---

## Summary

| Concept | Remember |
| ------- | -------- |
| Variable | A name that stores a value |
| Data type | The kind of value (`int`, `float`, `str`, `bool`, `None`) |
| `input()` | Always returns a string |
| Operators | Arithmetic, assignment, comparison, logical |
| Type casting | Use `int()`, `float()`, `str()` to convert |
| `type()` | Tells the type of a value |
