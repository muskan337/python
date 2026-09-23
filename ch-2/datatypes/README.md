# Python Data Types

> Study notes for beginners. Use this README together with `datatypes.py`: read the explanation here, then run and experiment with the code in that file.

---

## 1. What are Data Types?

### Simple Definition

A **data type** tells Python what *kind* of value something is (a whole number, some text, a list of items, and so on) and what you can do with it.

For example:

* You can **add** two numbers: `5 + 3`
* You can **join** two pieces of text: `"Hello " + "World"`
* But you **cannot** add a number to text: `5 + "3"` gives an error

### Why are Data Types Important?

| Reason | Explanation |
| ------ | ----------- |
| Correct operations | Each type supports different operations (numbers can be divided, strings cannot). |
| Memory and behavior | Python stores and handles each type differently. |
| Fewer bugs | Knowing the type helps you predict results and avoid errors. |
| Right tool for the job | Lists, sets and dictionaries each solve different problems. |

### How Does Python Decide the Type?

Python is **dynamically typed**. This means:

* You do **not** write the type when creating a variable.
* Python looks at the **value** you assign and decides the type automatically, while the program runs.
* The same variable can later hold a different type of value.

```python
x = 10          # Python sees a whole number -> int
print(type(x))  # <class 'int'>

x = "Hello"     # Now x holds text -> str
print(type(x))  # <class 'str'>
```

> The type belongs to the **value**, not to the variable name. The variable is just a label pointing to a value.

---

## 2. Main Data Types in Python

Here is the big picture before we go into detail:

| Category | Types |
| -------- | ----- |
| Numeric | `int`, `float`, `complex` |
| Boolean | `bool` |
| Sequence | `str`, `list`, `tuple`, `range` |
| Set | `set`, `frozenset` |
| Mapping | `dict` |
| None | `NoneType` |

---

### 1. Numeric Types

Numeric types store numbers.

#### `int` (Integer)

**What it is:** Whole numbers, positive or negative, with no decimal point.

```python
age = 18
temperature = -5
count = 0

print(type(age))   # <class 'int'>
```

**Important characteristics:**

* Can be positive, negative, or zero.
* Has **no size limit** in Python. It can be as big as your memory allows.
* Dividing with `/` always gives a `float`, even for whole results. Use `//` for whole-number division.

```python
big_number = 2 ** 100
print(big_number)   # 1267650600228229401496703205376

print(10 / 2)       # 5.0  (float)
print(10 // 3)      # 3    (whole-number division)
```

#### `float` (Floating-Point Number)

**What it is:** Numbers with a decimal point.

```python
price = 99.99
pi = 3.14159
small = 2.5e-3      # scientific notation = 0.0025

print(type(price))  # <class 'float'>
```

**Important characteristics:**

* Used for measurements, prices, averages, and so on.
* Floats are stored approximately, so tiny rounding errors can appear.

```python
print(0.1 + 0.2)    # 0.30000000000000004  (not exactly 0.3)
```

> Because of this, avoid comparing floats with `==`. This is a common surprise for beginners.

#### `complex` (Complex Number)

**What it is:** A number with a real part and an imaginary part. The imaginary part is written with `j`.

```python
z = 3 + 4j

print(type(z))      # <class 'complex'>
print(z.real)       # 3.0
print(z.imag)       # 4.0
print(abs(z))       # 5.0  (distance from 0)
```

**Important characteristics:**

* Rarely needed in everyday beginner programs.
* Mostly used in maths and science.

#### Numeric Types at a Glance

| Type | Example | Description |
| ---- | ------- | ----------- |
| `int` | `42` | Whole number |
| `float` | `3.14` | Number with decimal point |
| `complex` | `2 + 3j` | Real part + imaginary part |

---

### 2. Boolean Type

#### `bool`

**What it is:** A type that has only **two** possible values: `True` and `False`.

```python
is_student = True
is_raining = False

print(type(is_student))   # <class 'bool'>
```

