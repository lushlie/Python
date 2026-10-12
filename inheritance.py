class Animal:
    isMammal = True
    hasFur = True

class Dog(Animal):
    def bark(self):
        print("Woof!! Woof!!")

class Cat(Animal):
    def meow(self):
        print("Meow!! Meow!!")


dog = Dog()
dog.bark()
print(dog.isMammal)

cat = Cat()
cat.meow()
print(cat.hasFur)

