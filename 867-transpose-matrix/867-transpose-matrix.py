class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        import numpy as np
        A=np.array(matrix)
        A=A.transpose()
        return A
        