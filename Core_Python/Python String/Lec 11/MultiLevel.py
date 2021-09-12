class Animal:
    def eat(self):
        print('Eating...')


class Dog(Animal):
    def bark(self):
	
        self.eat()

        print('Barking...')


class BabyDog(Dog):
    def weep(self):

        self.bark()

        self.eat()

        print('Weeping...')


d = BabyDog()

# d.eat()

# d.bark()

d.weep()
