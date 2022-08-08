class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        import numpy as np
        matrix=np.array(matrix)
        matrix=matrix.transpose()
        return matrix
        