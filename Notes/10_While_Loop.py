""" While loop stops once its condition meets false statement or we can also use (BREAK) to exit from while loop even
when the codition is true
From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.



"""

# number starts from 0 and goes till 9
number = 0
while number < 10:

    print("Number +1= " + str(number))
    number += 1


"""
#Prints number from 0 to 6 due to the while loop.

number = 0
while number < 10:

    if number == 6:
        break                                                         #BREAK 
    print("Number +1 to 6= " + str(number))
    number += 1

Use continue in place of break in above code and it will contiure to print the value
"""

#Once the condition is false instead of exiting the while loop just go to else statement.

number_1 = 1
while number_1 < 5:
    print("Number_1:- " +str(number_1))
    number_1 += 1
else:
    number_1 = number_1 *100
    print("Number_1 is no longer greater than 5 :- " +str(number_1))


                                #PRACTICE
# Print the value from age list till value reaches 30 and also the value that stoped it to print.
age = [5,6,24,32,21,70]

counter = 0
while age[counter] < 30:
    print(age[counter])
    counter += 1

print("Value that stopped the loop is: " +str(age[counter]))

print("\n")

counter = 0
while age[counter] < 30:
    if age[counter] > 20:
        print("print the value: " +str(age[counter]))
        break
    counter += 1

                                # PRACTICE 2nd Question

counter = 0
while age[counter] < 70:
    age[counter] = age[counter] + 2
    print("Cells value is: " +str(age[counter]))
    counter += 1
else:
    print("Vale due to this loops stoped: " +str(age[counter]))

