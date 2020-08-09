def countTinyPairs(a, b, k):
    i = 0
    j = len(a)-1
    tiny = 0
    while i < len(a):
        if int(str(a[i])+str(b[j])) < k:
            tiny += 1
        i += 1
        j -= 1
    return tiny


a = [1, 2, 3]
b = [1, 2, 3]
k = 31
print(countTinyPairs(a, b, k))