**Important characteristics:**

* `True` and `False` must start with a **capital letter**.
* Usually the result of comparisons.
* `bool` is a subtype of `int`, so `True` behaves like `1` and `False` like `0`.

```python
print(5 > 3)        # True
print(5 == 10)      # False

print(True + True)  # 2
print(True == 1)    # True
```

#### Truthy and Falsy Values

Python can treat **any** value as `True` or `False` in conditions such as `if`. Use `bool()` to see how Python treats a value.

**Falsy values** (treated as `False`):

| Value | Type |
| ----- | ---- |
| `False` | bool |
| `0`, `0.0`, `0j` | numbers (zero) |
| `""` | empty string |
| `[]`, `()`, `{}`, `set()`, `range(0)` | empty collections |
| `None` | NoneType |

**Truthy values:** almost everything else.

```python
print(bool(0))        # False
print(bool(""))       # False
print(bool([]))       # False
print(bool(None))     # False

print(bool(5))        # True
print(bool("Hello"))  # True
print(bool([0]))      # True  (list is not empty, even though it holds 0)
print(bool("0"))      # True  (non-empty string)
```

A practical use:

```python
name = ""

if name:
    print("Name entered")
else:
    print("Name is empty")   # This runs
```

---

### 3. Sequence Types

A **sequence** is an *ordered* collection of items. Every item has a position number called an **index**, starting from `0`.

#### `str` (String)

**What it is:** Text, made of characters inside quotes.

```python
name = "Python"
message = 'Hello, World!'

print(type(name))     # <class 'str'>
print(name[0])        # P   (first character)
print(name[-1])       # n   (last character)
print(name[0:3])      # Pyt (slicing: index 0 up to, not including, 3)
print(len(name))      # 6
print(name.upper())   # PYTHON
```

**Important characteristics:**

* Ordered, and supports indexing and slicing.
* **Immutable** (you cannot change a character in place).
* Can use single `'...'`, double `"..."`, or triple `'''...'''` quotes.

#### `list`

**What it is:** An ordered collection of items that **can be changed**.

```python
fruits = ["apple", "banana", "cherry"]

print(type(fruits))     # <class 'list'>
print(fruits[1])        # banana

fruits.append("mango")  # add an item
fruits[0] = "grapes"    # change an item
print(fruits)           # ['grapes', 'banana', 'cherry', 'mango']
```

**Important characteristics:**

* Written with square brackets `[ ]`.
* **Mutable**, **ordered**, **allows duplicates**.
* Can hold different types together, e.g. `[1, "hi", 3.5, True]`.

#### `tuple`

**What it is:** An ordered collection of items that **cannot be changed** after creation.

```python
point = (10, 20)

print(type(point))   # <class 'tuple'>
print(point[0])      # 10

# point[0] = 99      # TypeError: 'tuple' object does not support item assignment
```

**Important characteristics:**

* Written with round brackets `( )`.
* **Immutable**, **ordered**, **allows duplicates**.
* A tuple with **one** item needs a trailing comma:

```python
single = (5,)     # tuple
not_tuple = (5)   # just the int 5

print(type(single))      # <class 'tuple'>
print(type(not_tuple))   # <class 'int'>
```

#### `range`

**What it is:** A sequence of numbers, mostly used in `for` loops.

```python
r = range(5)

print(type(r))       # <class 'range'>
print(list(r))       # [0, 1, 2, 3, 4]

print(list(range(1, 10, 2)))   # [1, 3, 5, 7, 9]  (start, stop, step)
```

**Important characteristics:**

* `range(start, stop, step)`. The `stop` value is **not** included.
* **Immutable** and **ordered**.
* It does not store every number in memory. It produces them when needed, so it is memory-efficient.

```python
for i in range(3):
    print(i)    # prints 0, then 1, then 2
```

#### Sequence Types Compared

