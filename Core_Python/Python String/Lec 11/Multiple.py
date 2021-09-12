class Animal:
    def eat(self):
        print('Eating...')


class Dog:
    def bark(self):
        print('Barking...')


class BabyDog(Animal, Dog):
    def weep(self):
        self.eat()

        self.bark()

        print('Weeping...')


d = BabyDog()

d.weep()

# d.eat()

# d.bark()
