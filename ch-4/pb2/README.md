# Practice Problem 2: Collect Marks

## Problem

Take the marks of 6 students from the user and store them in a list.

## The Code

```python
marks = []

m1 = input("Enter the marks of student 1 : ")
marks.append(m1)
m2 = input("Enter the marks of student 1 : ")
marks.append(m2)
m3 = input("Enter the marks of student 1 : ")
marks.append(m3)
m4 = input("Enter the marks of student 1 : ")
marks.append(m4)
m5 = input("Enter the marks of student 1 : ")
marks.append(m5)
m6 = input("Enter the marks of student 1 : ")
marks.append(m6)

print(marks)
```

## Sample Run

```text
Enter the marks of student 1 : 85
Enter the marks of student 1 : 90
Enter the marks of student 1 : 78
Enter the marks of student 1 : 66
Enter the marks of student 1 : 92
Enter the marks of student 1 : 70
['85', '90', '78', '66', '92', '70']
```

## Two Issues in This Code

| Issue | Why it matters | Fix |
| ----- | -------------- | --- |
| The prompt says "student 1" all six times | The user cannot tell which student they are entering. | Use student 1, 2, 3, ... 6. |
| Marks are stored as **strings** (`'85'`, not `85`) | `input()` always returns a string, so `sum(marks)` would fail with a `TypeError`. | Convert with `int()`. |

## Improved Version

```python
marks = []

for i in range(1, 7):
    m = int(input(f"Enter the marks of student {i} : "))
    marks.append(m)

print(marks)                       # [85, 90, 78, 66, 92, 70]
print("Total:", sum(marks))        # Total: 481
print("Highest:", max(marks))      # Highest: 92
```

## Summary

* `input()` gives strings. Convert marks with `int()` before doing maths.
* Make prompts specific so the user knows what to enter.
* Once numbers are in a list, `sum()`, `max()` and `min()` work on it.
