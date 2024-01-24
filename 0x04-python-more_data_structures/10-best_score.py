#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        students_score = len(a_dictionary.values())
        if students_score > 0:
            score = max(a_dictionary.values())
            for key in a_dictionary.keys():
                if a_dictionary[key] == score:
                    return key
    return None
