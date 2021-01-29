class DemoClass:
    num = 101

    # a method
    def read_number(self):
        print(self.num)

    def change_num(self,val):
        self.num = val


obj1 = DemoClass()
print(obj1.__dict__)

obj1.read_number()
print("after obj1.read_number() dict is:", obj1.__dict__)

obj1.change_num(15)
print("after obj1.change_num(15) dict is:", obj1.__dict__)
obj1.read_number()

print("\ncreating another object")
obj2 = DemoClass()
obj2.read_number()
