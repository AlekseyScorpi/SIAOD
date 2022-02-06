def printMat(mat):
    for line in mat:
        out = [str(el) for el in line]
        print(" ".join(out))


def func(mat):
    m = len(mat)
    n = len(mat[0])
    result = [[0 for j in range(n)] for i in range(m)]
    if m > n:
        for i in range(m - 1, -1, -1):
            temp = []
            j = 0
            while (i + j < m) & (j < n):
                temp.append(mat[i + j][j])
                j += 1
            temp.sort()
            j = 0
            while (i + j < m) & (j < n):
                result[i + j][j] = temp[j]
                j += 1
        for i in range(1, n):
            temp = []
            j = 0
            while (i + j < n) & (j < m):
                temp.append(mat[j][i + j])
                j += 1
            temp.sort()
            j = 0
            while (i + j < n) & (j < m):
                result[j][i + j] = temp[j]
                j += 1

    else:
        for i in range(m - 1, -1, -1):
            temp = []
            j = 0
            while (i + j < m) & (j < m):
                temp.append(mat[i + j][j])
                j += 1
            temp.sort()
            j = 0
            while (i + j < m) & (j < m):
                result[i + j][j] = temp[j]
                j += 1
        for i in range(1, n):
            temp = []
            j = 0
            while (i + j < n) & (j < m):
                temp.append(mat[j][i + j])
                j += 1
            temp.sort()
            j = 0
            while (i + j < n) & (j < m):
                result[j][i + j] = temp[j]
                j += 1
    return result


a = [[8, 2, 3, 4], [5, 7, 1, 0], [12, 3, 81, 17]]
b = [[8, 2, 3, 4], [41, 7, 1, 0], [3, 5, 7, 9], [9, 5, 7, 3], [0, 10, 20, 5]]
print("Origin matrix:")
printMat(a)
print("Sorted matrix:")
printMat(func(a))
