#leap year
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not leap year")

#if - 1 condition (true)
#elif - another condition (checks if 1 was false)
#else - (checks if none is true)