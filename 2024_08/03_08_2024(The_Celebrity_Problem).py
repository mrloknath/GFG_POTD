class Solution:
    def celebrity(self, mat):
        # code 
        n = len(mat)
        for i, r in enumerate(mat):
            if sum(r) == 0 and sum([mat[j][i] for j in range(n)]) == n-1:
                return i
        return -1