| Feature | `str` | `list` | `tuple` | `range` |
| ------- | ----- | ------ | ------- | ------- |
| Brackets | `" "` | `[ ]` | `( )` | `range()` |
| Ordered | Yes | Yes | Yes | Yes |
| Mutable | No | **Yes** | No | No |
| Indexing | Yes | Yes | Yes | Yes |
| Holds | Characters only | Any types | Any types | Integers only |

---

### 4. Set Types

A **set** is a collection of **unique** items with **no fixed order**.

#### `set`

**What it is:** An unordered collection with no duplicates that you can modify.

```python
numbers = {1, 2, 2, 3, 3, 3}

print(numbers)        # {1, 2, 3}  (duplicates removed)
print(type(numbers))  # <class 'set'>

numbers.add(4)
numbers.remove(1)
print(numbers)        # {2, 3, 4}
```

**Important characteristics:**

* Written with curly brackets `{ }`.
* **Mutable**, **unordered**, **no duplicates**.
* **No indexing**: `numbers[0]` gives an error, because there is no position.
* The printed order may differ from the order you typed.
* Items must be **hashable**, which roughly means immutable. A set can hold numbers, strings, and tuples, but not lists.
* To create an **empty** set, use `set()`. Writing `{}` creates an empty **dictionary**.

```python
empty_set = set()
empty_dict = {}

print(type(empty_set))    # <class 'set'>
print(type(empty_dict))   # <class 'dict'>
```

Sets support maths-style operations:

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # {1, 2, 3, 4, 5}  union (everything)
print(a & b)   # {3}              intersection (common items)
print(a - b)   # {1, 2}           difference (in a, not in b)
```

#### `frozenset`

**What it is:** An **immutable** version of a set.

```python
fs = frozenset([1, 2, 3, 3])

print(fs)             # frozenset({1, 2, 3})
print(type(fs))       # <class 'frozenset'>

# fs.add(4)           # AttributeError: 'frozenset' object has no attribute 'add'
```

#### `set` vs `frozenset`

| Feature | `set` | `frozenset` |
| ------- | ----- | ----------- |
| Mutable | Yes | **No** |
| Ordered | No | No |
| Duplicates | No | No |
| Can add/remove items | Yes | No |
| Can be a dictionary key or a set item | No | **Yes** |

---

### 5. Mapping Type

#### `dict` (Dictionary)

**What it is:** A collection that stores data as **key-value pairs**, like a real dictionary where you look up a word (key) to get its meaning (value).

* **Key**: the label used to look something up. Keys must be **unique** and **immutable** (strings, numbers, and tuples are fine; lists are not).
* **Value**: the data stored for that key. Values can be of any type and can repeat.
* **Key-value pair**: one `key: value` entry.

```python
student = {
    "name": "Asha",
    "age": 18,
    "course": "BTech CSE"
}

print(type(student))          # <class 'dict'>
print(student["name"])        # Asha

student["age"] = 19           # change a value
student["city"] = "Delhi"     # add a new pair
print(student)

print(student.get("phone"))   # None  (safe lookup, no error if key is missing)
```

Useful ways to read a dictionary:

```python
print(student.keys())     # all keys
print(student.values())   # all values
print(student.items())    # all (key, value) pairs

for key, value in student.items():
    print(key, "->", value)
```

**Important characteristics:**

* Written with curly brackets and colons: `{key: value}`.
* **Mutable**.
* Keys are **unique**. If you repeat a key, the last value wins.
* Keeps items in **insertion order** (the order you added them) in Python 3.7 and later.
* Accessing a missing key with `student["phone"]` raises a `KeyError`.

---

### 6. None Type

#### `NoneType`

**What it is:** The type of the special value `None`, which means **"no value"** or **"nothing here"**.

```python
result = None

print(result)         # None
print(type(result))   # <class 'NoneType'>
```

**Important characteristics:**

* `None` is **not** the same as `0`, `""`, or `False`. It means "no value at all".
* It is falsy.
* There is only **one** `None` object, so check for it with `is`, not `==`.

```python
if result is None:
    print("No value yet")
