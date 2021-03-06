# ex1
def squared_upto(first_num: int, last_number: int):
    root = first_num
    squared = root ** 2
    list_of_squared = []
    while squared <= last_number:
        list_of_squared.append(squared)
        root += 1
        squared = root ** 2
    return list_of_squared

def squared_upto_with_for(first_num: int, last_number: int):
    max_root = int(last_number ** 0.5)
    list_of_squared = []
    for num in range(first_num, max_root + 1):
        list_of_squared.append(num ** 2)
    return list_of_squared


# ex2
def all_even_in_range_using_while(first_num: int, last_num: int):
    ret_list = []
    num = first_num
    while num <= last_num:
        if num % 2 == 0:
            ret_list.append(num)
        num += 1
    return ret_list


def all_even_in_range_using_for(first_num: int, last_num: int):
    ret_list = []
    for num in range(first_num, last_num + 1):
        if num % 2 == 0:
            ret_list.append(num)
    return ret_list


# ex3
def letters_occurance(string: str):
    letter_list = list(string)
    letter_set = set(letter_list)
    letter_dict = {}
    for letter in letter_set:
        letter_dict[letter] = letter_list.count(letter)
    return letter_dict


# ex4
def print_list_elements_with_index(obj_list):
    for index, item in enumerate(obj_list):
        print(f"index: {index}, element: {item}")

def print_dict_elements_with_index(obj_dict):
    for index, item in enumerate(obj_dict.items()):
        print(f"index: {index}, element: {item}")


# ex5
def combine_lists_with_no_duplicates(list1, list2):
    return list(set(set(list1) | set(list2)))


def combine_lists_with_no_duplicates_2(list1, list2):
    combined_list = list(list1 + list2)
    ret_list = []
    for element in combined_list:
        if element not in ret_list:
            ret_list.append(element)
    return  ret_list


# ex6
def rotate_list_left(orig_list, steps):
    steps = steps % len(orig_list)
    rev_list = orig_list[::-1]
    ret_list_l = rev_list[steps::-1]
    # print("ret_list_l:", ret_list_l)
    ret_list_r = rev_list[:steps:-1]
    # print("ret_list_r:", ret_list_r)
    return ret_list_l + ret_list_r


    return ret_list



def main():
    # ex1
    print(squared_upto(0, 100))
    print(squared_upto_with_for(0, 100))

    # ex2
    print(all_even_in_range_using_while(0, 100))
    print(all_even_in_range_using_for(0, 100))

    # ex3
    print(letters_occurance("the dolphin is dead!"))

    # ex4
    list2= ["bla", "blabla", "blablabla"]
    print_list_elements_with_index(list2)
    dict1 = {"first": "bla!", "second": "blabla!", "thied": "blablabla!"}
    print_dict_elements_with_index(dict1)

    # ex5
    list1 = [3, 5, 5, 9, 15, 15, 55, 495, 4238, "bla", "bla2"]
    list1 = [3, 5, 9, 15, 55, 495, 7.5, "bla"]
    combined_list = combine_lists_with_no_duplicates(list1, list2)
    print(combined_list)
    combined_list_2 = combine_lists_with_no_duplicates_2(list1, list2)
    print(combined_list_2)

    # ex6
    orig_list = ["a", "b", "c", "d", "e", "f", "g"]
    rotated_list = rotate_list_left(orig_list, 3)
    print("rotated_list:", rotated_list)


if __name__ == '__main__':
    main()