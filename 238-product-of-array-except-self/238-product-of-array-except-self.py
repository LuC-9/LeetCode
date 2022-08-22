class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        p = 1
        for n in nums:
            res.append(p)
            p*= n
        p = 1
        for i in reversed(range(len(nums))):
            res[i]*= p
            p*= nums[i]    
        return res