```

**Common use cases:**

```python
# 1. A variable that will get a value later
answer = None

# 2. Functions that do not return anything give back None
def greet():
    print("Hello")

value = greet()       # prints Hello
print(value)          # None

# 3. "Not found" or "missing" signal
print({"a": 1}.get("b"))   # None
```

---

## 3. Quick Comparison Table

| Data Type | Example | Mutable? | Ordered? | Allows Duplicates? |
| --------- | ------- | -------- | -------- | ------------------ |
| `int` | `10` | No | N/A (single value) | N/A |
| `float` | `3.14` | No | N/A (single value) | N/A |
| `complex` | `2+3j` | No | N/A (single value) | N/A |
| `bool` | `True` | No | N/A (single value) | N/A |
| `str` | `"Hello"` | No | Yes | Yes |
| `list` | `[1, 2, 2]` | **Yes** | Yes | Yes |
| `tuple` | `(1, 2, 2)` | No | Yes | Yes |
| `range` | `range(5)` | No | Yes | No (values are unique) |
| `set` | `{1, 2, 3}` | **Yes** | No | No |
| `frozenset` | `frozenset({1, 2})` | No | No | No |
| `dict` | `{"a": 1}` | **Yes** | Yes (insertion order, Python 3.7+) | Keys: No, Values: Yes |
| `NoneType` | `None` | No | N/A (single value) | N/A |

---

## 4. How to Check Data Type

### `type()`

The `type()` function tells you the exact type of a value or variable.

```python
print(type(10))            # <class 'int'>
print(type(3.14))          # <class 'float'>
print(type("Hello"))       # <class 'str'>
print(type([1, 2, 3]))     # <class 'list'>
print(type((1, 2, 3)))     # <class 'tuple'>
print(type({1, 2, 3}))     # <class 'set'>
print(type({"a": 1}))      # <class 'dict'>
print(type(None))          # <class 'NoneType'>
```

You can also compare types:

```python
x = 10
print(type(x) == int)      # True
```

### `isinstance()`

`isinstance(value, type)` checks whether a value **belongs to** a type. It returns `True` or `False`.

```python
x = 10

print(isinstance(x, int))            # True
print(isinstance(x, str))            # False
print(isinstance(x, (int, float)))   # True  (checks against several types at once)
```

### `type()` vs `isinstance()`

| Feature | `type()` | `isinstance()` |
| ------- | -------- | -------------- |
| Returns | The type itself | `True` or `False` |
| Exact match only? | Yes | No. It also accepts subtypes |
| Check multiple types at once | No | Yes (use a tuple) |
| Best for | Seeing what a value is | Checking a value in `if` conditions |

The key difference shows up with `bool`, which is a subtype of `int`:

```python
print(type(True) == int)        # False  (exact type is bool)
print(isinstance(True, int))    # True   (bool counts as a kind of int)
print(isinstance(True, bool))   # True
```

> Prefer `isinstance()` when you just want to check "is this value a kind of X?".

---

## 5. Type Conversion / Type Casting

**Type conversion** means changing a value from one type to another using a built-in function such as `int()`, `float()`, `str()`, `list()`, `tuple()`, or `set()`.

Conversion creates a **new** value. The original is not changed.

### Conversion Examples

```python
# int -> float
print(float(5))            # 5.0

# float -> int (decimal part is cut off, NOT rounded)
print(int(3.9))            # 3
print(int(-3.9))           # -3

# string -> int
print(int("42"))           # 42

# string -> float
print(float("3.14"))       # 3.14

# int -> string
print(str(100))            # '100'

# list -> tuple
print(tuple([1, 2, 3]))    # (1, 2, 3)

# tuple -> list
print(list((1, 2, 3)))     # [1, 2, 3]

