def mutateTheArray(n, a):
    i = 0
    b=[]
    while i < len(a):
        if i == 0:
            b.append(0 + a[0] + a[1])
        elif i+1 == len(a):
            b.append(a[i - 1] + a[i] + 0)
        else:
            b.append(a[i - 1] + a[i] + a[i + 1])
        i +=1
    return b
    # if i == 0 or i >len(a)-1
    
print(mutateTheArray(5, [4, 0, 1, -2, 3]))