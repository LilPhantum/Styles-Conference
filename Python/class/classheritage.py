#Class exmp
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Rex")
print(my_dog.bark())

print ( "\n***inheritance***" )

# inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} makes a sound"
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"
kitty = Cat("Whiskers")
print(kitty.speak())

print ( "\n***super***" )

#Using super ()
class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly
    def speak(self):
        base = super().speak()
        return base + (", and I can fly" if self.can_fly else ", but I cannot fly")
parrot = Bird("Polly", True)
print(parrot.speak())
    
print ( "\n***multiple***" )

# MULTIPLE INHERITANCE
class Flyer:
    def fly(self):
        return "Flying high"
class Walker:
    def walk(self):
        return "Walking fast"
class Bat(Flyer, Walker):
    pass
b = Bat()
print(b.fly())
print(b.walk())

print ( "\n***calass***" )

# CLASS VS INSTANCE ATTRIBUTES
class Car:
    wheels = 4 # class attribute
    def __init__(self, color):
        self.color = color # instance attribute
car1 = Car("red")
car2 = Car("blue")
print(car1.wheels, car2.color)

print ( "\n***private***" )

# PRIVATE VARIABLES
class Secret:
    def __init__(self):
        self.__code = "1234" # private variable
    def reveal(self):
        return self.__code
s = Secret()
print(s.reveal())