# list -> set (duplicates removed, order not guaranteed)
print(set([1, 2, 2, 3]))   # {1, 2, 3}
```

### Summary Table

| Conversion | Function | Example | Result |
| ---------- | -------- | ------- | ------ |
| int → float | `float()` | `float(5)` | `5.0` |
| float → int | `int()` | `int(3.9)` | `3` |
| string → int | `int()` | `int("42")` | `42` |
| string → float | `float()` | `float("3.14")` | `3.14` |
| int → string | `str()` | `str(100)` | `'100'` |
| list → tuple | `tuple()` | `tuple([1, 2])` | `(1, 2)` |
| tuple → list | `list()` | `list((1, 2))` | `[1, 2]` |
| list → set | `set()` | `set([1, 1, 2])` | `{1, 2}` |

### When Conversion Causes Errors

```python
# Text that is not a valid number
# int("hello")        # ValueError

# A decimal string cannot go directly to int
# int("3.7")          # ValueError
print(int(float("3.7")))   # 3  (convert to float first, then to int)

# None cannot be converted to a number
# int(None)           # TypeError

# A list containing a list cannot become a set (lists are unhashable)
# set([[1, 2], [3]])  # TypeError
```

| Situation | Error |
| --------- | ----- |
| `int("abc")` | `ValueError` |
| `int("3.7")` | `ValueError` |
| `float("abc")` | `ValueError` |
| `int(None)` | `TypeError` |
| `set([[1, 2], [3, 4]])` | `TypeError` |

**Things to remember:**

* `int(3.9)` gives `3`. It **truncates**, it does not round. Use `round()` to round.
* Converting to a `set` **removes duplicates** and **loses the order**.
* `input()` always returns a **string**, so convert it before doing maths:

```python
age = input("Enter age: ")   # user types 18 -> age is the string "18"
age = int(age)               # now it is the number 18
```

---

## 6. Mutable vs Immutable Data Types

### What does Mutable mean?

A **mutable** object can be **changed after it is created**. You can add, remove, or modify its contents without creating a new object.

### What does Immutable mean?

An **immutable** object **cannot be changed** after it is created. Any "change" actually creates a **new** object.

### Which Types are Which?

| Mutable | Immutable |
| ------- | --------- |
| `list` | `int` |
| `set` | `float` |
| `dict` | `complex` |
| | `bool` |
| | `str` |
| | `tuple` |
| | `range` |
| | `frozenset` |
| | `NoneType` |

### Mutable Example (`list`)

```python
numbers = [1, 2, 3]
print(id(numbers))     # some memory address, e.g. 140234...

numbers.append(4)      # modifies the SAME list
print(numbers)         # [1, 2, 3, 4]
print(id(numbers))     # same address as before
```

### Immutable Example (`str` and `tuple`)

```python
name = "Python"
# name[0] = "J"        # TypeError: 'str' object does not support item assignment

name = "J" + name[1:]  # builds a NEW string
print(name)            # Jython
```

```python
point = (1, 2, 3)
# point[0] = 99        # TypeError
```

### Immutable Numbers Example

```python
x = 10
print(id(x))

x = x + 1              # creates a NEW int object
print(id(x))           # different address
```

> `id()` shows an object's identity (memory address). Same `id` after a change means the object was modified in place (mutable). A different `id` means a new object was created (immutable).

### Watch Out: Mutable Objects Share Changes

When you write `b = a` for a list, both names point to the **same** list:

```python
a = [1, 2, 3]
b = a            # NOT a copy, both names refer to one list

b.append(4)
print(a)         # [1, 2, 3, 4]  <- a changed too!

