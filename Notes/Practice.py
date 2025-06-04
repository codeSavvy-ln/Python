"""def is_leap(year):
    leap = False  # Default assumption: not a leap year

    # Leap year logic
    if year % 4 == 0:  # Divisible by 4
        if year % 100 == 0:  # Divisible by 100
            if year % 400 == 0:  # Divisible by 400
                leap = True
        else:
            leap = True

    return leap  # Return True if leap year, False otherwise

year = int(input("Enter a year: "))
print(is_leap(year))


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
coordinates = [[i, j, k]
               for i in range(x + 1)
               for j in range(y + 1)
               for k in range(z+1)
               if i + j + k != n]

print(coordinates)

a = True
b = False

if a and b or not a:
    print("Go")
else:
    print("Stop") 
                                                #Output: Stop (because if, the if statement returns false value then it will always print the else statement.



num = {1,4.5,5,23,2}
print(sum(num,start=10)) #output: 45


num = [4,5,2,3,-1,0,9]
sorted_nums_Ascending = sorted(num)
sorted_nums_Descending = sorted(num, reverse =True)


print(sorted_nums_Ascending)
print(sorted_nums_Descending)


people =[
{"name": "Alice", "age":30},
{"name": "Bob", "age":25},
{"name": "Charlie", "age":35},
]

sorted_keys = sorted(people,key = lambda x: x["age"], reverse = True)

print(sorted_keys)

tasks =["Write report", "Attend meeting","Review code","Submit timesheet"]

for x in range(len(tasks)):   or #for x, task in enumerate(tasks):
    print(f"{x +1}. {tasks[x]}")

                                                        #Output
                                                        1. Write report
                                                        2. Attend meeting
                                                        3. Review code
                                                        4. Submit timesheet

_____________________________________________________________________________________

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))  # Convert to list to reuse
    max_score = max(arr)
    score = [x for x in arr if x != max_score]
    sec = max(score)
    print(sec)
_____________________________________________________________________________________

"""
print("SS")
print("SS")
print("SS")