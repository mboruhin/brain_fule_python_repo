import b_basic2_exs

random_global_var = 5

# ex1
def is_name_in_global_namespace(name: str):
    return name in globals()


# ex2
print(b_basic2_exs.letters_occurance("the dolphin is dead!"))

def main():
    print("is_name_in_global_namespace('random_global_var'):", is_name_in_global_namespace('random_global_var'))





if __name__ == '__main__':
    main()


# ex3
import MyPackage.module1
MyPackage.module1.foo()


from MyPackage.module2 import *

bar()
_bar()