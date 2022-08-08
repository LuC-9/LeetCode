class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr=[0 for i in nums] 
        start=0 
        end=len(nums)-1 
        for i in range (len(nums)-1,-1,-1):
            smaller=nums[start]
            larger = nums[end]
            if abs(smaller)>=abs(larger):
                arr[i]=smaller**2
                start+=1
            if abs(smaller)<abs(larger):
                arr[i]=larger**2
                end-=1
        return arr