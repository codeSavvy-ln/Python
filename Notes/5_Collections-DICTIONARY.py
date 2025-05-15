### Dictionary is an unordered type of collection and declared by curly brackets {} . {'Key' : 'Value'}

"""
To access the item from dict, there are 2 ways:
1. Use Key name inside square bracket - ["brand'}
2. Use .get() function - get('brand')
"""
dictrionary_example = {'name': 'Rachel', 'test-grade': 98, 'Salary': 50000}

# two ways of fetching data from dictionaries                                                .get
print('Print name Key Value without using .get :' + str(dictrionary_example['name']))

print('Print name Key Value with using .get :' + str(dictrionary_example.get('name')))
new_employee = {'first_name': 'David'}



# Remove key-value from a dictionary





dictrionary_example.pop('Salary')
print("Removing salary from dict :" + str(dictrionary_example))




# print all 'Keys' of the dictionary
print("Keys :" + str(dictrionary_example.keys()))




# print all 'values' of the dictionary
print("Values :" + str(dictrionary_example.values()))




# use a variable and place it inside a new dictionary
company_value = "Google"
Job_title = "Developer"
new_dictionary = {"Company": company_value, "Job title": Job_title}

print("new dictionary :" + str(new_dictionary))




###Add a new cell into a Dict

new_dictionary["Salary"] = 10000
print("New Dict after adding Salary: " + str(new_dictionary))


print("\n")

#Check if key(only key not value) does exist in dict?

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")



# PRACTICE

Alex = {"Age": 32, "Married": 'Yes', "Kids": 3}
print("Alex's age: " + str(Alex["Age"]))
print("Is alex married: " + str(Alex["Married"]))
print("How many kids does alex has: " + str(Alex["Kids"]))

# Alex had a birthday and now is 33, update the value that belongs to the key =‘Age’

Alex_Age = {"Age": 33}
Alex.update(Alex_Age)
print("Alex dict after a year: " + str(Alex))

Alex_kids = {"Kids": 4}
Alex.update(Alex_kids)
print("Alex Dict after having another child: " + str(Alex))

# Print out the keys of the dictionary

print("The key keys are: " + str(Alex.keys()))

# Print out the values of the dictionary
print("The key values are: " + str(Alex.values()))

# ADVANCE

# There are two types of cells in nested dictionary - Parent and child cell
joe = {"Age": 35, "Kids": {"David": 'Boy', "Lisa": 'Girl'}}

print("all Joe: " + str(joe["Kids"]))

# print the gender of david
print("all Joe: " + str(joe["Kids"]["David"]))

# Clean the dictionary                                            .clear
# print("Clean the dictionary: "+str(joe.clear()))

# Create a copy of an existing Dict                                .Copy
print("Copy of Joe Dict: " + str(joe.copy()))

# Prctice (Advance)

buliding_attendants = {"Floor_1": {"First_apartment": 'Rachel', "Second_appartment": 'Jeen'},
                       "Floor_2": {"Third appartment": 'Jack'}}

# Print all nested cell items of the 1st floor
print("All nested items of the first floor: " + str(buliding_attendants["Floor_1"]))

# Print out the resident in the ‘second_apartment’
print("Resident in second appartmet is: " + str(buliding_attendants["Floor_1"]["Second_appartment"]))

# Caroll moved into the 4th appartment on the second floor
buliding_attendants["Floor_2"]["Fourth appartment"] = 'Caroll'

print("Caroll moved into the 4th appartment on the second floor: " + str(buliding_attendants))

# Building owner decided to let his daughter live in the first appartment so rachel has to move from that appartment

# Removing first floor from the dictionary

##### buliding_attendants["Floor_1"].pop("First_apartment")
##### print("Removing Floor_1 from the Dict: "+str(buliding_attendants))


# Owners daughter shifted into0 first floor

owners_daughter = {"First_apartment": 'Daughter'}
buliding_attendants["Floor_1"].update(owners_daughter)
print("Owners daughter gets shifted into first floor: " + str(buliding_attendants))