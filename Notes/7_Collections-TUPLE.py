<<<<<<< HEAD
# Tuple has :   <It is sort of fixed collections. once you create it don't touch it>
# ❏ Indexed and ordered cells - same as ‘list’.
# ❏ Cells cannot be changed - same as ‘set’.
# ❏ Cells cannot be added after initial creation.
# ❏ Cells cannot be deleted after initial creation.
# ❏ Single value per cell - same as ‘list’.
# ❏ Round brackets around the collection - While ‘list’ has square brackets.

###() when we create a tuple and [] - to extract a value from tuple

"""
To create a tuple with only one item, you have to add a comma after the item,
otherwise Python will not recognize it as a tuple:

thistuple = ("apple",)
print(type(thistuple))
"""

professions_in_the_industry = ("front-end", "back-end", "dev_ops", "qa")

# Print a value from tuple collection by its index cell value
print(professions_in_the_industry[-3])

# Access several cells by range of indexes
print(professions_in_the_industry[0:3])

#type of collection
print("Type of collection: " + str(type(professions_in_the_industry)))


#Change cell value

#‘Tuple’ cells are unchangeable.But still, there is a way to overcome this by :
fruits_tuple = ("banana", "berry", "mango")

print("Tuple: " + str(fruits_tuple))

fruits_lists = list(fruits_tuple)
fruits_lists[1] = "Apple"
fruits_tuple = tuple(fruits_lists)

print("Add Apple into the tuple: " + str(fruits_tuple))


                            #Change tuple values
#We can change the tuple  to list and change the list then turn it back to tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

                            #Add tuple to tuple

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

                            #Unpacking of tuple
"""But, in Python, we are also allowed to extract the values back into variables. 
This is called "unpacking":

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
"""


                                      #Practice

technological_terms = ("python", "pycharm IDE", "tuple", "collections", "string")

python = technological_terms[0]
pycharm_ide = technological_terms[-4]
tuple = technological_terms[2]
string = technological_terms[-1]

#print("we are ninja developers. we write " + str(python), "code in " + str(pycharm_ide) +", and now practicing "+ str(tuple), "collections topic, that contains ")
print("we are ninja developers. we write " + str(python), "code in " + str(pycharm_ide) + ", and now practicing " + str(tuple), "collections topic, that contains " + str(string), "variables.")


technological_lists = list(technological_terms)

technological_lists.append("float",)  #<if we remove the comma this it will become int not tuple>
technological_lists.append("list",)

#technological_terms = tuple(technological_lists)

print("Print new tuple: " + str(technological_terms))
=======
# Tuple has :   <It is sort of fixed collections. once you create it don't touch it>
# ❏ Indexed and ordered cells - same as ‘list’.
# ❏ Cells cannot be changed - same as ‘set’.
# ❏ Cells cannot be added after initial creation.
# ❏ Cells cannot be deleted after initial creation.
# ❏ Single value per cell - same as ‘list’.
# ❏ Round brackets around the collection - While ‘list’ has square brackets.

###() when we create a tuple and [] - to extract a value from tuple

"""
To create a tuple with only one item, you have to add a comma after the item,
otherwise Python will not recognize it as a tuple:

thistuple = ("apple",)
print(type(thistuple))
"""

professions_in_the_industry = ("front-end", "back-end", "dev_ops", "qa")

# Print a value from tuple collection by its index cell value
print(professions_in_the_industry[-3])

# Access several cells by range of indexes
print(professions_in_the_industry[0:3])

#type of collection
print("Type of collection: " + str(type(professions_in_the_industry)))


#Change cell value

#‘Tuple’ cells are unchangeable.But still, there is a way to overcome this by :
fruits_tuple = ("banana", "berry", "mango")

print("Tuple: " + str(fruits_tuple))

fruits_lists = list(fruits_tuple)
fruits_lists[1] = "Apple"
fruits_tuple = tuple(fruits_lists)

print("Add Apple into the tuple: " + str(fruits_tuple))


                            #Change tuple values
#We can change the tuple  to list and change the list then turn it back to tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

                            #Add tuple to tuple

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

                            #Unpacking of tuple
"""But, in Python, we are also allowed to extract the values back into variables. 
This is called "unpacking":

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
"""


                                      #Practice

technological_terms = ("python", "pycharm IDE", "tuple", "collections", "string")

python = technological_terms[0]
pycharm_ide = technological_terms[-4]
tuple = technological_terms[2]
string = technological_terms[-1]

#print("we are ninja developers. we write " + str(python), "code in " + str(pycharm_ide) +", and now practicing "+ str(tuple), "collections topic, that contains ")
print("we are ninja developers. we write " + str(python), "code in " + str(pycharm_ide) + ", and now practicing " + str(tuple), "collections topic, that contains " + str(string), "variables.")


technological_lists = list(technological_terms)

technological_lists.append("float",)  #<if we remove the comma this it will become int not tuple>
technological_lists.append("list",)

#technological_terms = tuple(technological_lists)

print("Print new tuple: " + str(technological_terms))
>>>>>>> 77a7026290cffc14ad5280317110e1c4e2e6e29e
