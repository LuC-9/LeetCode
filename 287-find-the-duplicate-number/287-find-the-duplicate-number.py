class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            ab=abs(i)
            if nums[ab-1]<0:
                return ab
            nums[ab-1]*=-1
        return -1
        