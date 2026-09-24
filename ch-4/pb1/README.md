# Practice Problem 1: Collect Fruits

## Problem

Take 5 fruit names from the user and store them in a list.

## The Code (in the file)

The whole program is currently **commented out**, so running the file prints nothing.

```python
fruits = []

f1 = input("enter the fruits name")
fruits.append(f1)
f2 = input("enter the fruits name")
fruits.append(f2)
f3 = input("enter the fruits name")
fruits.append(f3)
f4 = input("enter the fruits name")
fruits.append(f4)
f5 = input("enter the fruits name")
fruits.append(f5)

print(fruits)
```

To run it, remove the `#` at the start of each line.

## Sample Run

```text
enter the fruits nameapple
enter the fruits namemango
enter the fruits namebanana
enter the fruits namekiwi
enter the fruits namegrapes
['apple', 'mango', 'banana', 'kiwi', 'grapes']
```

## How It Works

| Step | Meaning |
| ---- | ------- |
| `fruits = []` | Creates an empty list. |
| `input(...)` | Reads one fruit name. |
| `fruits.append(f1)` | Adds it to the end of the list. |
| `print(fruits)` | Prints the final list. |

## Improvements

1. Add a space at the end of the prompt so typing does not touch the text: `"enter the fruit name: "`.
2. Once you learn loops, the same program is much shorter:

```python
fruits = []

for i in range(5):
    fruits.append(input("Enter fruit name: "))

print(fruits)
```

## Summary

* Start with an empty list and grow it using `append()`.
* Repeating the same lines is a sign that a loop would help.
