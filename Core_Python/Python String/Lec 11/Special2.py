class Animal:
    def eat(self):
        print('Eating...')


class Dog():
    def eat(self):
        print('Barking...')


'''
class BabyDog(Animal, Dog):
    def eat(self):

        print('Weeping...')


d = BabyDog()

d.eat()

'''


class BabyDog(Animal, Dog):
    pass


d = BabyDog()

d.eat()


class BabyDog(Animal, Dog):

    def eat1(self):
        print('Weeping...')


d = BabyDog()

d.eat()
