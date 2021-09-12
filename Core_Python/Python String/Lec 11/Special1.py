class Animal:

    def eat(self):
        print('Eating...')


class Dog(Animal):

    def eat(self):
        # Animal.eat(self)

        print('Barking...')


d = Dog()

d.eat()


a = Animal()
a.eat()

Animal.eat(a)
Animal.eat(d)

