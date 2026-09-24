# Operators

## What are Operators?

**Operators** are symbols that perform an action on values. In `5 + 3`, the `+` is the operator and `5` and `3` are the **operands**.

## The Code

```python
#Arithematic operator

a = 34
b = 4
c = a+b
print(c)

# assignment operators

a = 4-1
print(a)
b = 6
b+=3

print(b)

# comparison operator(==, =>, >, <, !=) retuen boolean
d = 5<4
print(d)

# logical operators ans, or, not

e = True or False
print(e)
```

## Output

```text
38
3
9
False
True
```

## Step-by-Step

| Code | What happens | Printed |
| ---- | ------------ | ------- |
| `c = a+b` | 34 + 4 | `38` |
| `a = 4-1` | `a` is reassigned to 3 | `3` |
| `b = 6` then `b += 3` | `b += 3` means `b = b + 3` | `9` |
| `d = 5<4` | Is 5 less than 4? No | `False` |
| `e = True or False` | `or` is True if either side is True | `True` |

---

## 1. Arithmetic Operators

Used for maths.

| Operator | Meaning | Example | Result |
| -------- | ------- | ------- | ------ |
| `+` | Addition | `7 + 2` | `9` |
| `-` | Subtraction | `7 - 2` | `5` |
| `*` | Multiplication | `7 * 2` | `14` |
| `/` | Division (always float) | `7 / 2` | `3.5` |
| `//` | Floor division | `7 // 2` | `3` |
| `%` | Remainder (modulus) | `7 % 2` | `1` |
| `**` | Power | `7 ** 2` | `49` |

## 2. Assignment Operators

Used to store or update values.

| Operator | Example | Same as |
| -------- | ------- | ------- |
| `=` | `x = 5` | store 5 in x |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |

## 3. Comparison Operators

Compare two values and return `True` or `False`.

| Operator | Meaning | Example | Result |
| -------- | ------- | ------- | ------ |
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `5 <= 3` | `False` |

> **Correction:** the comment in the file lists `=>`. That is not valid Python. The correct operator is `>=`. Writing `5 => 3` gives a `SyntaxError`.

## 4. Logical Operators

Combine conditions. The file's comment says "ans", which should be **and**.

| Operator | Meaning | Example | Result |
| -------- | ------- | ------- | ------ |
| `and` | True only if **both** are True | `True and False` | `False` |
| `or` | True if **at least one** is True | `True or False` | `True` |
| `not` | Reverses the value | `not True` | `False` |

```python
age = 20
print(age > 18 and age < 30)   # True
print(age < 18 or age > 60)    # False
print(not age > 18)            # False
```

---

## Common Mistakes

| Mistake | Explanation |
| ------- | ----------- |
| Using `=` instead of `==` in a comparison | `=` assigns, `==` compares. |
| Writing `=>` | The correct form is `>=`. |
| Expecting `7 / 2` to be `3` | `/` gives `3.5`. Use `//` for `3`. |
| Writing `ans` | The keyword is `and`. |

## Summary

* Arithmetic: `+ - * / // % **`
* Assignment: `= += -= *= /=`
* Comparison: `== != > < >= <=` (return `True` or `False`)
* Logical: `and`, `or`, `not`
