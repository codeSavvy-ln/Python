<<<<<<< HEAD
""""### Collections in Python are containers that store collections of data.
### In total, there are four collections in python: LIST,DICT,SET and TUPLE

### LIST :- is declared by sqaure brackets []
### A list is a data structure in Python that contains an ordered sequence of zero
 or more elements. Lists in Python are mutable, which means they can be changed.
 They can contain any type of data, like a string or a dictionary.

 LIST                   dic()                    Set                         TUPLE

[]                  {key:value}                 {}                           ()
ordered              ordered                 unordered                    ordered
changeable          changeable              unchangeable                 unchangeable
Duplicate           No duplicate            No duplicate                  duplicate
                   Str,Int,Boolean         Str,Int,Boolean               Str,Int,Boolean
Can be access        can be              Can't access by index/key
                    only copy()
mutable             mutable                 mutable                        immutable
"""
list_of_random_values = [31, 4, 31.5 , 3,"Yes"]

        # Postive index numbering [0,1,  2   ,3,  4   ] here, we start from left
        # Negative index numbering[-5,-4,-3  ,-2, -1  ] here, we start from right

print(list_of_random_values [2])
print(list_of_random_values [4])
print(list_of_random_values[-2])
print(list_of_random_values[-5])



            #type()

"""From python's perspective, lists are defined as objects with the data type 
'list':"""
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

            #list() Constructor

"""It is also possible to use the list() constructor when creating a new list."""

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)






            #Practice

cars = ["BMW","TOYOTA","TESLA","KIA"]
print("List of cars: "+str(cars))

print("One before last item :" +cars[-2])

print(cars[1]=="TOYOTA")

mixed_values = ["jim",3500,"Alex",2.53,True]

print(mixed_values[0:4])

            # Add "Alpha-Romeo" into the list                            .append

cars.append("Alpha-Romeo")
print("Updated cars list :" +str(cars))

            #Insert a value on a specific position in a list             .insert

cars.insert(2,"TATA")
print("After inserting Tata into the list : " +str(cars))

            # Remove an item by mentioning the value                     .remove

cars.remove("TATA")
print("After removing tata from the list : " +str(cars))

            #Remove an item by mentioning the cell index                  .POP
cars.pop(2)
print("Removing Tesla from the list : "+str(cars))



            #Practice for List collection (Advance)

list_of_employees = ["Adam","John","Greg","Danna","Ashy"]

            # length of the list
"""length_of_employees_list = len(list_of_employees)"""

print("Length of the employees list :"+str(len(list_of_employees)))

            # Inserting "Jack" in place of "John"
list_of_employees[1] = "Jack"
print("New list of employees : "+str(list_of_employees))


"""
Another way to add a value in a specific place

Change a range of item values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

If you insert more items than you replace, the new items will be inserted where
you specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

ANS = ['apple', 'blackcurrant', 'watermelon', 'cherry']
"""

list_of_employees.insert(3,"Mavrik")
print("Mavrik joined in the list of employees : " +str(list_of_employees))

list_of_employees.pop(3)
print("Mavrik is removed from the list : "+str(list_of_employees))

            # Sort the list of employees by 'abc'
list_of_employees.sort()
print("Sorted list : "+str(list_of_employees))


#ZIP() Function
 #It combines two or more iterbales (like lists, tuples or strings) element-wise into a single iterable of tuples

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

zipped = zip(names, ages)
print(list(zipped))


=======
""""### Collections in Python are containers that store collections of data.
### In total, there are four collections in python: LIST,DICT,SET and TUPLE

### LIST :- is declared by sqaure brackets []
### A list is a data structure in Python that contains an ordered sequence of zero
 or more elements. Lists in Python are mutable, which means they can be changed.
 They can contain any type of data, like a string or a dictionary.

 LIST                   dic()                    Set                         TUPLE

[]                  {key:value}                 {}                           ()
ordered              ordered                 unordered                    ordered
changeable          changeable              unchangeable                 unchangeable
Duplicate           No duplicate            No duplicate                  duplicate
                   Str,Int,Boolean         Str,Int,Boolean               Str,Int,Boolean
Can be access        can be              Can't access by index/key
                    only copy()
mutable             mutable                 mutable                        immutable
"""
list_of_random_values = [31, 4, 31.5 , 3,"Yes"]

        # Postive index numbering [0,1,  2   ,3,  4   ] here, we start from left
        # Negative index numbering[-5,-4,-3  ,-2, -1  ] here, we start from right

print(list_of_random_values [2])
print(list_of_random_values [4])
print(list_of_random_values[-2])
print(list_of_random_values[-5])



            #type()

"""From python's perspective, lists are defined as objects with the data type 
'list':"""
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

            #list() Constructor

"""It is also possible to use the list() constructor when creating a new list."""

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)






            #Practice

cars = ["BMW","TOYOTA","TESLA","KIA"]
print("List of cars: "+str(cars))

print("One before last item :" +cars[-2])

print(cars[1]=="TOYOTA")

mixed_values = ["jim",3500,"Alex",2.53,True]

print(mixed_values[0:4])

            # Add "Alpha-Romeo" into the list                            .append

cars.append("Alpha-Romeo")
print("Updated cars list :" +str(cars))

            #Insert a value on a specific position in a list             .insert

cars.insert(2,"TATA")
print("After inserting Tata into the list : " +str(cars))

            # Remove an item by mentioning the value                     .remove

cars.remove("TATA")
print("After removing tata from the list : " +str(cars))

            #Remove an item by mentioning the cell index                  .POP
cars.pop(2)
print("Removing Tesla from the list : "+str(cars))



            #Practice for List collection (Advance)

list_of_employees = ["Adam","John","Greg","Danna","Ashy"]

            # length of the list
"""length_of_employees_list = len(list_of_employees)"""

print("Length of the employees list :"+str(len(list_of_employees)))

            # Inserting "Jack" in place of "John"
list_of_employees[1] = "Jack"
print("New list of employees : "+str(list_of_employees))


"""
Another way to add a value in a specific place

Change a range of item values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

If you insert more items than you replace, the new items will be inserted where
you specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

ANS = ['apple', 'blackcurrant', 'watermelon', 'cherry']
"""

list_of_employees.insert(3,"Mavrik")
print("Mavrik joined in the list of employees : " +str(list_of_employees))

list_of_employees.pop(3)
print("Mavrik is removed from the list : "+str(list_of_employees))

            # Sort the list of employees by 'abc'
list_of_employees.sort()
print("Sorted list : "+str(list_of_employees))


#ZIP() Function
 #It combines two or more iterbales (like lists, tuples or strings) element-wise into a single iterable of tuples

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

zipped = zip(names, ages)
print(list(zipped))


>>>>>>> 77a7026290cffc14ad5280317110e1c4e2e6e29e
