class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ms=nums[0]
        cs=0
        for i in range(len(nums)):
            cs+=nums[i]
            if ms <= cs:
                ms=cs
            if cs < 0:
                cs=0
        return ms