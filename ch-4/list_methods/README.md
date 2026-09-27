# List Methods

## What are List Methods?

Methods are built-in actions for lists. Unlike string methods, most list methods **change the original list** because lists are mutable.

## The Code

```python
friends = ["Apple", "Orange", 5, 345.06, False, "Akash", "Rohan"]
#LISTS PR KOI METHODS USE KROGE TO LIST CHANGE HO JAAYEGI BUT IN CASE OF STRING NO CHANGE IN ORIGINAL STRING

friends.append("me") #append me at the end of the list

print(friends)

l1 = [1, 5, 4, 532, 234, 78]
l1.sort()  #sort the list
print(l1)

l1.reverse() #reverses the list
print(l1)

l1.insert(3, 33333) #(idx, object) insert 33333 at the idx 3
print(l1)

l1.pop(3)  #removes 33333
print(l1)
```

## Output

```text
['Apple', 'Orange', 5, 345.06, False, 'Akash', 'Rohan', 'me']
[1, 4, 5, 78, 234, 532]
[532, 234, 78, 5, 4, 1]
[532, 234, 78, 33333, 5, 4, 1]
[532, 234, 78, 5, 4, 1]
```

(The comment in the file says: "if you use methods on a list, the list changes, but with a string the original does not change.")

## Step by Step

| Step | Code | List becomes |
| ---- | ---- | ------------ |
| 1 | `friends.append("me")` | `me` added at the end |
| 2 | `l1.sort()` | `[1, 4, 5, 78, 234, 532]` (smallest to largest) |
| 3 | `l1.reverse()` | `[532, 234, 78, 5, 4, 1]` |
| 4 | `l1.insert(3, 33333)` | `33333` placed at index 3, the rest shift right |
| 5 | `l1.pop(3)` | Item at index 3 is removed |

Note: `pop(3)` removes the item **at index 3**, not the value `3`. It happened to remove `33333` because that was at index 3.

## Methods Reference

| Method | What it does | Example | Result |
| ------ | ------------ | ------- | ------ |
| `append(x)` | Add `x` at the end | `[1,2].append(3)` | `[1, 2, 3]` |
| `insert(i, x)` | Add `x` at index `i` | `[1,3].insert(1, 2)` | `[1, 2, 3]` |
| `pop(i)` | Remove and return item at index `i` (last if no `i`) | `[1,2,3].pop()` | returns `3` |
| `remove(x)` | Remove the first item equal to `x` | `[1,2,2].remove(2)` | `[1, 2]` |
| `sort()` | Sort ascending | `[3,1,2].sort()` | `[1, 2, 3]` |
| `reverse()` | Reverse the order | `[1,2,3].reverse()` | `[3, 2, 1]` |
| `extend(list)` | Add all items from another list | `[1].extend([2,3])` | `[1, 2, 3]` |
| `count(x)` | How many times `x` appears | `[1,1,2].count(1)` | `2` |
| `index(x)` | Index of first `x` | `[5,6].index(6)` | `1` |
| `copy()` | Make a separate copy | `a.copy()` | new list |
| `clear()` | Remove everything | `a.clear()` | `[]` |

## Important Points

* `sort()`, `reverse()`, `append()`, `insert()` return `None`. Do **not** write `l1 = l1.sort()`, or `l1` becomes `None`.
* `sort()` cannot compare mixed types. Sorting the `friends` list (strings and numbers together) raises a `TypeError`.
* To sort in descending order: `l1.sort(reverse=True)`.
* To get a sorted copy without changing the original: `sorted(l1)`.

```python
l1 = [3, 1, 2]
l1 = l1.sort()
print(l1)          # None   (a common mistake)
```

## Common Mistakes

| Mistake | Fix |
| ------- | --- |
| `l1 = l1.sort()` | Just call `l1.sort()`. |
| `pop(33333)` to remove a value | `pop` takes an **index**. Use `remove(33333)` for a value. |
| Sorting a list with mixed types | Keep the list to one comparable type. |

## Summary

* List methods modify the list in place.
* `append` adds at the end, `insert` adds at an index, `pop` removes by index, `remove` removes by value.
* `sort()` and `reverse()` change the order of the original list.
