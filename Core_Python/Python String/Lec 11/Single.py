class Animal:
    def __init__(self):
        self.x=10
    def eat(self):

      print('Eating...')

class Dog(Animal):

    def bark(self):

        self.eat()

        print('Barking...')
        print(self.x)

d=Dog()

d.bark()

d.eat()


