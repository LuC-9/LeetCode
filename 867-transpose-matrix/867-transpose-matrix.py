class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        l=[[] for y in range (len(matrix[0]))]
        for i in range (len(matrix)):
            for j in range (len(matrix[0])):
                l[j].append(matrix[i][j])
        return l    