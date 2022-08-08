class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        l=[[0 for x in range (len(matrix))] for y in range (len(matrix[0]))]
        for i in range (len(matrix[0])):
            for j in range (len(matrix)):
                l[i][j]=matrix[j][i]
        return l      