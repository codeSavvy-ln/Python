                    #Check String is present or not in the variable

"""To check if a certain phrase or character is present in a string, we can use the
keyword in and not in keyword to check if the string is not present """

txt = "The best things in life are free!"
print("free" in txt)


                    #Slicing variable - to specify range of variables

b = "Hello, World!"
print(b[2:5])

c = "Hello, World!"
print(c[:5])

d = "Hello, World!"
print(d[2:])
                    #Negative Indexing
d = "Hello, World!"
print(d[-5:-2])

                    #Modify Strings

e = "Hello, World!"
print(e.strip())                         #Upper case/Lower Case letters

"""
.strip = Whitespace is the space before and/or after the actual text
.replace = replaces a string with another string
.split = splits the string into substrings if it finds instances of the separator:

"""

                    #Format-String  - to combine both string and numbers

"""The format() method takes the passed arguments, formats them, and places them 
in the string where the placeholders {} are:"""

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#format can take unlimited no. of arguments and place them into respective placeholders

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


"""
You can use index numbers {0} to be sure the arguments are placed in the correct 
placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

"""

                    #Escape Characters (\)- Inserts charac that are illegal in string

txt1 = "We are the so-called \"Vikings\" from the north."
print(txt1)
"""
\'	    Single Quote	
\\	    Backslash	
\n	    New Line	
\r	    Carriage Return	
\t	    Tab	
\b	    Backspace	
\f	    Form Feed	
\ooo	Octal value	
\XHH (in small letters)	Hex value
"""