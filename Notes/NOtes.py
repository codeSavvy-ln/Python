"""
    Casting

Use a to declare the type of varaible. Ex-
print("Casting from integer to string")

integer_variable = 5
integer_variable_casting_to_string = str(integer_variable)

print(type(integer_variable_casting_to_string))


    Camel Case
Each word, except the first, starts with a capital letter: myVariableName
    Lower camel case - myVariableName
    Upper Camel Case - MyVariableName

    Pascal Case
Each word starts with a capital letter: MyVariableName

    Snake Case
Each word is separated by an underscore character: my_variable_name



    Keyword	Description
and                         	A logical operator
as	                            To create an alias
assert	                        For debugging
break	                        To break out of a loop
class	                        To define a class
continue	                    To continue to the next iteration of a loop
def	                            To define a function
del	                            To delete an object
elif	                        Used in conditional statements, same as else if
else	                        Used in conditional statements
except	                        Used with exceptions, what to do when an exception occurs
False	                        Boolean value, result of comparison operations
finally	                        Used with exceptions, a block of code that will be executed no matter if there is an exception or not
for	                            To create a for loop
from	                        To import specific parts of a module
global	                        To declare a global variable
if	                            To make a conditional statement
import	                        To import a module
in	                            To check if a value is present in a list, tuple, etc.
is	                            To test if two variables are equal
lambda	                        To create an anonymous function
None	                        Represents a null value
nonlocal	                    To declare a non-local variable
not	                            A logical operator
or	                            A logical operator
pass	                        A null statement, a statement that will do nothing
raise	                        To raise an exception
return	                        To exit a function and return a value
True	                        Boolean value, result of comparison operations
try	                            To make a try...except statement
while	                        To create a while loop
with	                        Used to simplify exception handling
yield	                        To end a function, returns a generator


### Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:

Text Type:	                    str
Numeric Types:	                int, float, complex
Sequence Types:	                list, tuple, range
Mapping Type:	                dict
Set Types:	                    set, frozenset
Boolean Type:	                bool
Binary Types:	                bytes, bytearray, memoryview
None Type:	                    NoneType


### Float can also be scientific numbers with an "e" to indicate the power of 10.
Ex:-   x = 3e3
Result:- x = 3000

            #Varibale like int, Float, Complex can be inter convertible

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

                    #Random Number

Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:


                    #Check String

To check if a certain phrase or character is present in a string, we can use the
keyword in and not in keyword to check if the string is not present

txt = "The best things in life are free!"
print("free" in txt)


LIST                   dic()                    Set                         TUPLE

[]                  {key:value}                 {}                           ()
ordered              ordered                 unordered                    ordered
changeable          changeable              unchangeable                 unchangeable
Duplicate           No duplicate            No duplicate                  duplicate
                   Str,Int,Boolean         Str,Int,Boolean               Str,Int,Boolean
Can be access        can be              Can't access by index/key
                    only copy()


dct were unorderd till python 3.6

Ordered; Changeable = Data within the collection is ordered and changeble
Duplicate = If the duplicate date/members are allowed or not in the collections



#
"""
"""
n = 4
if n % 2 == 0:
  print("first = weird")
elif n>2 and n<5:
  print("Second = Not Wierd")
elif n%2==0 and n>6 and n<20:
  print("Third: wierd")
elif n%2==0 and n>20:
  print("Forth: wierd")
  
 

n = int(input("Enter an integer: "))

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 ==0 and n>20 :
    print("Not wierd")
    
     """
"""
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif n in range(2,6):
        print("Not Weird")
    elif n in range(6,21):
        print("Weird")
    elif n > 20:
        print("Not Weird")




class Employee:
    def __init__(self, name, salary, attendance):
        self.name = name
        self.salary = salary
        self.attendance = attendance

    def show_Employee_details(self):
        print("Name: ", self.name, "Salary: ", self.salary)

Sara = Employee("Sara", 3000, True)
Sara.show_Employee_details()

"""

"""
1. Integer Division (//):
Integer division is performed using the // operator in Python.
It divides two numbers and returns the quotient as an integer, discarding any remainder or fractional part.
The result is always rounded down to the nearest integer (even if the result is negative).

print(10 // 3)  # Output: 3 (10 divided by 3 is 3.333, rounded down to 3)
print(10 // 2)  # Output: 5
print(-10 // 3) # Output: -4 (rounds down to the smaller integer, -4)


2. Float Division (/):
Float division is performed using the / operator in Python.
It divides two numbers and returns the quotient as a float (with decimal points), even if the result is a whole number.

print(10 / 3)  # Output: 3.3333333333333335
print(10 / 2)  # Output: 5.0
print(-10 / 3) # Output: -3.3333333333333335


\'	    Single Quote	
\\	    Backslash	
\n	    New Line	
\r	    Carriage Return	
\t	    Tab	
\b	    Backspace	
\f	    Form Feed	
\ooo	Octal value	
\XHH (in small letters)	Hex value

| Desired Type     | Example Code                             | Example Input | Result            |
| ---------------- | ---------------------------------------- | ------------- | ----------------- |
| **String**       | `name = input()`                         | `"Alice"`     | `'Alice'` (str)   |
| **Integer**      | `age = int(input())`                     | `25`          | `25` (int)        |
| **Float**        | `price = float(input())`                 | `9.99`        | `9.99` (float)    |
| **Boolean**      | `flag = bool(int(input()))`              | `1`           | `True` (bool)     |
| **List**         | `lst = input().split()`                  | `a b c`       | `['a', 'b', 'c']` |
| **Tuple**        | `tpl = tuple(input().split())`           | `1 2 3`       | `('1', '2', '3')` |
| **List of ints** | `nums = list(map(int, input().split()))` | `1 2 3`       | `[1, 2, 3]`       |


---------------------------------------------------------------------------------------------------------------------
List comprehension is a concise and elegant way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an iterable (like a list, range, or string) and optionally filtering items based on a condition.

Syntax: [expression for item in iterable if condition]

expression: The operation or value to include in the new list.			
item: The variable representing each element in the iterable.			
iterable: The collection (e.g., list, range, string) to iterate over.			
if condition (optional): A filter to include only specific items.

Example:
1	Simple List Creation: Create a list of squares of numbers from 0 to 9:							
	squares = [x**2 for x in range(10)]						squares = []	
	print(squares)			[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]			for x in range(10):	
							squares.append(x**2)	
2	With a Condition: Create a list of even numbers from 0 to 9:							
	evens = [x for x in range(10) if x % 2 == 0]				[0, 2, 4, 6, 8]			
	print(evens)							
								
3	Transforming Items: Convert a list of strings to uppercase:							
	words = ['hello', 'world', 'python']							
	uppercase_words = [word.upper() for word in words]				['HELLO', 'WORLD', 'PYTHON']			
	print(uppercase_words)							
								
4	Nested loops: Create a list of all pairs (x, y) where x is from 1 to 3 and y is from 1 to 2:							
	pairs = [(x, y) for x in range(1, 4) for y in range(1, 3)]							
	print(pairs)				[(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]			
								
5	Flatten a nested list: Flatten a 2D list:							
	matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]							
	flattened = [num for row in matrix for num in row]				[1, 2, 3, 4, 5, 6, 7, 8, 9]			
	print(flattened)					

--------------------------------------------------------------------------------------------------------------------		

|    Immutable   |   Mutable     |
|----------------|---------------|
|   Str          |   list        |
|   int          |   set         |
|   float        |   dict        |
|   bool         |"any other type|
|   bytes        |used by 3rd    |
|   tuple        |party library  |
|                |or module"     |
|________________|_______________|
"""
print("SSAS")


