# Chapter 1: Getting Started

This chapter covers the very first steps: printing text, writing comments, multi-line strings, and using an external module.

## Files in This Chapter

| File | What it does |
| ---- | ------------ |
| `.py` | Fetches a joke with `pyjokes` and prints a multi-line poem |
| `pblm/pblm.py` | Speaks a sentence using `pyttsx3` |
| `python/python.py` | Empty file (placeholder) |

---

## 1. `.py` File

```python
import pyjokes

joke = pyjokes.get_joke()
print("joke")

# multi line string
print('''Twinkle, twinkle, little star,
How I wonder what you are!
... (rest of the poem) ...
''')
```

### What Each Part Does

| Line | Meaning |
| ---- | ------- |
| `import pyjokes` | Loads an external package. Install it first with `pip install pyjokes`. |
| `pyjokes.get_joke()` | Returns a random joke as a string. |
| `print("joke")` | Prints the **word** `joke`, not the joke. |
| `# multi line string` | A comment. Python ignores it. |
| `print('''...''')` | Triple quotes let a string span many lines. |

### Important: A Bug to Fix

`print("joke")` prints the literal text `joke` because it is inside quotes. To print the actual joke, remove the quotes:

```python
print(joke)
```

### Multi-line Strings

Text inside `'''...'''` (or `"""..."""`) keeps its line breaks exactly as typed.

```python
poem = '''Roses are red,
Violets are blue.'''

print(poem)
```

Output:

```text
Roses are red,
Violets are blue.
```

### Comments

```python
# This is a single-line comment
print("Hello")   # This is a comment after code
```

### File Name Note

The file is named just `.py`, which has no real name. Rename it (for example `twinkle.py`) so it is easy to run and find.

---

## Key Points

* `import` brings in extra code written by others.
* External packages must be installed with `pip` before importing.
* Text in quotes is printed as text, not treated as a variable.
* Triple quotes create multi-line strings.
* `#` starts a comment.

## Summary

You learned to print text, comment code, use multi-line strings, and import a package. Next, see [`pblm`](pblm) for another package example.
