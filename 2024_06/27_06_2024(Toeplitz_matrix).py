def isToepliz(mat):
    #code here
    ans = []
    for i in range(len(mat) - 1):
        for j in range(len(mat[0]) - 1):
            if mat[i][j] != mat[i+1][j+1]:
                return False
    return True
