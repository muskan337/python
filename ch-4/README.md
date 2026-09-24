# Chapter 4: Lists and Tuples

Both lists and tuples store **multiple values in order**. The big difference: a list can be changed, a tuple cannot.

## Contents

| Folder | Topic |
| ------ | ----- |
| [list](list) | Creating, indexing, slicing, changing lists |
| [list_methods](list_methods) | `append`, `sort`, `reverse`, `insert`, `pop` |
| [tuple](tuple) | Creating tuples, immutability |
| [tuple_methods](tuple_methods) | `count`, `index` |
| [pb1](pb1) | Practice: collect 5 fruits |
| [pb2](pb2) | Practice: collect 6 marks |
| [pb3](pb3) | Practice: tuples cannot be changed |
| [pb4](pb4) | Practice: sum of a list |
| [pb5](pb5) | Practice: count items in a tuple |

## List vs Tuple

| Feature | List | Tuple |
| ------- | ---- | ----- |
| Brackets | `[ ]` | `( )` |
| Mutable | Yes | No |
| Ordered | Yes | Yes |
| Duplicates | Allowed | Allowed |
| Indexing and slicing | Yes | Yes |
| Methods | Many | Only `count` and `index` |
| Example | `[1, 2, 3]` | `(1, 2, 3)` |

## Summary

* Use a **list** when the data needs to change.
* Use a **tuple** when the data should stay fixed.
* Both are indexed from `0` and support slicing.
