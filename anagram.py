# Given two strings, check if they are anagrams of each other
def anagram2(s1,s2):
    # Clean up strings by removing white space
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    # Edge case that checks the length of both strings, if they don't have
    # the same amount of characters, they cannot be anagrams, thus False.
    if len(s1) != len(s2):
        return False

    # Create a dictionary that stores the frequency of each letter
    count = {}

    # Loop through first string and count the frequency of each letter
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    # Loop through the second string and subtract each occurence from count
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            counter[letter] = 1
    
    # check dictionary if any value is not 0 return false
    for k in count:
        if count[k] != 0:
            return False
    
    # return True 
    return True
    

print(anagram2("otha", "hto"))