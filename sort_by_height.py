def sortByHeight(a):
    sorted = False
    i = 0
    j = 1
    swap = True
    counter = 0
    while counter < len(a):
        counter += 1
        print(a[i], a[j])
        if j == len(a)-1:
            if swap == False:
                return a
            i = 0
            j = 1
            continue

        if a[i] == -1 or a[j] == -1:
            i += 1
            j += 1
            continue

        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            swap = True
            i += 1
            j += 1
            print(a[i], a[j])
        else:
            i += 1
            j += 1
    return a


        

        



    # use bubble sort but exclude negative one and leave in place
    # bubble sort
    # sorted = False
    # compare adjacent elements
    # if no swaps return the array


a = [-1, 150, 190, 170, -1, -1, 160, 180]
print(sortByHeight(a))