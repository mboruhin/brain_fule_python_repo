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


a,b = Test(), Test()
a.x = 10
b.z = 10 # fails

# ----------------------------------------------------------------------------------------------
f = FrozenClass()
print(type(f))
print(f.__dict__)