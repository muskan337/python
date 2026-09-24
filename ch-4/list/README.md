# Lists

## What is a List?

A **list** is an ordered collection of items stored in one variable. Lists are written with square brackets and can hold **any data type**, mixed together.

## The Code

```python
friends = ["apple", "mango", "muskan", False,  5, 345.06]

print(friends[0])

#we can make changes in existing string, lists are mutable

friends[0] = "grapes"

print(friends[0])

#LISTS ARE CONTAINERS TO STORE A SET OF VALUES OF ANY DATA TYPE
# A LIST CAN BE INDEXED JUST LIKE A STRING AND CAN BE SLICED JUST LIKE STRING
print(friends[1:4]) #mangi, muskan , 4
```

## Output

```text
apple
grapes
['mango', 'muskan', False]
```

## Explanation

| Code | Meaning | Result |
| ---- | ------- | ------ |
| `friends = [...]` | A list with a string, a bool, an int, and a float | |
| `friends[0]` | First item | `apple` |
| `friends[0] = "grapes"` | Replaces the first item (allowed, lists are mutable) | |
| `friends[1:4]` | Items at index 1, 2, 3 | `['mango', 'muskan', False]` |

## Two Comment Corrections

| Comment in file | Correction |
| --------------- | ---------- |
| `#mangi, muskan , 4` | The slice gives `mango`, `muskan`, **`False`**. Index 4 (the value `5`) is not included. |
| "we can make changes in existing string" | It should say **list**. Strings are immutable, lists are mutable. |

## Index Map

| Item | "apple" | "mango" | "muskan" | False | 5 | 345.06 |
| ---- | ------- | ------- | -------- | ----- | - | ------ |
| Index | 0 | 1 | 2 | 3 | 4 | 5 |
| Negative | -6 | -5 | -4 | -3 | -2 | -1 |

## More Things You Can Do

```python
friends = ["apple", "mango", "muskan"]

print(len(friends))        # 3
print(friends[-1])         # muskan
print("mango" in friends)  # True
print(friends + ["kiwi"])  # ['apple', 'mango', 'muskan', 'kiwi']
```

## Common Mistakes

| Mistake | Fix |
| ------- | --- |
| Using an index that does not exist (`friends[10]`) | Raises `IndexError`. Check `len()` first. |
| Thinking `friends[1:4]` includes index 4 | The stop index is excluded. |
| Using `( )` instead of `[ ]` | `( )` creates a tuple. |

## Summary

* Lists are ordered, mutable, and allow duplicates and mixed types.
* Index and slice them just like strings.
* You can change an item by assigning to its index.
