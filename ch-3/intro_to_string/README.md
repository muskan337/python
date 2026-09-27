# Introduction to Strings

## What is a String?

A **string** (`str`) is text. It is written inside single quotes, double quotes, or triple quotes.

## The Code

```python
a = 'muskan'
b = "muskan"
c = "'muskan'"
#string is immutable- can't be changed after being made
#  m   u   s   k   a   n
#  0   1   2   3   4   5  length = 6
#  -6  -5  -4  -3  -2  -1  length = 6

#nameshort = len(c)   #to print the length of a string

#to slice a string
nameshort = b[0:3] #[starting idx :  ending+1 idx], 3 not included but 0 is

print(nameshort)  #mus
character1 = a[1]
print(character1)   #u
```

## Output

```text
mus
u
```

## 1. Ways to Write Strings

| Style | Example | Note |
| ----- | ------- | ---- |
| Single quotes | `'muskan'` | Same as double quotes |
| Double quotes | `"muskan"` | Useful when the text contains `'` |
| Quotes inside quotes | `"'muskan'"` | Prints `'muskan'` with the single quotes |
| Triple quotes | `'''line 1` newline `line 2'''` | Multi-line text |

## 2. Indexing

Every character has a position number called an **index**. Counting starts at `0`.

| Character | m | u | s | k | a | n |
| --------- | - | - | - | - | - | - |
| Positive index | 0 | 1 | 2 | 3 | 4 | 5 |
| Negative index | -6 | -5 | -4 | -3 | -2 | -1 |

```python
name = "muskan"
print(name[0])    # m
print(name[1])    # u
print(name[-1])   # n
```

Accessing an index that does not exist causes an `IndexError`:

```python
# name[10]   # IndexError: string index out of range
```

## 3. Length

```python
print(len("muskan"))   # 6
```

The last valid index is always `length - 1`.

## 4. Slicing

Slicing takes a part of a string: `string[start:stop]`.

* `start` is **included**.
* `stop` is **not included**.

```python
b = "muskan"
print(b[0:3])   # mus   (indexes 0, 1, 2)
```

## 5. Strings are Immutable

You cannot change a character inside a string.

```python
name = "muskan"
# name[0] = "M"    # TypeError: 'str' object does not support item assignment

name = "M" + name[1:]   # build a NEW string
print(name)             # Muskan
```

## Common Mistakes

| Mistake | Fix |
| ------- | --- |
| Expecting `b[0:3]` to include index 3 | The stop index is excluded. |
| Trying to change a character with `name[0] = "M"` | Strings are immutable. Create a new string. |
| Mismatched quotes like `"muskan'` | Start and end with the same type of quote. |
| Starting index count from 1 | Python starts at 0. |

## Summary

* Strings are text in quotes and are **immutable**.
* Index from `0` (left) or `-1` (right).
* `string[start:stop]` slices, and `stop` is excluded.
* `len()` gives the number of characters.
