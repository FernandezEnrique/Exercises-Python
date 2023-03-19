# Quick Start with Python

Here are some basics functions of Python to get started.

# Console I/O

# Print

The `print` function is used to show text on the screen

`sep` is a separator between each word given.

`end` will be at the end of the string

```python3
print("Hello", "World", sep="-", end="!")
>> Hello-World!
```

We can format the text

```python3
name = "Enrique"
print(f"Hello {name}", end='.')
>> Hello Enrique.
```

# Input

This function `input` allows user input and it can be stored in a variable.

```python3
var_name = input("Write your name: ")
>> Javier
print(var_name)
>> Javier
```

# Integer and String

To do maths, it is useful to convert a string to an integer

```python3
n1 = input("Write a number: ")
>> 2
n2 = input("Write another number: ")
>> 2
print(n1 + n2)
>> 22 (I do not think you were expecting this)
print(int(n1) + int(n2))
>> 4
```

So, from string to int: `int()`

And, from int to string: `str()`

# Variable

In Python we do not need to specify its type, in other languajes like C++ we have to say the type of the var before we create it, for example

```Cpp
int year = 2023;
```

In Python it does not work like that, we just say the name and its value. We can even change its type later.

```python3
year = 2023
year = "2023"
```

The name of vars can start with a letter (capital or not) and with an underscore, never with a number.

```python3
year = 2023
Year = 2023
YEAR = 2023
_year = 2023
0year = 2023
```

All of them are valid except the last one.