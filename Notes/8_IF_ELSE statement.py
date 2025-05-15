# If-else statement gives an ability to decision making. It helps to execute bulk of codes
#  Elif (Else if) for all mid conditions.
#  Else is for last condition used as a 'last exit point'
""" Intendation is equal to 2 white spaces. Use curly brackets you don't want to use intendation as show below:
if age < 35:{
print("You have earned a BMW car.")
}
"""

x = 4
if x>3:
    print("True")
else:
    print("False")


                        #ELIF
age = 36
if age < 35:
    print("You have earned a BMW car.")


elif age >= 30:
    print("You are financial independant now.")

elif age >= 25:
    print("You have earned a car.")

else:
    print("You are only 22")


# Logical operator 'AND'

age = 30
name = "James"
married = "True"

if age>40 and name == "James":
    print("James is greated than 20 years old")
else:
    print("Above statement is incorrect")

# Logical operator 'OR'


if age>20 or name == "James":
    print("James is greated than 20 years old")
else:
    print("Above statement is incorrect")


# NESTING in IF statement

if age > 20 and name == "James":
    if married == "True":
        print("James is above 30 and married")
    else:
        print("James is 30 and not married")

else:
    print("All the above statements are incorrect")

                         #SHORT HAND IF - Single line if statement

a = 850
b = 950
#EX-1
if a<b: print ("a is greater than b")

#EX-2
print ("a is greater than b") if a>b else print ("b is greater than a")

#EX-3

print ("a is greater than b") if a>b else print("a is equal to b") if a==b else print \
    ("a is less than b")

"""explanation for EX-3 
If a>b passes then it will print 'a is greater than b' otherwise it will go to else
 then after going to else it will check if a==b then it will print a is equal to b otherwise it will print a is less than b"""



                           #Practice

employees = {"Jack" : 6, "Russel" : 10, "Keren" : 2}
print(employees)

if employees["Jack"] >= 5 and employees["Jack"] <= 8:
    print("Jack is available")

elif employees["Russel"] >= 5 and employees["Russel"] <= 8:
    print("Russel is available")

elif employees["Keren"] >= 5 and employees["Keren"] <= 8:
    print("Keren is available")

else:
    print("No one is available")


# 2. Manager asks if someone can work 2 or 4 hours on the weekend

if employees["Jack"] == 2 or employees["Jack"] == 4:
    print("Jack is available for 2 or 4 hours on the weekend ")

elif employees["Russel"] == 2 or employees["Russel"] == 4:
    print("Russel is available for 2 or 4 hours on the weekend ")

elif employees["Keren"] == 2 or employees["Keren"] == 4:
    print("Keren is available for 2 or 4 hours on the weekend ")

    if employees["Keren"] == 2:
        print("Keren is available for 2 hours")

    else:
        print("Keren is available for 4 hours")


else:
    print("No one is available")


# Manager wnats to know the exact time keren is available in the weekend