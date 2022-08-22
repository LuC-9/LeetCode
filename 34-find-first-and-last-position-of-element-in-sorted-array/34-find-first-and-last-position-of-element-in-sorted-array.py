class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:  
        #Essentially a modified binary search
		#To find the first occurence of a number, scan the remaining left part
		#To find the last occurence of a number, scan the remaining right part
		
        def binarySearch(find):
            left, right = 0, len(nums) - 1
            output = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    output = mid
                    
					#This is the only modification to a standard binary search
                    if find == 'first': #To find the first occurence, look to the left (shrink from right)
                        right = mid - 1
                    elif find == 'last': #To find the last occurence, look to the right (shrink from left)
                        left = mid + 1
            
            return output
            
        return [binarySearch('first'), binarySearch('last')]
        