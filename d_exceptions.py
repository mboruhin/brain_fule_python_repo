
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("division by 0!")
    except TypeError:
        print("incorrect input types!")
        raise # re-raising the current exception


def main():
    a = div(4, 0)
    try:
        b = div("cat", 8)
    except TypeError:
        print("in main - incorrect input types!")

    c = div(5, 2)
    print("c:", c)


if __name__ == "__main__":
    main()