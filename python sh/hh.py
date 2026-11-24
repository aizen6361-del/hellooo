def displayMatrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

def convertToSparseMatrix(matrix):
    sparseMatrix = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                temp = []
                temp.append(i)
                temp.append(j)
                temp.append(matrix[i][j])
                sparseMatrix.append(temp)

    print("\nSparse Matrix:")
    displayMatrix(sparseMatrix)

normalMatrix = [
    [9, 0, 0, 0],
    [0, 4, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 5],
    [6, 0, 0, 0]
]

displayMatrix(normalMatrix)
convertToSparseMatrix(normalMatrix)
