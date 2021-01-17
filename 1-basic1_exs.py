#  ex1
def is_even(number: int):
    return number % 2 == 0


# ex2
def print_str_number_times(string: str, number: int=1):
    for i in range(number):
        print(string)


# ex3
def is_leap_year(year: int):
    if year % 4 == 0 and year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0


# ex4
def is_int(input):
    return type(input) == int


def main():
    print("is_even(5):", is_even(5))
    print("is_even(8):", is_even(8))
    print("is_even(8.5):", is_even(8.5))  # warning for type error

    print_str_number_times("bla!")
    print_str_number_times("bla!!", 5)

    print("is_leap_year(1855):", is_leap_year(1855))
    print("is_leap_year(1600):", is_leap_year(1600))
    print("is_leap_year(1700):", is_leap_year(1700))

    print("is_int(5):", is_int(5))
    print("is_int(5.5):", is_int(5.5))
    print("is_int('bla'):", is_int('bla'))


if __name__ == '__main__':
    main()
