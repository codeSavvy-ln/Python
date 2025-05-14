<<<<<<< HEAD
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
"""

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

=======
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
"""

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

>>>>>>> 77a7026290cffc14ad5280317110e1c4e2e6e29e
