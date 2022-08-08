class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0]*n for i in range(m)]
        oddcount = 0
        for i in indices:
            row=i[0];col=i[1]
            for j in range(n):
                matrix[row][j]+=1
                if matrix[row][j]%2==0:
                    oddcount-=1
                else:
                    oddcount+=1
            for k in range(m):
                matrix[k][col]+=1
                if matrix[k][col]%2==0:
                    oddcount-=1
                else:
                    oddcount+=1
        return oddcount