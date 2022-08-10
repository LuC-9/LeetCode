class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n=len(mat)
        p=q=r=s=True
        for i in range(n):
            for j in range(n):
                if mat[i][j]!=target[i][j]:
                    p=False
                if mat[i][j]!=target[j][n-i-1]:
                    q=False
                if mat[i][j]!=target[n-i-1][n-j-1]:
                    r=False
                if mat[i][j]!=target[n-j-1][i]:
                    s= False
        return p or q or r or s