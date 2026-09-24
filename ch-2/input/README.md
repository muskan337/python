# Python Input, Type Conversion and f-strings

> Study notes for beginners. Use this README together with your Python file: read the explanation here, then run and experiment with the code.

---

## 1. What Does This File Do?

This file shows three basic ideas:

1. Taking input from the user with `input()`
2. Why input is always a **string**, and how to convert it with `int()`
3. Printing a message with a variable inside it using an **f-string**

### The Code

```python
# a = input("enter number 1: ")      # input as string

# b = int(input("enter number 2: "))

# print("No.a is:  ", a)             # 1
# print("No. b is: ", b)             # 2

# print("Sum is ", a + b)            # error (see Section 5)

name = input("Enter ur name : ")
print(f"good afternoon, {name}")
```

> Lines starting with `#` are **comments**. Python ignores them. In this file, only the last two lines actually run. The commented lines are kept as experiments.

### Sample Run

```text
Enter ur name : Asha
good afternoon, Asha
```

---

## 2. `input()` Function

### What is it?

`input()` pauses the program, shows a message (called a **prompt**), and waits for the user to type something and press Enter.

```python
name = input("Enter your name: ")
print(name)
```

| Part | Meaning |
| ---- | ------- |
| `input(...)` | Function that reads what the user types |
| `"Enter your name: "` | The prompt shown to the user |
| `name = ...` | Stores the typed value in the variable `name` |

### Important Characteristic

`input()` **always returns a string (`str`)**, no matter what the user types.

```python
x = input("Enter a number: ")   # user types 25

print(x)          # 25
print(type(x))    # <class 'str'>
```

Even though `25` looks like a number, Python stores it as the text `"25"`.

---

## 3. Converting Input to a Number

To do maths, convert the string into a number using `int()` (whole numbers) or `float()` (decimals).

```python
b = int(input("enter number 2: "))   # user types 5

print(b)          # 5
print(type(b))    # <class 'int'>
```

What happens step by step:

| Step | What Python does | Result |
| ---- | ---------------- | ------ |
| 1 | `input("enter number 2: ")` reads the text | `"5"` (string) |
| 2 | `int("5")` converts the text | `5` (integer) |
| 3 | Result is stored in `b` | `b = 5` |

### Decimal Numbers

```python
price = float(input("Enter price: "))   # user types 9.99
print(price + 1)                        # 10.99
```

### When Conversion Fails

```python
# int("hello")   # ValueError: invalid literal for int()
# int("3.7")     # ValueError (a decimal string cannot go directly to int)
# int("")        # ValueError (user just pressed Enter)
```

| User types | `int(...)` result |
| ---------- | ----------------- |
| `25` | Works, gives `25` |
| `-4` | Works, gives `-4` |
| `3.7` | `ValueError` |
| `abc` | `ValueError` |
| *(nothing)* | `ValueError` |

---

## 4. `print()` Function

`print()` displays values on the screen.

### Using Commas

Separating items with commas prints them with a **space** between them. Different types are fine.

```python
a = "1"
b = 2

print("No.a is: ", a)    # No.a is:  1
print("No. b is: ", b)   # No. b is:  2
```

> The message ends with a space and `print` adds another one, so you see two spaces. This is why the output looks slightly wider.

### Comma vs `+` in `print()`

| Style | Example | Works with mixed types? |
| ----- | ------- | ----------------------- |
| Comma | `print("Age:", 18)` | Yes |
| Plus (`+`) | `print("Age: " + 18)` | No, `TypeError` |
| Plus with `str()` | `print("Age: " + str(18))` | Yes |

---

## 5. Why `a + b` Gives an Error (Commented Code)

The commented-out part of the file had:

```python
a = input("enter number 1: ")     # a is a string, e.g. "1"
b = int(input("enter number 2: "))  # b is an int, e.g. 2

print("Sum is ", a + b)
```

`a` is a **string** and `b` is an **integer**. Python cannot add text and a number, so this raises:

```text
TypeError: can only concatenate str (not "int") to str
```

> **Correction to the original comment:** the note `# 12` next to this line is not accurate for this exact code. `"1" + 2` does **not** produce `12`, it produces an error. You only get `12` when **both** values are strings.

### What `+` Does Depends on the Type

```python
print("1" + "2")   # 12   -> both strings: joined together (concatenation)
print(1 + 2)       # 3    -> both ints: added
# print("1" + 2)   # TypeError -> mixed types
```

### Three Ways to Fix It

```python
a = input("enter number 1: ")
b = int(input("enter number 2: "))

# Fix 1: convert a to int, then add
print("Sum is ", int(a) + b)

# Fix 2: convert both when reading input
a = int(input("enter number 1: "))
b = int(input("enter number 2: "))
print("Sum is ", a + b)

# Fix 3: convert both to strings to join them as text
print("Joined is ", a + str(b))
```

---

## 6. f-strings (Formatted Strings)

### What is it?

An **f-string** lets you put variables directly inside a string. Put the letter `f` before the opening quote and write variables inside `{ }`.

```python
name = input("Enter ur name : ")
print(f"good afternoon, {name}")
```

If the user types `Asha`, Python replaces `{name}` with `Asha`:

```text
good afternoon, Asha
```

### Rules

| Rule | Example |
| ---- | ------- |
| Start with `f` before the quote | `f"Hello"` |
| Put variable names inside `{ }` | `f"Hello {name}"` |
| Works with any type (no `str()` needed) | `f"Age is {age}"` |
| Can contain expressions | `f"Sum is {a + b}"` |

