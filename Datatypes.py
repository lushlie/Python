age = 67   #integer
height = 1.65    #float
greeting = "hiii"  #string
mammal = True  #boolean

#Data Structures multiple values stored in a single data

cars = ["mercedes", "porche", "toyota", "bmw"]   #list - ordered and changeable
fruits = ("apple", "banana", "cherry")    # tuple - ordered and unchangeable
countries = {"italy", "kenya","france"}    #set - unordered and unchangeable
capitals = {"kenya": "nairobi", "china": "beijing", "russia": "moscow"}   #dictionary - ordered and changeable
#typecasting - changing value's datatypes
#explicit manualing changing
name = "bro"
age  = 21
gpa = 1.9
student = True

age = float (age)
print(age)
gpa = int (gpa)
print(gpa)
student = str  (student)
print(student)
age = bool (age)
print(age)

#implicit auto changing
x = 2
y = 2.0
x = x / y
print(x)


#to see it's  datatype
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

print(cars)
print(fruits)
print(countries)
#print(dir(capitals))
#print(help(capitals))
print(capitals.get("kenya"))