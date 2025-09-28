# Replace ___ with your code

# create the Animal class
class Animal:
    def eat(self):
        print('I can eat food')

# create the Dog class
class Dog(Animal):
    def bark(self):
        print('I can bark')
    def eat(self):
        super().eat()

# create an object of the Dog class
dog1 = Dog()

# call the eat() method using the object
dog1.eat()