### Examples

```python
name = "Asha"
age = 18

print(f"My name is {name} and I am {age}.")
print(f"Next year I will be {age + 1}.")
print(f"Name in capitals: {name.upper()}")
```

Output:

```text
My name is Asha and I am 18.
Next year I will be 19.
Name in capitals: ASHA
```

### Without f-string vs With f-string

```python
name = "Asha"

print("good afternoon, " + name)     # concatenation
print("good afternoon,", name)       # comma
print(f"good afternoon, {name}")     # f-string (cleanest)
```

All three print similar output, but f-strings are easiest to read once you have several variables.

### Forgetting the `f`

```python
name = "Asha"

print("good afternoon, {name}")    # good afternoon, {name}   (wrong)
print(f"good afternoon, {name}")   # good afternoon, Asha     (correct)
```

---

## 7. Examples

### Example 1: Greeting

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

### Example 2: Adding Two Numbers

```python
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print(f"Sum is {a + b}")
```

### Example 3: Checking Types

```python
x = input("Enter something: ")
y = int(x) if x.isdigit() else None

print(f"x is {type(x).__name__}")
print(f"y is {y}")
```

> `x.isdigit()` returns `True` if the string contains only digits. This avoids a crash on bad input.

### Example 4: Area of a Rectangle (with decimals)

```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))

print(f"Area is {length * width}")
```

### Example 5: Safe Conversion with `try` / `except`

```python
try:
    num = int(input("Enter a number: "))
    print(f"Double is {num * 2}")
except ValueError:
    print("That was not a valid whole number.")
```

---

## 8. Common Mistakes

| # | Mistake | Explanation / Fix |
| - | ------- | ----------------- |
| 1 | Forgetting that `input()` returns a string | Convert with `int()` or `float()` before maths. |
| 2 | Adding a string and an int (`"1" + 2`) | Raises `TypeError`. Convert one side first. |
| 3 | Expecting `"1" + "2"` to give `3` | It joins the strings and gives `"12"`. |
| 4 | Using `int()` on a decimal string like `"3.7"` | Raises `ValueError`. Use `float()`, or `int(float("3.7"))`. |
| 5 | Forgetting the `f` in an f-string | `"{name}"` prints the braces as plain text. |
| 6 | Using `int()` when the user types text | Crashes with `ValueError`. Use `try` / `except`. |
| 7 | Forgetting the quotes in the prompt | `input(Enter name)` is a `SyntaxError`. Use `input("Enter name")`. |
| 8 | Using `+` in `print()` with a number | `print("Age: " + 18)` fails. Use a comma, `str()`, or an f-string. |
| 9 | Naming a variable `input` | It hides the built-in `input()` function. |
| 10 | Not leaving a space at the end of the prompt | `"Enter name:"` makes the typed text touch the colon. Use `"Enter name: "`. |

---

## 9. Important Points for Exams/Interviews

* `input()` **always** returns a `str`.
* Use `int()` or `float()` to convert input to a number.
* `int("3.7")` raises `ValueError`, but `int(3.7)` gives `3`.
* `+` **adds** numbers but **joins** strings. Mixing the two raises `TypeError`.
* `"1" + "2"` is `"12"`, while `1 + 2` is `3`.
* `print("a", "b")` separates items with a space by default.
* An **f-string** starts with `f` and uses `{ }` for variables and expressions.
* f-strings were added in **Python 3.6**.
* Anything after `#` on a line is a comment and is ignored.
* Invalid conversions raise `ValueError`. Wrong operations between types raise `TypeError`.

---

## 10. Practice Questions

1. What type does `input()` always return? Prove it with a small program.
2. What is the output?
   ```python
   a = "10"
   b = "20"
   print(a + b)
   ```
3. What is the output, and why?
   ```python
   a = 10
   b = 20
   print(a + b)
   ```
4. Why does this code raise an error? Fix it in two different ways.
   ```python
   a = input("Enter a number: ")
   print(a + 5)
   ```
5. What is the difference between `print("Hi", name)` and `print(f"Hi {name}")`?
6. What is wrong with this line?
   ```python
   print("Hello, {name}")
   ```
7. What happens when the user types `abc` for this code? How can you handle it?
   ```python
   n = int(input("Enter number: "))
   ```
8. Write a program that takes two numbers and prints their product using an f-string.
9. Write a program that takes a name and an age, and prints `Asha will be 19 next year.` (for `Asha` and `18`).
10. What is the difference between `int("5")`, `int(5.9)` and `int("5.9")`?

---

## 11. Summary

* `input()` reads what the user types and gives it back as a **string**.
* Convert with `int()` or `float()` when you need to do maths.
* `+` on two strings **joins** them. `+` on two numbers **adds** them. Mixed types cause `TypeError`.
* Invalid text passed to `int()` or `float()` causes `ValueError`.
* `print()` with commas adds a space between items and accepts mixed types.
* **f-strings** (`f"... {variable} ..."`) are the clearest way to put values inside text.

| Quick Revision | |
| -------------- | - |
| Read text | `input("prompt")` |
| Read whole number | `int(input("prompt"))` |
| Read decimal number | `float(input("prompt"))` |
| Print with variable | `print(f"Hello {name}")` |
| Join strings | `"a" + "b"` gives `"ab"` |
| Mixed `+` | `TypeError` |
