

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


if __name__ == '__main__':
    main()


