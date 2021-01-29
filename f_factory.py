from abc import ABC, abstractmethod


class Animal:
    last_id = 0

    def __init__(self, classification: str):
        self.classification = classification
        Animal.last_id += 1
        self.id = Animal.last_id
        # print("Animal.__init__ finished")

    @classmethod
    def create(cls):
        raise NotImplementedError(f"you forgot to implement speak for class {cls.__name__}")

    def get_classification(self):
        return self.classification

    def get_id(self):
        return self.id

    def speak(self):
        raise NotImplementedError(f"you forgot to implement speak for class {self.__class__.__name__}")

    def __repr__(self):
        # raise NotImplementedError(f"you forgot to implement __repr__ for class {self.__class__.__name__}")
        return f"this is a {self.get_classification()} which is a {self.__class__.__name__} and his id is {self.get_id()}"


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self, "mammal")

    @classmethod
    def create(cls):
        return Dog()

    def speak(self):
        print("BARK!!!")

    # def __repr__(self):
    #     return f"this is a mammal which is a dog and his id is {Animal.get_id(self)}"


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self, "mammal")

    @classmethod
    def create(cls):
        return Cat()

    def speak(self):
        print("FUCK OFF")


class Carp(Animal):
    def __init__(self):
        Animal.__init__(self, "fish")

    @classmethod
    def create(cls):
        return Carp()

    def speak(self):
        print("...BLOOP...")










def main():
    dog1 = Dog.create()
    print("dog1.get_id():", dog1.get_id())

    dog2 = Dog.create()
    print("dog2.get_id():", dog2.get_id())
    print(dog2)

    cat1 = Cat.create()
    cat1.speak()

    fish1 = Carp.create()
    fish1.speak()
    print(fish1)
    print("dog1.get_id():", dog1.get_id())
    print("dog1.last_id", dog1.last_id)
    print("cat1.last_id", cat1.last_id)
    print("fish1.last_id", fish1.last_id)

if __name__ == '__main__':
    main()

