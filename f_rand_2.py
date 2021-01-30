# original example from https://stackoverflow.com/questions/3603502/prevent-creating-new-attributes-outside-init
class FrozenClass(object):
    __isfrozen = False

    def __setattr__(self, key, value):
        print(key)
        print("class __isfrozen id   ", id(FrozenClass.__isfrozen))
        print("instance __isfrozen id", id(self.__isfrozen))
        if self.__isfrozen and not hasattr(self, key):
            raise TypeError( "%r is a frozen class" % self )
        object.__setattr__(self, key, value)

    def _freeze(self):
        self.__isfrozen = True

class Test(FrozenClass):
    def __init__(self):
        print("before self.x = 42")
        self.x = 42
        print("before self.y = 2**3")
        self.y = 2**3
        print("before self._freeze()")
        self._freeze() # no new attributes after this point.


def test1():
    a,b = Test(), Test()
    a.x = 10
    b.z = 10 # fails


# ----------------------------------------------------------------------------------------------
# my version
class ClassWithFreeze:
    __is_frozen = False

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__is_frozen = True


    def __setattr__(self, key, value):
        if self.__is_frozen and key not in self.__dict__.keys():
            raise TypeError( "%r is a frozen class" % self)
        else:
            self.__dict__[key] = value

    def __repr__(self):
        return f"ClassWithFreeze object. x = {self.x}, y = {self.y}."


def test2():
    var1 = ClassWithFreeze(3,5)
    print(var1)
    var1.x = 8
    var1.y = 55
    print(var1)
    # var1.z = 8 # should fail here
    var2 = ClassWithFreeze(300,500)
    print(var2)
    var2.x = 800
    var2.y = 5500
    print(var2)


if __name__ == '__main__':
    # test1()
    test2()
