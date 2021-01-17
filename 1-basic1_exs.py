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


# ex5
def flip_int(number):
    reversed_num = 0
    factor = 1
    if type(number) == str:
        number = int(number)
    if number < 0:
        factor = -1
        number = -number
    while number:
        reversed_num = reversed_num * 10 + number % 10
        number //= 10
    return reversed_num * factor


# ex6
def grade_calculator(num_grade: int):
    grade = None
    if num_grade in range(10):
        grade = "F"
    elif num_grade in range(10, 30):
        grade = "E"
    elif num_grade in range(30, 50):
        grade = "D"
    elif num_grade in range(50, 70):
        grade = "C"
    elif num_grade in range(70, 90):
        grade = "B"
    elif num_grade in range(90, 101):
        grade = "A"
    else:
        raise ValueError (f"{num_grade} is not a valid grade!")
    return grade



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

    print("flip_int(155):", flip_int(155))
    print("flip_int(2):", flip_int(2))
    print("flip_int(-690):", flip_int(-690))
    print('flip_int("12345"):', flip_int("12345"))

if __name__ == '__main__':
    main()
