

import re


Input_Str = "FOOTBALL"

def replace(Input_String, char_2_replace, replaced_char, n):
    pattern = re.compile(char_2_replace)
    if len(re.findall(pattern, Input_String)) >= n: 
        where = [m for m in pattern.finditer(Input_String)][n-1]
        before = Input_String[:where.start()]
        after = Input_String[where.end():]
        newString = before + replaced_char + after
    else: 
        newString = Input_String
    return newString

print(replace(Input_Str, 'L', 'X', 4))