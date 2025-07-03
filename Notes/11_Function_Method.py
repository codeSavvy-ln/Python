"""
#Method = Function and are denoted by 'def' and makes the code reusable
#Function is a block of code which is only run when it is called
These are used to separate the code

function is a code to perform the task
Method is a function that is specific to a data type

MODULES-

These are the files with .py extension and are used to perform specific task by importing them.

there are 2 types of modules:
    built-in modules - Python has around 200 built modules to use like pandas, NumPy, os etc
    User-defined - User can also create a module and import it for any specific use.

2 types of function

1. built in function -  do not to define them with def()
2. User-defined function - need to define them with def()

Syntax
def function_name(parameters):
    return value
result = function_name()

def = keyword to define a function
function_name = Name of the function (should be descriptive and follow naming conventions)
parameters = Variables passed to the function (optional)
return = Returns a value (optional)

Example:-
def add_numbers(a,b):
    result = a+b
    print ("sum of 3 and 4: " +str(result))
result = add_numbers(3,4)

# Arguments are the values passed to a function when calling it. they can be positional
, keyword or both, depending on how they are specified:

#1 - Positional arguments
Arguments that are passed to a function in the same order as their corresponding parameters are defined in the function.

Example:-
#2 - Keyword argumetns
Arguments passed to a function by explicitly specifying the parameter name along with the value.

Example:-
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
greet(age=25, name="Alice")  # Output: Hello Alice, you are 25 years old.


# Parameters vs Arguments:
Parameters are variables defined in the function signature.
Arguments are the actual values passed to the function during the call.

# Return Statement:
Functions can optionally return a value using the return statement.
If return is omitted, the function returns None by default.


"""


                                #1st Code
def salary_calc (salary):

    salary_of_employee = salary * 0.98
    print("Salary of employee is: " +str(salary_of_employee))

salary_calc(10000)
salary_calc(1000)


"""
                                #2nd Code
def salary_calc (salary,tax_reduction):

    salary_of_employee = salary * tax_reduction
    print("Salary of employee is: " +str(salary_of_employee))

salary_calc(10000,0.98)
salary_calc(1000,0.88)
"""


"""
                                    #3rd Code
def my_funtion(country = "Canada"):
    print("i am from " +str(country))

my_funtion()
my_funtion("Italy")

"""

                                #Type of function arguments

#1. Default argument :
"""We can provide default value to the arguments this way
arguments a default value even if the value is not provided to the argument"""

def my_function(a,b=4):
    print("The Average: ", (a+b)/2)

my_function(4)





    # 2.Keyword Argumets:
""" We can provide arguments with Key = Value syntax.
"""

def my_function(a,b):
    print("The Average (Keyword Args): ", (a+b)/2)
    print("a:" +str(a))

my_function(b=3, a=5)



    # 3.Required Arguments
""" Those arguments which are not provided in the functions are required to 
provide the arguments like a has a value but b does not
"""
def my_function(a=2,b=4): #remove 9 from here
    print("The Average (Keyword Args1): ", (a+b)/2)

my_function(4)


                            #Arbitrary Arguments, *args (short name)
"""If you do not know how many arguments that will be passed into your function, 
add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:
"""

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")




                    #Arbitrary Keyword Arguments, **kwargs(short name)
"""
If you do not know how many keyword arguments that will be passed into your function, 
add two asterisk: ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly:
"""
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")




                                    #4th Code (Use of RETURN)
def my_function(x):
    return 5*x
number = my_function(3)
print(number)


                                    #5th Code (Advance method :- keyword argument)

def phone_brands(Brand1,Brand2,Brand3):
    print("Brand 2 phone is: " +str(Brand2))

phone_brands(Brand1 = "Apple", Brand2 = "Samsung", Brand3 = "Lava")


                                    #6th Code (Advance :- Arbitary arguments)

def clothing_brands(*clothing_brands):
    print("This brand makes fast fashion cloths: " +str(clothing_brands[-1]))
clothing_brands("LV","Gucci","H&M")
clothing_brands("Armani","Zara")

print("\n")

                                    #7th Code

def company_name(**company_info):
    print("company name of the model is: " +company_info["model"])

company_name(brand = "Apple", model = "Iphone X", year = "2020")
company_name(brand = "Samsung", model = "Samsung s23", year = "2023")


"""                     LAMDA FUNCTION
#A lambda function in Python is an anonymous function (a function without a name) defined using the lambda keyword. It is used for creating small, simple, and concise functions in a single line.
# It is a single liner single expresison or a single liner multiple expression

When to Use Lambda Functions
# For short, throwaway functions that you don't need to reuse.
# In functional programming constructs like map, filter, and reduce.
# When passing small functions as arguments to higher-order functions.

Limitations
# Can only contain one expression.
# Cannot have statements or annotations.
# Limited readability for complex logic.

syntax - lambda arguments : expression


lambda = Keyword to define a lambda
arguments = Input parameters fr the function (similar to regular function arguments)
expression = A single expression that is evaluated and returned.

add = lambda x,y : x+y
print (add(3,5))

we can also store a lambda as a variable
average = lambda x: sum(x) / len(x)
"""
