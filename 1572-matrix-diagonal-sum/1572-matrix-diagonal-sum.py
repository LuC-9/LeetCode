class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s=0
        for i in range(len(mat)):
            s+=mat[i][i]
        for j in range(len(mat)-1,-1,-1):
            if len(mat)-1-j != j:
                s+=mat[len(mat)-1-j][j]
        return s    