class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A = [[n*n]]
        print(A)
        while A[0][0] > 1:
            A = [range(A[0][0] - len(A), A[0][0])] + list(zip(*A[::-1]))
        return A * (n>0)
        