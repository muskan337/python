# Practice Problem 1: Greeting

## Problem

Take the user's name as input and print a greeting.

## The Code

```python
name  = input("enter your name: ")
print(f"good afternoon,  {name}")
```

## Sample Run

```text
enter your name: Asha
good afternoon,  Asha
```

## Explanation

| Line | Meaning |
| ---- | ------- |
| `input("enter your name: ")` | Shows the prompt and reads the typed text as a string. |
| `name = ...` | Stores it in `name`. |
| `f"good afternoon,  {name}"` | An f-string that inserts the value of `name`. |

Note: there are **two spaces** after the comma in the f-string, so the output has a double space. Use one space for a clean look:

```python
print(f"good afternoon, {name}")
```

## Other Ways to Write It

```python
print("good afternoon, " + name)
print("good afternoon,", name)
```

## Summary

* `input()` returns a string.
* Use an f-string to put variables inside text.
* Full explanation: see [ch-2/input](../../ch-2/input).
