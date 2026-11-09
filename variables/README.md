# Variables

## What is a variable?

A **variable** is a named box that stores a value you want to use later.

```python
name = "Tharuka"   # text
age = 23           # number
```

## The 4 main data types

| Type  | Example | Means |
|-------|---------|-------|
| `str` | `"hello"` | text |
| `int` | `23` | whole number |
| `float` | `5.8` | decimal number |
| `bool` | `True` / `False` | yes / no |

Check a type with `type()`:

```python
print(type(age))   # <class 'int'>
```

## Rules for naming variables

1. Start with a letter or underscore (not a number)
2. No spaces — use `_` instead
3. Case-sensitive: `Age` ≠ `age`
4. No Python keywords (`if`, `for`, `while`, `class`, `def`, ...)

## Print with f-strings (best way)

```python
age = 23
print(f"I am {age} years old")
```

## Run the example

```bash
cd tutorials/variables
python variables.py
```
