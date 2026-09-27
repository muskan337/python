# Text to Speech with `pyttsx3`

## What Does This Program Do?

It makes your computer **speak** a sentence aloud.

## Setup

`pyttsx3` is not built into Python. Install it once:

```bash
pip install pyttsx3
```

## The Code

```python
import pyttsx3
engine = pyttsx3.init();
engine.say("Hello, my name is muskaan")
engine.runAndWait()
```

## Line by Line

| Line | Meaning |
| ---- | ------- |
| `import pyttsx3` | Loads the text-to-speech package. |
| `engine = pyttsx3.init()` | Creates a speech engine object and stores it in `engine`. |
| `engine.say("...")` | Adds the text to the speaking queue. |
| `engine.runAndWait()` | Actually speaks the queued text and waits until it is done. |

## Output

There is no printed output. You **hear** the sentence through your speakers.

## Notes

* The `;` after `pyttsx3.init()` is not needed in Python. It is allowed but usually left out.
* Nothing is spoken if you forget `runAndWait()`.
* If you get `ModuleNotFoundError: No module named 'pyttsx3'`, the package is not installed. Run the `pip install` command above.
* Change the text inside `say()` to make it speak anything.

## Try It Yourself

```python
import pyttsx3

name = input("Enter your name: ")

engine = pyttsx3.init()
engine.say(f"Hello {name}, welcome to Python")
engine.runAndWait()
```

## Summary

* External packages are installed with `pip` and loaded with `import`.
* `init()` creates the engine, `say()` queues text, `runAndWait()` speaks it.
