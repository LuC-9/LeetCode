class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1
        
            
            
    
            
            
        