class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        dsum = 0
        for i in range(len(mat)):
            dsum+=mat[i][i]
            dsum+=mat[i][len(mat)-1-i]
        if len(mat)%2==1:
            dsum -= mat[len(mat)//2][len(mat)//2]
        return dsum