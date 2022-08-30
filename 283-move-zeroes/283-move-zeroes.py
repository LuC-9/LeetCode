class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[index], nums[i] = nums[i], nums[index]
                i += 1
        