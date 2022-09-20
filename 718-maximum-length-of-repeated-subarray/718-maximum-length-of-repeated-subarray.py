class Solution(object):
    def findLength(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        r = len(A) + 1
        c = len(B) + 1
        if r == 1 or c == 1:
            return 0
    
        dp = [[0] * c for _ in range(r)]
        res = 0
    
        for i in range(1, r):
            for j in range(1, c):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])          
        return res