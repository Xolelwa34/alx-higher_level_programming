#!/usr/bin/python3
def multiple_returns(sentence):
    mul = len(sentence)
    char = sentence[0] if mul > 0 else "None"
    high = mul, char
    return(high)
