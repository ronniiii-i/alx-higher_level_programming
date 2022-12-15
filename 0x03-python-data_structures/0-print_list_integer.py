def print_list_integer(my_list=[]):
    if not my_list:
        print("The list is empty")
    return
    for item in my_list:
        print("{}".format(int(item)))
