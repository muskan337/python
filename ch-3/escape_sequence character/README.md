# Escape Sequence Characters

## What are They?

An **escape sequence** is a backslash `\` followed by a character. It stands for a special character that is hard to type inside a string, like a new line or a tab.

## The Code

```python
a = "Muskan is learnig python\nbcoz she wants to \tlearn \"Data Science\""
  # \n -> for new line
  #\t -> gives tab jitna space
print(a)
```

## Output

```text
Muskan is learnig python
bcoz she wants to 	learn "Data Science"
```

The gap before `learn` is a tab.

## Common Escape Sequences

| Sequence | Meaning | Example | Result |
| -------- | ------- | ------- | ------ |
| `\n` | New line | `"Hi\nBye"` | `Hi` then `Bye` on the next line |
| `\t` | Tab (wide space) | `"A\tB"` | `A    B` |
| `\"` | Double quote | `"He said \"Hi\""` | `He said "Hi"` |
| `\'` | Single quote | `'It\'s ok'` | `It's ok` |
| `\\` | Backslash | `"C:\\Users"` | `C:\Users` |

## Why Do We Need `\"`?

Without the backslash, Python thinks the string has ended:

```python
# print("She said "Hello"")   # SyntaxError
print("She said \"Hello\"")   # She said "Hello"
```

Another way is to use different outer quotes:

```python
print('She said "Hello"')     # She said "Hello"
```

## Raw Strings

Put `r` before the quote to print backslashes exactly as written:

```python
print(r"C:\new\table")   # C:\new\table
```

## Common Mistakes

| Mistake | Fix |
| ------- | --- |
| Using `/n` instead of `\n` | Escape sequences use a **backslash**. |
| Forgetting to escape quotes inside the same type of quotes | Use `\"` or switch the outer quotes. |
| Writing a Windows path with single `\` | Use `\\` or a raw string. |

## Summary

* `\` starts an escape sequence.
* `\n` = new line, `\t` = tab, `\"` = quote, `\\` = backslash.
* Escape sequences only work inside strings.
