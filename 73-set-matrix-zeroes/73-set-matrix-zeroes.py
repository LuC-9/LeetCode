class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = set()
        column = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)          
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for i in column:
            for j in range(len(matrix)):
                matrix[j][i] = 0 
                    
        """
        Do not return anything, modify matrix in-place instead.
        
        M, N, n = len(m), len(m[0]), [list(i) for i in m]
    	for i,j in itertools.product(range(M),range(N)):
    		if n[i][j]: continue
    		for k in range(N): m[i][k] = 0
    		for k in range(M): m[k][j] = 0
        """
        