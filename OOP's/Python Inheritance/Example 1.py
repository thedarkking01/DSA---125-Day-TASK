class Animal:
    def eat(self):
        print("I can eat")

# derive Dog from Animal      
class Dog(Animal):
    def bark(self):
        print("I can bark")

# derive Cat from Animal
class Cat(Animal):
    def get_grumpy(self):
        print("I am getting grumpy.")

# object of Dog
dog1 = Dog()

dog1.bark()
dog1.eat()

# object of Cat
cat1 = Cat()
cat1.eat()