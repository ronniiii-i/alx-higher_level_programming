#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            elif not (isinstance(my_list_1[i], (int, float)) and
                      isinstance(my_list_2[i], (int, float))):
                raise TypeError("wrong type")
            elif my_list_2[i] == 0:
                raise ZeroDivisionError("division by 0")
            else:
                result.append(my_list_1[i] / my_list_2[i])
        except IndexError as e:
            print(e)
        except TypeError as e:
            print(e)
        except ZeroDivisionError as e:
            print(e)
        finally:
            result.append(0)
    return result
