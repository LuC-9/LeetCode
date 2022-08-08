class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s=0
        n=len(mat)
        for i in range(len(mat)):
            s+=mat[i][i]
            if n-i-1!=i:
                s+=mat[n-i-1][i]
        return s    