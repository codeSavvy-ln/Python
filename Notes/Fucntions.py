"""
append() - appends a new value into list
extend() - extends the list
sort()  - Sort the list into ascending order
sort(reverse = True) - Sort the list in descending order
sort(key=str.lower)  -
reverse() - Reverse the order of the list
remove() - To remove the item fromt the set.
pop() - Removes the random item from the set. In list a specific value can be removed by giving its index value
discard() - To remove an item from set. Advantage over remove - does not hit error if the item does not exist.
copy() - copy a list into new list
add() - to add a new value into set
update() - to add the whole date type(Set/list) too another set
instersaction() - will return a new set with items common in both x and y set - z = x.intersaction(y)
intersaction_update() - Keeps only those value which are present in both x & y set - x.intersaction_update(y)
symmetric_difference() - will return a new set with items that are not common in both x and - z = x.symmetric_difference(y)
symmetric_difference_update - will only return those items that are uncommon in both x and y set - x.symmetric_difference_update(y)

keys() - Will fetch all the key from the dict
values() - will fetch all the values from the dict
item() - will return both key and item from the dict
popitem() - removes the last inserted item{"key":"value"}

"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

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

#ZIP(list_1,list_2) Function
 #It combines two or more iterbales (like lists, tuples or strings) element-wise into a single iterable of tuples

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

zipped = zip(names, ages)
print(list(zipped))

#isinstance(object,type) - To validate data types on python
 #This function returns True if the specified object is of the specified type, Otherwise False.

test = isinstance(5,int)
print(test)
print(isinstance("test",str))


#reversed(list) - reverse the iterable object

list = [1,2,3,4,5]
result = reversed(list)
for x in result:
  print(x)

#sorted(list) - It sorts the result in ascending order as default and use reverse=True if you want to sort the result in descending order.

#To sort in ascending order
a = [1,7,2,6,8,4,9,5]
result = sorted(a)
print(result)

#To sort in descending order
a = [1,7,2,6,8,4,9,5]
result = sorted(a,reverse=True)
print(result)

#Global() Function in python - Fetches (in key:Value pair) whatever variable, function, collections etc you created
"""
var = globals()
print(var)
"""
#Locals() - Gives you local specific objects

# Split() - Work as a delimiter to specify where you want to split the data.
  # It will always return in list

string = "This is a simple string which i can split into words bsaed on space"
output = string.split(" ")
print(output)

#Strip() - Removes white spaces from the beginning and end of the string.
 #lstrip() removes the space from left side
 #rstrip() removes the space from right side
spaces= " Pyspark"
output1 = spaces.strip()
print(spaces, output1)

#Capitalize - First word will be capitalize
cap = "thing"
output2 = cap.capitalize()
print(output2)


"""
#Returns only the even number from 0 to 20 - isn't woring currently
def func_odd(num):
  if num%2==0:
    return True
data = range(20)
print(list(filter(func_odd,data)))

print(list(filter(lambda a: a%2==0,data)))

"""

#List Comprehensions

square = [x**2 for x in range(0,11)]
Even = [x for x in range(10) if x%2==0]
print(square)
print(Even)

#assert() - it will be used for data validation purposes. will not return anything if the condition passes but it will return message after comma if the condition fails.
t=6
s=6
assert t==s,"t is not equla to s"
print("assertion passed")