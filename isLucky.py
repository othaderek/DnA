def isLucky(n):
    # split a number in half (not divide)
    string_num = str(n)
    string_list = list(string_num)
    num_list = [int(char) for char in string_list]
    first_three = num_list[0:int(len(num_list)/2)]
    last_three = num_list[int(len(num_list)/2):]
    print(first_three, last_three)
    if sum(first_three) == sum(last_three):
        return True
    return False
    # get length of string divide it by two and slice out those digits
    # turn num to string
    # number always has even digits
    # sum the left side with the right
    # if they match return true, else false

n = 1230
isLucky(n)