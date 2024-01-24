#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    replace_dic = a_dictionary.copy()
    for key in replace_dic.keys():
        replace_dic[key] *= 2
    return replace_dic
