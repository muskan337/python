# Variables

## What is a Variable?

A **variable** is a name that stores a value so you can use it later. Think of it as a labelled box.

```python
age = 18
```

Here `age` is the variable and `18` is the value stored in it.

## The Code

```python
a = 1

b = 2

name = "harry";

print(a+b)
print(name)
```

## Output

```text
3
harry
```

## Explanation

| Line | Meaning |
| ---- | ------- |
| `a = 1` | Stores the integer `1` in `a`. |
| `b = 2` | Stores the integer `2` in `b`. |
| `name = "harry";` | Stores the text `harry`. The `;` at the end is allowed but unnecessary. |
| `print(a+b)` | Adds the numbers and prints `3`. |
| `print(name)` | Prints `harry`. |

Blank lines between statements are ignored by Python. They only make code easier to read.

## Rules for Variable Names

| Rule | Valid | Invalid |
| ---- | ----- | ------- |
| Can use letters, digits, underscore | `student_1` | `student-1` |
| Cannot start with a digit | `name1` | `1name` |
| No special symbols like `@`, `#`, `$` | `musk_an` | `musk@n` |
| No spaces | `full_name` | `full name` |
| Cannot be a Python keyword | `class_name` | `class`, `if`, `for` |
| Case-sensitive | `Age` and `age` are different | |

## Good Naming Habits

```python
total_marks = 450       # clear
tm = 450                # unclear
```

* Use lowercase with underscores (`first_name`).
* Choose names that describe the value.
* Do not reuse built-in names like `list`, `str`, `int`.

## Variables Can Change

```python
x = 10
print(x)    # 10

x = 20
print(x)    # 20

x = "now text"
print(x)    # now text
```

Python allows the same variable to hold different types at different times.

## Multiple Assignment

```python
a, b, c = 1, 2, 3
x = y = 0
```

## Common Mistakes

| Mistake | Fix |
| ------- | --- |
| Using a variable before creating it (`NameError`) | Assign a value first. |
| Writing `name = harry` without quotes | Text needs quotes: `"harry"`. |
| Mixing up `=` and `==` | `=` assigns, `==` compares. |

## Summary

* A variable stores a value under a name.
* `=` assigns a value.
* Follow the naming rules and use meaningful names.
* Variables can be reassigned to new values.
