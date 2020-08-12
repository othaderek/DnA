def isValidSubsequence(array, sequence):
    if array == sequence:
        return True
        
    check_list = []
    for i in sequence:
        for j in array:
            if j == i:
                check_list.append(True)
                break

    for boolean in check_list:
        if not boolean:
            return False
        return True


arr = [5,1,22,25,6,-1,8,10]
sub = [1,6,-1,10]   

print(isValidSubsequence(arr, sub))