c = a.copy()     # a real, independent copy
c.append(5)
print(a)         # [1, 2, 3, 4]  (unchanged)
```

---

## 7. Examples

> These examples are meant to be run. You can also try them in your `datatypes.py` file.

### Example 1: One Variable of Each Type

```python
age = 18                          # int
height = 5.9                      # float
z = 2 + 3j                        # complex
is_student = True                 # bool
name = "Asha"                     # str
marks = [85, 90, 78]              # list
coordinates = (10, 20)            # tuple
digits = range(5)                 # range
unique_ids = {101, 102, 103}      # set
frozen_ids = frozenset([1, 2])    # frozenset
profile = {"name": "Asha"}        # dict
nothing = None                    # NoneType

values = [age, height, z, is_student, name, marks,
          coordinates, digits, unique_ids, frozen_ids, profile, nothing]

for v in values:
    print(v, "->", type(v).__name__)
```

### Example 2: Student Information

```python
student = {
    "name": "Asha",
    "age": 18,
    "marks": [85, 90, 78],
    "is_hosteller": True
}

total = sum(student["marks"])
average = total / len(student["marks"])

print("Name:", student["name"])
print("Total:", total)
print("Average:", round(average, 2))
print("Hosteller:", student["is_hosteller"])
```

### Example 3: Removing Duplicates with a Set

```python
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = list(set(numbers))
print(unique_numbers)   # [1, 2, 3, 4, 5]  (order can vary in general)
```

### Example 4: Taking Input and Converting Types

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Type of sum:", type(num1 + num2))
```

### Example 5: Checking Types with `isinstance()`

```python
def describe(value):
    if isinstance(value, bool):
        return "Boolean"
    elif isinstance(value, (int, float)):
        return "Number"
    elif isinstance(value, str):
        return "Text"
    elif isinstance(value, (list, tuple)):
        return "Ordered collection"
    else:
        return "Something else"

print(describe(True))        # Boolean
print(describe(42))          # Number
print(describe("Hello"))     # Text
print(describe([1, 2]))      # Ordered collection
```

> `bool` is checked **first** because `True` is also an `int`.

---

## 8. Common Mistakes

| # | Mistake | Explanation / Fix |
| - | ------- | ----------------- |
| 1 | Using `{}` to create an empty set | `{}` creates an empty **dict**. Use `set()`. |
| 2 | Forgetting the comma in a one-item tuple | `(5)` is an `int`. Write `(5,)`. |
| 3 | Trying to change a string or tuple | They are immutable. Create a new value instead. |
| 4 | Adding a number and a string | `5 + "3"` gives a `TypeError`. Convert first: `5 + int("3")`. |
| 5 | Forgetting that `input()` returns a string | Convert with `int()` or `float()` before doing maths. |
| 6 | Expecting `int("3.7")` to work | It raises `ValueError`. Use `int(float("3.7"))`. |
| 7 | Expecting `int(3.9)` to round | It **cuts off** the decimal and gives `3`. Use `round()`. |
| 8 | Comparing floats with `==` | `0.1 + 0.2 == 0.3` is `False` because of tiny rounding errors. |
| 9 | Writing `true` or `false` in lowercase | Python needs `True` and `False`. |
| 10 | Using `== None` | Use `is None`. |
| 11 | Using a list as a dictionary key or set item | Keys and set items must be immutable (hashable). Use a tuple. |
| 12 | Expecting a set to keep order or support indexing | Sets are unordered, so `my_set[0]` is an error. |
| 13 | Thinking `b = a` copies a list | It only creates a second name for the same list. Use `a.copy()`. |
| 14 | Printing `range(5)` and expecting a list | It prints `range(0, 5)`. Use `list(range(5))`. |
| 15 | Naming variables `list`, `str`, `int`, `dict`, and so on | This hides the built-in names and breaks later code such as `list(...)`. |
| 16 | Reading a missing dictionary key with `[]` | It raises `KeyError`. Use `.get()` for a safe lookup. |

---

## 9. Important Points for Exams/Interviews

