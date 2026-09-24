# Python Learning Notes

My step-by-step notes and practice code while learning Python. Every folder has a Python file with the code and a `README.md` that explains it in simple language, including the expected output.

---

## Chapters

| Chapter | Topic | What is inside |
| ------- | ----- | -------------- |
| [ch-1](ch-1) | Getting Started | `print()`, comments, multi-line strings, using external modules |
| [ch-2](ch-2) | Basics | Variables, data types, input, operators, type casting |
| [ch-3](ch-3) | Strings | Indexing, slicing, escape sequences, string methods |
| [ch-4](ch-4) | Lists and Tuples | Mutable vs immutable, list and tuple methods, practice problems |
| [ch-5](ch-5) | Dictionaries and Sets | Key-value pairs, dictionary methods, sets |

---

## Folder Guide

| Folder | Topic |
| ------ | ----- |
| `ch-1/pblm` | Text-to-speech program using `pyttsx3` |
| `ch-2/variables` | Creating variables and printing them |
| `ch-2/datatypes` | All built-in data types (full study notes) |
| `ch-2/input` | Taking user input, `int()`, f-strings |
| `ch-2/operatorss` | Arithmetic, assignment, comparison, logical operators |
| `ch-3/intro_to_string` | Quotes, indexing, basic slicing |
| `ch-3/negative_slicing` | Negative indexes and slicing with a step |
| `ch-3/escape_sequence character` | `\n`, `\t`, `\"` |
| `ch-3/str_function` | String methods like `upper()`, `find()`, `replace()` |
| `ch-3/pb1`, `ch-3/pb2` | Practice problems on strings |
| `ch-4/list`, `ch-4/list_methods` | Lists and their methods |
| `ch-4/tuple`, `ch-4/tuple_methods` | Tuples and their methods |
| `ch-4/pb1` to `ch-4/pb5` | Practice problems on lists and tuples |
| `ch-5/dictionary`, `ch-5/methods` | Dictionaries and their methods |
| `ch-5/sets` | Sets |

---

## How to Run Any File

1. Install Python 3 and check it with `python --version`.
2. Open a terminal in the folder of the file.
3. Run:

```bash
python filename.py
```

Two programs in `ch-1` use external packages:

```bash
pip install pyjokes pyttsx3
```

Everything else uses only built-in Python.

---

## Housekeeping Notes

Small things in the repo worth fixing later:

| Item | Suggestion |
| ---- | ---------- |
| `ch-1/.py` has no file name | Rename it, e.g. `ch-1/twinkle.py` |
| `ch-2/typecasting and Type( )func` has no `.py` extension and no folder | Move it to `ch-2/typecasting/typecasting.py` |
| `ch-2/operatorss` | Likely a typo for `operators` |
| Names with spaces (`escape_sequence character`) | Use underscores: `escape_sequence_character` |
| `ch-4/pb4` uses `list` as a variable name | Rename it, since it hides the built-in `list` |

---

## Author

Muskan, first-year BTech CSE student.
