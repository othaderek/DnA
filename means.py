import pdb

def meanGroups(a):
    result=[]
    mean_group = []
    i = 0
    for arr in a:
        mean = sum(arr)/len(arr)
        mean_group.append(int(mean))

    dictMap = {}
    index = 0
    for m in mean_group:
        if dictMap.get(m) == None:
            dictMap.__setitem__(m, [index])
        else:
            dictMap[m].append(index)
        index += 1
    print(dictMap.values())

meanGroups([[3, 3, 4, 2],
     [4, 4],
     [4, 0, 3, 3],
     [2, 3],
     [3, 3, 3]])
