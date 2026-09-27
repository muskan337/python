# String Functions (Methods)

## What are String Methods?

A **method** is a built-in action a string can perform, called with a dot: `text.method()`. Methods **do not change** the original string (strings are immutable). They return a **new** value.

## The Code

```python
name = "muskan jain"

print(len(name))
print(name.endswith("kan"))
print(name.startswith("mus"))
print(name.capitalize())

str(123)
"HELLO".lower()
"hello".upper()
"hello world".capitalize()

print(name.count("a"))
print(name.find("muskan"))
print(name.replace("muskan", "jain"))

"hello world".title()
" hello ".strip()
" muskan ".lstrip()
" muskan ".rstrip()
```

(Comments removed for space. See your file for the originals.)

## Output

```text
11
False
True
Muskan jain
2
0
jain jain
```

## Two Comments in the File Need Correcting

| Line | Comment says | Actual result | Why |
| ---- | ------------ | ------------- | --- |
| `print(len(name))` | `#6` | `11` | `"muskan jain"` has 11 characters including the space. `6` is the length of just `"muskan"`. |
| `print(name.endswith("kan"))` | `#true` | `False` | The string ends with `"jain"`, not `"kan"`. |

## Lines That Show No Output

Lines like `"hello".upper()` compute a result but do not print it, so nothing appears. To see the result, use `print()`:

```python
print("hello".upper())   # HELLO
```

## Methods Reference

| Method | What it does | Example | Result |
| ------ | ------------ | ------- | ------ |
| `len(s)` | Number of characters | `len("hi")` | `2` |
| `s.upper()` | All capitals | `"hello".upper()` | `'HELLO'` |
| `s.lower()` | All small letters | `"HELLO".lower()` | `'hello'` |
| `s.capitalize()` | First letter capital, rest small | `"hello world".capitalize()` | `'Hello world'` |
| `s.title()` | First letter of every word capital | `"hello world".title()` | `'Hello World'` |
| `s.startswith(x)` | Does it begin with `x`? | `"muskan".startswith("mus")` | `True` |
| `s.endswith(x)` | Does it end with `x`? | `"muskan".endswith("kan")` | `True` |
| `s.count(x)` | How many times `x` appears | `"banana".count("a")` | `3` |
| `s.find(x)` | Index of first `x`, or `-1` if absent | `"muskan".find("k")` | `3` |
| `s.replace(a, b)` | Replace `a` with `b` | `"cat".replace("c", "b")` | `'bat'` |
| `s.strip()` | Remove spaces at both ends | `" hi ".strip()` | `'hi'` |
| `s.lstrip()` | Remove spaces on the left | `" hi ".lstrip()` | `'hi '` |
| `s.rstrip()` | Remove spaces on the right | `" hi ".rstrip()` | `' hi'` |
| `str(x)` | Convert to a string | `str(123)` | `'123'` |

## Important Points

* Methods return new strings. The original stays the same.
* `count()` and `find()` are **case-sensitive**: `"Muskan".find("m")` gives `-1`.
* `find()` returns `-1` when not found, while `index()` raises an error.
* Methods can be chained: `" HELLO ".strip().lower()` gives `'hello'`.

```python
name = "muskan"
name.upper()
print(name)    # muskan  (unchanged)

name = name.upper()
print(name)    # MUSKAN  (saved by reassigning)
```

## Common Mistakes

| Mistake | Fix |
| ------- | --- |
| Calling `name.upper()` and expecting `name` to change | Assign the result: `name = name.upper()` |
| Forgetting the brackets `()` | `name.upper` without brackets is not a call. |
| Expecting `count("A")` to match `"a"` | Matching is case-sensitive. |

## Summary

* String methods are called with `string.method()`.
* They return new values and never modify the original.
* Use `print()` to see the results.
