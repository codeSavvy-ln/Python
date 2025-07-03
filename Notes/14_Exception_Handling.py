"""
# There are at-least 2 kinds of errors in python:- Syntax error and exceptions.

# Exception handling:- it is a mechanism that allows you to handle runtime errors
or basically refers how we will handle any errors in case it occurs for example if
an ETL job fails then we can setup an alert saying that particular job got fail.

# Exception can be at Data, Code, System or Server level.

# Common Python Exceptions:
ZeroDivisionError: Raised when dividing by zero.
ValueError: Raised when a function receives an argument of the right type but an inappropriate value.
TypeError: Raised when an operation or function is applied to an object of inappropriate type.
FileNotFoundError: Raised when a file or directory is requested but doesn’t exist.

# Key Components of Exception Handling in Python:
try Block:
=========
Code that might raise an exception is placed inside the try block.
If an exception occurs, Python immediately stops executing the code in the try block and looks for an except block to handle it.

Except Block:
============
This block contains the code to handle specific exceptions.
You can have multiple except blocks to handle different exceptions.

else Block (Optional):
=====================
If no exceptions are raised in the try block, the else block is executed.

finally Block (Optional):
========================
This block is always executed, regardless of whether an exception occurred or not.
Useful for cleanup operations like closing files or releasing resources.

#Note - If you want to use multiple exception or exception is already know on the
result side then make sure to add the exceptions name following the exception as
shown in the below basic example.

Benefits in Python:
Simplifies error handling.
Improves code readability and maintainability.
Prevents program crashes.
Allows for specific handling of different error types.
"""
"""
#ZeroDivisionError

a=5
b=0
print (a/b)

#TypeError
It occurs when try to use an incompatible data type while performing a task for example when we try to add a string to an integer

variable = "Integer" + 5

a=5
b='1'
print (a/b)

ValueError

When provided value is not in acceptable range. for example when we try to convert string "Hello" to a float.

float("Hello")

#Basic Example-
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
finally:
    print("Execution completed.")


class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom exception!")
except CustomError as e:
    print("Caught:", e)

_______________________________________________________________
    Try-except                   vs             raise
_______________________________________________________________
Avoid errors being produced   | will produce an error
Still execute subsequent error| Avoid executing subsequent code

"""
# Track the exception message by giving it an Alias name-
try:
    a=5
    b=0
    print(a/b)
except Exception as e:
    print("Exception error is: " ,e)

"""
BaseException
├── BaseExceptionGroup
├── GeneratorExit
├── KeyboardInterrupt
├── SystemExit
└── Exception
    ├── ArithmeticError
    │   ├── FloatingPointError
    │   ├── OverflowError
    │   └── ZeroDivisionError
    ├── AssertionError
    ├── AttributeError
    ├── BufferError
    ├── EOFError
    ├── ExceptionGroup (BaseExceptionGroup)
    ├── ImportError
    │   └── ModuleNotFoundError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── MemoryError
    ├── NameError
    │   └── UnboundLocalError
    └── OSError
        ├── BlockingIOError
        ├── ChildProcessError
        └── ConnectionError
            └── BrokenPipeError

"""