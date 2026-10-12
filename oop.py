#object oriented programming
#class -bliueprint/ sketch

class student:    #characterics
  def __init__(self,name,age,gender,course):
      self.name = name
      self.age = age
      self.gender = gender
      self.course = course

  def study(self):  #behaivour
        print("Student is studying")
  def sing(self):
        print("Student is singing")

#object - final/real
student1 = student("James", 13, "male","mit")
print(student1.age)
student1.study()
print()
student2 = student("mary", 12, "female", "mit")

student3 = student("ken", 14, "male", "mit")

#polymorphism- to have many forms or faces

#1. inheritance- object like parent class
from abc import ABC,abstractmethod
class shape:
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2 #area of circle

class square(shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2 #area

class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height * 0.5

shapes = [circle(4),square(5),triangle(6, 7)]
for shape in shapes:
    print(f"(shape.area())cm")


#2. duck typing- object  must have methods


#encapsulation- protects objects data from being changed, keeping same data together
class bankaccount:
    def __init__(self, balance):
       self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = bankaccount(1000)
account.deposit(500)
print(account.get_balance())
