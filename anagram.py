def anagram(string1, string2):
    s1 = string1.replace(" ", "")
    s2 = string2.replace(" ", "")

    return sorted(s1) == sorted(s2)

# print(anagram("otha", "ahto"))

def anagram2(s1,s2):
    # Clean up strings
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    # Edge case
    if len(s1) != len(s2):
        return False
        
    count = {}

    # Loop through first string and count the occurence of each letter
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    # Loop through and subtract any occurences
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            counter[letter] = 1
    
    # check dictionary if any value is not 0 return false else true
    for k in count:
        if count[k] != 0:
            return False
    
    return True
    

print(anagram2("otha", "hto"))