number = int(input("Enter a number :"))

#condition returning reminder of no.
if number == 0:
    print("The number is neutral")
elif number % 2 == 0:
    print("even")
else:
    print("odd")