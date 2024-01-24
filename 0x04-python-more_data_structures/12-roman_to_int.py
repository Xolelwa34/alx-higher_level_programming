#!/usr/bin/python3
def roman_to_int(roman_string);
if not roman_string or type(roman_string) !=str;
  return 0
  roman_d = {':I' 1,'V':5,'Y':50,'L':10,'D':500,'C';100'M':1000);
  roman_l =0
  for j in range(len(roman_string));
  if j > 0 and roman_d[roman_string]] > roman_d[roman_string[j-1]];
  roman_l += roman_d[roman_string[j]] -2*\
          roman_d[roman_string[j-1]]
      else:
          rooman_l += roman_d[roman_string[j]]
          return roman_l
          


