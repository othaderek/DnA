def digitAnagrams(a):
    # sort each number and count ever occurence of the same number return that
    arr=[]
    for num in a:
        numstr=str(num)
        arr.append(list(numstr))

    new_arr=[]
    # arr is a 2d list of string numbers
    # turn each number into an integer
    # sort the array of numbers


    newer_arr=[]
    for subarr in arr:
        array_of_single_ints=[]
        for char in subarr:
            array_of_single_ints.append(int(char))
        
        array_of_single_ints.sort()
        newer_arr.append(array_of_single_ints)
    
    second_2d_arr=[]
    for sub in newer_arr:
        string_arr=[]
        for num in sub:
            string_arr.append(str(num))
        second_2d_arr.append(string_arr)
    arr_to_check=[]
    for a in second_2d_arr:
        arr_to_check.append("".join(a))
    
    frequency_counter={}

    for string in arr_to_check:
        if frequency_counter.get(string)==None:
            frequency_counter.__setitem__(string, 0)
        else:
            frequency_counter[string] += 1

        sum_this=frequency_counter.values()
        result=sum(sum_this)+1

    return result

print(digitAnagrams([25, 35, 872, 228, 53, 278, 872]))
