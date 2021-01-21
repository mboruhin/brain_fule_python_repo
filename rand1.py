from c_scopes_and_modules import is_name_in_global_namespace

aaaaaaaaaaaaaaaaaaaaa = 15

def crap1(number):
    bla = 0
    for x in range(number):
        print(x)
        bla = x
    return bla

def is_x_between_a_and_b(x, a, b):
    return x in range(a,b)

def main():
    print(crap1(5))
    # in_data = input()
    # print(type(in_data))
    print("is_x_between_a_and_b(5, 2, 6):", is_x_between_a_and_b(5, 21, 6))
    str1 = "the dolphin"
    str2 = " is dead"
    combined = str1 + str2
    print(combined)
    int_to_translate = 48
    print("the char:", chr(int_to_translate))

    set1 = {"live", "die", "repeat"}
    for x in enumerate(set1):
        num, string = x
        print("num:", num, "  string:", string)

    num_list = [1, 2, 4, 8, 9]
    str_list = ["dog", "cat", "bird"]
    result = zip(num_list, str_list)
    print(result)
    print(list(result))

    print("reversed(num_list):", reversed(num_list))
    print("num_list:", num_list)
    num_list.reverse()
    print(num_list)


    class Bla:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return f"x: {self.x}, y: {self.y}"

    bla1 = Bla(3, 5)
    print(bla1)
    print(bla1.__dict__)

    print(globals())
    print("is_name_in_global_namespace('random_global_var'):", is_name_in_global_namespace('random_global_var'))


if __name__ == '__main__':
    main()


