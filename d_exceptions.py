
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("division by 0!")
    except TypeError:
        print("incorrect input types!")



def main():
    a = div(4 , 0)
    b = div("cat", 8)
    c = div(5, 2)
    print("c:", c)


if __name__ == "__main__":
    main()