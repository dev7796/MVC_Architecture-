class Animal:
    def eat(self):
        print('This is Animal')


class Dog(Animal):
    def bark(self):
        print('This is Dog')


class BabyDog(Animal):
    def weep(self):
        self.eat()

        self.bark()

        print('This is BabyDog')

class Puppy(Dog):
    def meow(self):
        self.eat()
        print("This is Puppy")

class SmallDog(BabyDog,Puppy):
    def bark(self):
        print("This is SmallDog")

class Cat(SmallDog):
    def bark(self):
        print("This is Cat")


d = Cat()

d.weep()

d.eat()

d.bark()

d.meow()

Dog.bark(d)
SmallDog.bark(d)
'''Flow... Animal >>> Dog >>> Puppy 
                          >>> SmallDog
                  >>> BabyDog >>> SmallDog 
                              >>> Cat '''