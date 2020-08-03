import pdb

def makeArrayConsecutive2(statues):
    statues.sort()
    left = 0
    right = 1
    needs = 0
    while right < len(statues):
        if statues[right] - statues[left] == 1:
            left+=1
            right+=1
        else:
            new_num = statues[left] + 1
            statues.insert(right, new_num)
            left+=1
            right+=1
            needs+=1
    return needs
print(makeArrayConsecutive2([6, 2, 3, 8]))