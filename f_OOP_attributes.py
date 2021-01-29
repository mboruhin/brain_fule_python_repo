# ex1
class X:
    def __init__(self, x):
        self.x = x

    def __getattr__(self, item):
        print(f'Impossible to find an attribute named "{str(item)}" in current X object')


# ex2
class Y:

    def __init__(self, y):
        self.y = y

    def __setattr__(self, key, value):
        expected_attrs = ['y']
        if key in expected_attrs:
            self.__dict__[key] = value
        else:
            # raise AttributeError(f"Y object has no '{key}' attribute")
            print(f"Y object has no '{key}' attribute")


class Z:
    __slots__ = ['z']

    def __init__(self, z):
        self.z = z



def main():
    var1 = X(1)
    a = var1.x
    b = var1.a

    var2 = Y(2)
    var2.y = 5
    print("var2.y:", var2.y)
    var2.z = 8

    var3 = Z(5.7)
    print("var3:", var3)
    print("var3.z:", var3.z)
    var3.z = 3.33
    print("var3.z:", var3.z)
    # print("var3.__dict__", var3.__dict__)  # AttributeError: 'Z' object has no attribute '__dict__'



if __name__ == '__main__':
    main()