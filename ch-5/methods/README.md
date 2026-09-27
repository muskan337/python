# Dictionary Methods

## The Code

```python
marks = {
    "Muskan" : 100,
    "Shubham" : 34
}

print(marks.keys())
marks.update({"Muskan": 99, "Renuka": 95})
print(marks.values())
print(marks.get("shivika")) #None
```

## Output

```text
dict_keys(['Muskan', 'Shubham'])
dict_values([99, 34, 95])
None
```

## Step by Step

| Code | What happens |
| ---- | ------------ |
| `marks.keys()` | Returns all the keys: `Muskan`, `Shubham`. |
| `marks.update({...})` | Changes `Muskan` from 100 to **99** and adds a new pair `Renuka: 95`. |
| `marks.values()` | Returns all the values **after** the update: `99, 34, 95`. |
| `marks.get("shivika")` | The key does not exist, so it returns `None` instead of an error. |

The order of the lines matters: `keys()` was printed **before** `update()`, so `Renuka` is not in the first line.

After `update()`, the dictionary is:

```python
{'Muskan': 99, 'Shubham': 34, 'Renuka': 95}
```

## Methods Reference

| Method | What it does | Example |
| ------ | ------------ | ------- |
| `keys()` | All keys | `marks.keys()` |
| `values()` | All values | `marks.values()` |
| `items()` | All `(key, value)` pairs | `marks.items()` |
| `get(key)` | Value for `key`, or `None` if missing | `marks.get("Ravi")` |
| `get(key, default)` | Value, or `default` if missing | `marks.get("Ravi", 0)` |
| `update(dict)` | Add or change several pairs | `marks.update({"A": 1})` |
| `pop(key)` | Remove `key` and return its value | `marks.pop("Shubham")` |
| `clear()` | Remove everything | `marks.clear()` |
| `copy()` | Make a separate copy | `marks.copy()` |

## `get()` vs Square Brackets

```python
marks = {"Muskan": 99}

print(marks.get("Ravi"))      # None
print(marks.get("Ravi", 0))   # 0
# print(marks["Ravi"])        # KeyError
```

Keys are **case-sensitive**: `"Muskan"` and `"muskan"` are different keys.

## Looping Over a Dictionary

```python
for name, score in marks.items():
    print(name, "->", score)
```

## Common Mistakes

| Mistake | Fix |
| ------- | --- |
| Reading a missing key with `[]` | Use `.get()` to avoid `KeyError`. |
| Expecting `keys()` to give a list | It gives a view. Wrap it: `list(marks.keys())`. |
| Forgetting that `update()` overwrites existing keys | The old value is replaced. |
| Wrong letter case in a key | `"Shivika"` and `"shivika"` are different. |

## Summary

* `keys()`, `values()`, `items()` let you look inside a dictionary.
* `update()` adds new pairs and overwrites existing keys.
* `get()` is a safe way to read a value.
