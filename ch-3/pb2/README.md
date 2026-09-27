# Practice Problem 2: Letter Template

## Problem

Store a letter with placeholders `<|Name|>` and `<|Date|>`, then replace them with real values.

## The Code

```python
Letter = ''' Dear <|Name|>,
            You are selected!
            <|Date|> '''

print(Letter.replace("<|Name|>", "Muskan").replace("<|Date|>", "22/9/26"))
```

## Output

```text
 Dear Muskan,
            You are selected!
            22/9/26 
```

## Explanation

| Part | Meaning |
| ---- | ------- |
| `'''...'''` | Triple quotes allow the letter to span several lines. |
| `<|Name|>`, `<|Date|>` | Placeholders. They are just text that we choose to replace. |
| `.replace(old, new)` | Returns a **new** string with `old` replaced by `new`. |
| `.replace(...).replace(...)` | **Chaining**: the second `replace` works on the result of the first. |

## Important Points

* Strings are immutable, so `replace()` does not change `Letter`. It returns a new string.
* The spaces at the start of each line are part of the string, so they appear in the output.
* `replace()` replaces **all** matches by default.

```python
print(Letter)   # still shows the placeholders
```

## Improvement: Ask the User

```python
name = input("Enter name: ")
date = input("Enter date: ")

letter = """Dear <|Name|>,
You are selected!
<|Date|>"""

print(letter.replace("<|Name|>", name).replace("<|Date|>", date))
```

## Summary

* Triple quotes create multi-line strings.
* `replace()` returns a new string and can be chained.
* Placeholders are a simple way to build templates.
