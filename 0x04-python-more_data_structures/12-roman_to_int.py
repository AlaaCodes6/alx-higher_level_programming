#!/usr/bin/python3
def subtract(list_num):
    to_subtract = 0
    max_list = max(list_num)

    for num in list_num:
        if max_list > num:
            to_subtract += num

    return (max_list - to_subtract)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(r_dict.keys())

    n = 0
    last_rom = 0
    list_num = [0]

    for i in roman_string:
        for r_num in list_keys:
            if r_num == i:
                if r_dict.get(i) <= last_rom:
                    num += subtract(list_num)
                    list_num = [r_dict.get(i)]
                else:
                    list_num.append(r_dict.get(i))

                last_rom = r_dict.get(i)

    n += subtract(list_num)

    return (n)
