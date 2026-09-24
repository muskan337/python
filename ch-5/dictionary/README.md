# Dictionary

## What is a Dictionary?

A **dictionary** stores data as **key-value pairs**. You look up a value using its key, like finding a word's meaning in a real dictionary.

## The Code

```python
#Dictionary is a collection of key-value pairs
#why dictionary
#Dictionary is unordered, mutable, indexed, can't contain duplicate keys
marks = {
    "Muskan" : 100,
    "Shubham" : 34
}

#list odf list s allowed in python, but it is computationally expensive

print(marks, type(marks))

print(marks["Muskan"])
```

## Output

```text
{'Muskan': 100, 'Shubham': 34} <class 'dict'>
100
```

## Explanation

| Term | In this example |
| ---- | --------------- |
| Key | `"Muskan"`, `"Shubham"` |
| Value | `100`, `34` |
| Key-value pair | `"Muskan": 100` |
| `marks["Muskan"]` | Looks up the value for the key `"Muskan"`, giving `100` |

## Adding, Changing, Deleting

```python
marks = {"Muskan": 100, "Shubham": 34}

marks["Renuka"] = 95       # add a new pair
marks["Shubham"] = 40      # change an existing value
del marks["Renuka"]        # delete a pair

print(marks)               # {'Muskan': 100, 'Shubham': 40}
```

## Rules for Dictionaries

| Rule | Detail |
| ---- | ------ |
| Keys are unique | A repeated key keeps only the **last** value. |
| Keys must be immutable | Strings, numbers, and tuples are fine. Lists are not. |
| Values can be anything | Numbers, strings, lists, even other dictionaries. |
| Lookup uses the key | `marks["Muskan"]`, not an index number. |

```python
d = {"a": 1, "a": 2}
print(d)    # {'a': 2}
```

## Comment Corrections

The comment in the file says a dictionary is "unordered" and "indexed". Both need a small update:

| Comment says | Correct for modern Python |
| ------------ | ------------------------- |
| Unordered | Since Python 3.7, dictionaries **remember the order** items were added. |
| Indexed | They are accessed by **key**, not by position number. `marks[0]` looks for a key named `0`. |

## Missing Keys

```python
marks = {"Muskan": 100}

# print(marks["Ravi"])    # KeyError: 'Ravi'
print(marks.get("Ravi"))  # None (safe)
```

## Nested Structures

Dictionaries can hold lists or other dictionaries:

```python
student = {
    "name": "Muskan",
    "marks": [90, 85, 100]
}

print(student["marks"][0])   # 90
```

## Summary

* A dictionary is a collection of `key: value` pairs written in `{ }`.
* Keys are unique and immutable. Values can be any type.
* Use `dict[key]` to read, and `.get(key)` for safe lookup.
