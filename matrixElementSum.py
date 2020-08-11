def matrixElementsSum(matrix):
    # loop over each array simlutaneously
    # add numbers not underneath a zero
    # as soon as I see a zero i rule out the rest everything underneath it
    matrixSum = 0
    l_to_r = 0
    t_to_b = 0
    while l_to_r < len(matrix[0]):
        while t_to_b < len(matrix):
            print(f"top to bottom: {t_to_b} " , f"left to right: {l_to_r}" , f"element: {matrix[t_to_b][l_to_r]}")
            if matrix[t_to_b][l_to_r] == 0:
                t_to_b = 0
                break
            matrixSum += matrix[t_to_b][l_to_r]
            t_to_b += 1
        if l_to_r < len(matrix[0]):
            t_to_b = 0
        l_to_r += 1

    return matrixSum
    



matrix=[[1,1,1,0], 
        [0,5,0,1], 
        [2,1,3,10]]
print(matrixElementsSum(matrix)) # => 9 