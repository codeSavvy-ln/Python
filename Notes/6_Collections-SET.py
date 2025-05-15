# fruit_set_collection = {“banana”, “apple”, “berry”} = we cannot access a ‘set’ cell by index. But what we can do is, to check if it exists by using a boolean statement.
#If we will have duplicate items inside a ‘set’, once printing it, python willignore the dublications and will print only 1 of the duplicated items.


# LIST                                                      #SET

# Square brackets []                                    Curly brackets{}
# Ordered collection (has index & cell values)          Unordered collection
# It can contain several cells with same values         It cannot have more than 1 cell with same values
# Value can be changed and added once list is created   you cannot change the value once created but you can add it


"""Note: The values True and 1 are considered the same value in sets, and are
treated as duplicates:

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
"""

fruit_set_collection = {"banana", "apple", "berry"}
print(fruit_set_collection)

#Print 'TRUE' if banana exists in the set collection otherwise 'FALSE'
print("banana" in fruit_set_collection)

# Remove banana from the set collection                                                   .discard
fruit_set_collection.discard("banana")
print(fruit_set_collection)
# Add 'Cherry' into the set collection                                                    .append
fruit_set_collection.add("Cherry")
print(fruit_set_collection)

                                    #Practice

drinks = {"Cola", "Sprite", "Beer", "Water"}

#Add soda into the set. However there is already soda exists in the set so, it will print only once
drinks.add("Soda")
print("Adding soda into the set collection: " + str(drinks))

# Delete Soda from the set

drinks.discard("Soda")
print("Deleting soda from the set collection: " + str(drinks))

# Length of the set collection
print("length of the set collection: " + str(len(drinks)))

#

drinks_1 = drinks.copy()
print("Dublicate 'drinks' set collection: " + str(drinks_1))
