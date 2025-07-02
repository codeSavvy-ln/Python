"""# A loop is a block of statements repeatedly used until a particular condition is satisfied
# for cell in numbers_b :- here cell is single value where numbers_b is whole package
# break is used at the end of the loop to stop the loop once we get the desired output
# cell, Fruit_item, fruit_character

 for value in sequence:
	action
for each value in sequence, perform action 
     action is intended because of the colon in the previous line

syntax - for var in range(number):
in is operator in above synatx

#In for loop, we can only use iteration object like list,String but not integer.

#Break - It will stop it from running once the condition is met.
#continue - it will skip only that result which satisfies the condition.
#Pass - It will skip to next iteration once it matches with the result.

--Feature--           --FOR--                              --WHILE--
                It depends on data                  It depends on condition
Usage           Iterates over sequence or range     Executes based on a condition
When to Use     Number of iteration are known       Iterations depend on a condition
termination     stops when the sequence ends        stops when the condition becomes false
Control         Can use break and continue          Can use break and continue
"""
numbers_b = [1,2,3]

for cell in numbers_b:
    cell = cell * 5
    print(cell)

print("\n")

# Print a specific value from the below list by using for loop with if statement
fruits = ["Banana", "Orange", "Cherry", "Orange"]
for fruit_cell in fruits:
    if fruit_cell == "Orange":
        print(fruit_cell)
        break

                     # range()
for x in range(3):
    print(x)

print("\n")

for x in range(3,5):
    print(x)


print("\n")
# range from 3 to 15 with the difference of 4
for x in range(3,15,4):
    print(x)

print("\n")
                        # ADVANCE



                    #PRACTICE (ADVANCE)
"""
Tax for people earning 1 - 2k = 5%
Tax for people earning 2k - 5k = 10%
Tax for people earning 5k - 15k = 15%
Tax for people earning above 15k = 17%
healthcare reduction from each people is 2% after tax reduction
"""
businesses_list = [1500, 2542, 2001, 3500, 5300, 5555, 17000, 21000, 10 ,15001]
total_taxes = 0

for single_income in businesses_list:
    if single_income >= 1 and single_income <= 2000:
        tax = single_income * 0.05

    elif single_income >= 2001 and single_income <= 5000:
        tax = single_income * 0.1

    elif single_income >= 5001 and single_income <= 15000:
        tax = single_income * 0.15

    else:
        tax = single_income * 0.17

    net_income = single_income - tax
    salary_after_healthcare_reduction = net_income * 0.98
    print("Your salary is " + str(single_income) + " and deducted tax is: " +str(tax))
    print("Salary after reducing healthcare: " +str(salary_after_healthcare_reduction))
    print("\n")
    total_taxes = total_taxes + tax

print("Total of taxes: "+str(total_taxes))


# ENUMERATE
 #It is a built-in function which adds a counter to an iterable and returns it in a form of enumerate object.
 #This object can then be used directly in for loops or be converted into a lost of tuples using list() method.

#Example - 1
for i, letter in enumerate('pyspark'):
    print ("At index{} the letter is {}".format (i,letter))

#Example - 2
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

"""
| Feature     | f-string                  | `.format()`                          |
| ----------- | ------------------------- | ------------------------------------ |
| Syntax      | `f"Text {var}"`           | `"Text {}".format(var)`              |
| Readability | Cleaner and more readable | Slightly more verbose                |
| Version     | Python 3.6+               | Python 2.7 and 3.x                   |
| Performance | Slightly faster           | Slightly slower                      |
| Best for    | Most use cases            | Older codebases, advanced formatting |
"""