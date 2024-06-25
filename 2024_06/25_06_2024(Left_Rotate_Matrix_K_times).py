class Solution:
    def rotateMatrix(self, k, mat):
        n = len(mat)
        m = len(mat[0])
        effective_k = k % m
        rotated_mat = []
        for row in mat:
            new_row = row[effective_k:] + row[:effective_k]
            rotated_mat.append(new_row)
        return rotated_mat
