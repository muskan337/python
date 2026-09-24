# Negative Indexing and Slicing

## The Code

```python
name = "muskan"

nameshort = name[0:3]
print(name[0:5])  #muska
print(name[-4:-1]) #ska
print(name[2:5])   #ska
print(name[:5])   #same as[0:5]
print(name[2:])   #same as [2:6]
print(name[2:6])   #[1:length]

a = "012345678910"
print(a[1:5:2])
```

## Output

```text
muska
ska
ska
muska
skan
skan
13
```

## Index Map for `"muskan"`

| Character | m | u | s | k | a | n |
| --------- | - | - | - | - | - | - |
| Index | 0 | 1 | 2 | 3 | 4 | 5 |
| Negative index | -6 | -5 | -4 | -3 | -2 | -1 |

## Slice Syntax

```text
string[start : stop : step]
```

| Part | Meaning | Default |
| ---- | ------- | ------- |
| `start` | First index (included) | `0` |
| `stop` | Last index (**not** included) | end of string |
| `step` | Jump size | `1` |

## Line by Line

| Code | Works out to | Output |
| ---- | ------------ | ------ |
| `name[0:5]` | indexes 0 to 4 | `muska` |
| `name[-4:-1]` | -4 is `s`, stops before -1 (`n`) | `ska` |
| `name[2:5]` | indexes 2, 3, 4 | `ska` |
| `name[:5]` | start missing, so 0 | `muska` |
| `name[2:]` | stop missing, so till the end | `skan` |
| `name[2:6]` | indexes 2 to 5 | `skan` |
| `a[1:5:2]` | indexes 1 and 3 (jump by 2) | `13` |

## Useful Slicing Tricks

```python
name = "muskan"

print(name[::-1])    # naksum  (reverse the string)
print(name[::2])     # msa     (every second character)
print(name[-3:])     # kan     (last three characters)
```

## Common Mistakes

| Mistake | Explanation |
| ------- | ----------- |
| Expecting the stop index to be included | It never is. |
| `name[-1:-4]` returns an empty string | With a positive step, start must be to the left of stop. |
| Slicing out of range causes an error | It does not. `name[2:100]` safely gives `skan`. |

## Summary

* Negative indexes count from the right, starting at `-1`.
* Slice format is `[start:stop:step]`, and `stop` is excluded.
* Leaving out `start` or `stop` uses the beginning or end.
* Slicing never modifies the original string.
