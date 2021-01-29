class TestClass:
    class_var = "random str!"

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add_w(self, w):
        self.w = w


class Base:
    base_class_var = 5

    def __init__(self):
        self.x = 7.5

    def set_base_class_var(self, val):
        Base.base_class_var = val

    def __repr__(self):
        return f"base_class_var is: {self.base_class_var}"


class Derived(Base):

    def __init__(self, val):
        self.set_base_class_var(val)

    def __repr__(self):
        return f"base_class_var in Derived is: {self.base_class_var}"


def main():
    a = TestClass(1, 2, 3)
    print("a.__dict__:", a.__dict__)
    print("TestClass.__dict__:", TestClass.__dict__)
    a.add_w(4)
    print("a.__dict__:", a.__dict__)
    print("TestClass.__dict__:", TestClass.__dict__)
    print(a.class_var)

    # inheritance and base class variables
    base1 = Base()
    print(base1)
    base1.set_base_class_var(8)
    print(base1)
    base2 = Base()
    print(base2)
    print(Base.base_class_var)

    derived1 = Derived(38)
    print(derived1.__class__.__mro__)
    print(base2)
    # derived1.x = 9.7
    # print(derived1.__dict__)


    # d1 = Derived(6)





if __name__ == "__main__":
    main()
