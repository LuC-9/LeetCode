class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n=[list(i) for i in matrix]
        for i,j in itertools.product(range(len(matrix)),range(len(matrix[0]))):
                  
            if n[i][j]!=0:
                continue
            for k in range (len(matrix[0])):
                matrix[i][k]=0
            for k in range (len(matrix)):
                    matrix[k][j]=0
                    
        """
        Do not return anything, modify matrix in-place instead.
        
        M, N, n = len(m), len(m[0]), [list(i) for i in m]
    	for i,j in itertools.product(range(M),range(N)):
    		if n[i][j]: continue
    		for k in range(N): m[i][k] = 0
    		for k in range(M): m[k][j] = 0
        """
        