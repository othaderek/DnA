import pdb
def reduceTheNumber(number, k):

    if len(number)<= k:
        print(number)
        return number

    a = [(number[i:i+k]) for i in range(0, len(number), k)] 
    new_arr = []
    nums=[]
    n=[]
    last_list=[]

    for numString in a:
        new_arr.append(list(numString))

    for subarr in new_arr:
        nums.append([int(i) for i in subarr])

    for array in nums:
        n.append(sum(array))

    for num in n:
        last_list.append(str(num))

    number=''.join(last_list)
    reduceTheNumber(number, k)
    
    # return number
    
    # if len(number) <= k end
    # split number into groups of k digits each, last group < k digits
    # sum digits in each array concat


print(reduceTheNumber("1111122222", 3))
