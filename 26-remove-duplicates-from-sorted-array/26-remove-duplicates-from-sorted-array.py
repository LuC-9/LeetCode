class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1
        j = 1
        for i in range(0, len(nums)-1): 
            if nums[i] != nums[i+1]: 
                nums[j] = nums[i+1]
                j += 1
        return j