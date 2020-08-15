def commonCharacterCount(s1, s2):
    # find the longer string
    max_string = max(s1, s2)
    min_string = min(s1, s2)
    chars_map = {}
    max_char_list = list(max_string)
    min_char_list = list(min_string)
    result = 0
    
    for char in max_char_list:
        if chars_map.get(char) == None:
            chars_map[char] = 1
        else:
            chars_map[char] += 1

    for char in min_char_list:

        if chars_map.get(char) == None:
            continue

        if chars_map.get(char) is not 0:
            chars_map[char] -= 1
            result += 1

    return result



    

s1 = "aabcc"
s2 = "adcaa"
print(commonCharacterCount(s1,s2))
