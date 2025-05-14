<<<<<<< HEAD
"""
Variables are containers for storing data values.
#String is a variable which holds zero or more letters, numbers,special characters or the combo of all three
# It can't be manipulated by mathematical actions.
# It is always use under double quotation ex "a"

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

                    #use '+' inside a print command

First_name = "Ankit"
print("My first name is: " +First_name)

                    # Multiple values can be assigned for multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

                    #One Value to Multiple Variables

x = y = z = "Orange"
print(x)
print(y)
print(z)

                    #Unpack a Collection
"""If you have a collection of values in a list, tuple etc. Python allows you to 
extract the values into variables. This is called unpacking."""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)



                    # replace a part of a string

Serial_Number = "abc123"
print("My serial number is :" +Serial_Number.replace('123','456'))

                    #Practice
windows_serial_number ="abc-def-ghi-jkl"
print("New : "+windows_serial_number.replace('abc','aaa').replace('def','bbb').replace('ghi','ccc').replace('jkl','ddd'))
new_partial_variable_a = windows_serial_number[0:3]
new_partial_variable_b = windows_serial_number[4:7]
new_partial_variable_c = windows_serial_number[8:11]
new_partial_variable_d = windows_serial_number[12:15]

print(new_partial_variable_a)
print(new_partial_variable_b)
print(new_partial_variable_c)
print(new_partial_variable_d)

                #Global Variables
"""Variables that are created outside of a function (as in all of the examples above)
are known as global variables.
Create a variable outside of a function, and use it inside the function"""


x = "awesome"

def myfunc():               #pehely function ek inside searh karega agar milgaya otherwise bahar wala variable use kr lega
  print("Python is 1:" + x)

myfunc()

"""If you create a variable with the same name inside a function, this variable 
will be local, and can only be used inside the function. The global variable 
with the same name will remain as it was, global and with the original value."""

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is 2.1" + x)

myfunc()

print("Python is 2.2" + x)

                #The global Keyword
"""Normally, when you create a variable inside a function, that variable is local,
and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword."""

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is 3: " + x)


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

=======
"""
Variables are containers for storing data values.
#String is a variable which holds zero or more letters, numbers,special characters or the combo of all three
# It can't be manipulated by mathematical actions.
# It is always use under double quotation ex "a"

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

                    #use '+' inside a print command

First_name = "Ankit"
print("My first name is: " +First_name)

                    # Multiple values can be assigned for multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

                    #One Value to Multiple Variables

x = y = z = "Orange"
print(x)
print(y)
print(z)

                    #Unpack a Collection
"""If you have a collection of values in a list, tuple etc. Python allows you to 
extract the values into variables. This is called unpacking."""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)



                    # replace a part of a string

Serial_Number = "abc123"
print("My serial number is :" +Serial_Number.replace('123','456'))

                    #Practice
windows_serial_number ="abc-def-ghi-jkl"
print("New : "+windows_serial_number.replace('abc','aaa').replace('def','bbb').replace('ghi','ccc').replace('jkl','ddd'))
new_partial_variable_a = windows_serial_number[0:3]
new_partial_variable_b = windows_serial_number[4:7]
new_partial_variable_c = windows_serial_number[8:11]
new_partial_variable_d = windows_serial_number[12:15]

print(new_partial_variable_a)
print(new_partial_variable_b)
print(new_partial_variable_c)
print(new_partial_variable_d)

                #Global Variables
"""Variables that are created outside of a function (as in all of the examples above)
are known as global variables.
Create a variable outside of a function, and use it inside the function"""


x = "awesome"

def myfunc():               #pehely function ek inside searh karega agar milgaya otherwise bahar wala variable use kr lega
  print("Python is 1:" + x)

myfunc()

"""If you create a variable with the same name inside a function, this variable 
will be local, and can only be used inside the function. The global variable 
with the same name will remain as it was, global and with the original value."""

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is 2.1" + x)

myfunc()

print("Python is 2.2" + x)

                #The global Keyword
"""Normally, when you create a variable inside a function, that variable is local,
and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword."""

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is 3: " + x)


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

>>>>>>> 77a7026290cffc14ad5280317110e1c4e2e6e29e
print("Python is 4:" + x)