* Python is **dynamically typed**. You don't declare types, and the type is decided by the value at runtime.
* In Python, **everything is an object**, and every object has a type.
* `type()` returns the exact type. `isinstance()` also accepts subtypes.
* `int` has **no size limit** in Python.
* `/` always returns a `float`. `//` gives whole-number (floor) division.
* `bool` is a **subclass of `int`**: `True == 1`, `False == 0`, and `True + True == 2`.
* **Falsy values:** `0`, `0.0`, `0j`, `""`, `[]`, `()`, `{}`, `set()`, `range(0)`, `None`, `False`.
* **Mutable:** `list`, `set`, `dict`. **Immutable:** `int`, `float`, `complex`, `bool`, `str`, `tuple`, `range`, `frozenset`, `NoneType`.
* A `list` is mutable. A `tuple` is immutable. Tuples are generally used for fixed data.
* A tuple can contain a mutable item (for example a list), and that inner list can still be changed. The tuple itself still cannot have items replaced.
* `set` stores **unique** items and has no order. `frozenset` is its immutable version.
* `{}` creates a **dict**, not a set.
* **Dictionary keys** must be unique and immutable (hashable). Values can be anything.
* `dict` keeps insertion order in Python 3.7 and later.
* `None` is the only value of `NoneType`. Compare with `is None`.
* `input()` always returns a `str`.
* `int(3.9)` gives `3` because it truncates. It does not round.
* Converting a list to a set removes duplicates and loses the order.
* Use `is` to compare **identity** (same object) and `==` to compare **values**.

---

## 10. Practice Questions

1. What is a data type, and why does Python need data types?
2. What does it mean that Python is *dynamically typed*? Give a small example.
3. What is the output of each line, and what is the type of each result?
   ```python
   print(10 / 2)
   print(10 // 3)
   print(2 ** 3)
   ```
4. List all the falsy values in Python that you can remember. What is the output of `bool("0")` and why?
5. What is the difference between a `list` and a `tuple`? When would you choose a tuple?
6. Which line raises an error, and why?
   ```python
   name = "Python"
   name[0] = "J"
   ```
7. What is the difference between `set` and `frozenset`? Why can a `frozenset` be a dictionary key but a `set` cannot?
8. What is the type of each variable?
   ```python
   a = {}
   b = set()
   c = (5)
   d = (5,)
   ```
9. Convert the list `[1, 2, 2, 3, 3, 3]` into a set. What do you observe about duplicates and order?
10. What happens when you run each line, and why?
    ```python
    int("25")
    int("2.5")
    int(2.9)
    float("abc")
    ```

---

## 11. Summary

* A **data type** defines what kind of value something is and what you can do with it.
* Python decides the type automatically from the value (**dynamic typing**).
* **Numeric:** `int` (whole numbers), `float` (decimals), `complex` (real + imaginary).
* **Boolean:** `bool` has `True` and `False`. Empty and zero values are falsy.
* **Sequences:** `str`, `list`, `tuple` and `range` are all ordered and support indexing. Only `list` is mutable.
* **Sets:** `set` and `frozenset` store unique, unordered items. `frozenset` is immutable.
* **Dictionary:** `dict` stores unique-key/value pairs and is mutable.
* **None:** `NoneType` represents "no value". Check it with `is None`.
* Check types with `type()` or `isinstance()`.
* Convert types with `int()`, `float()`, `str()`, `list()`, `tuple()` and `set()`. Invalid conversions raise `ValueError` or `TypeError`.
* **Mutable:** `list`, `set`, `dict`. **Immutable:** everything else covered here.

| Quick Revision | |
| -------------- | - |
| Change allowed | `list`, `set`, `dict` |
| No change allowed | `int`, `float`, `complex`, `bool`, `str`, `tuple`, `range`, `frozenset`, `NoneType` |
| Ordered | `str`, `list`, `tuple`, `range`, `dict` (insertion order) |
| Unique items only | `set`, `frozenset`, `dict` keys |
| Empty set | `set()` |
| Empty dict | `{}` |
| Single-item tuple | `(5,)` |