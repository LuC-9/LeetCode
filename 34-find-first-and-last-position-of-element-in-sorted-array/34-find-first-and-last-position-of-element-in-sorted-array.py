class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:    
        def left(nums,k):
            s=0
            ans=-1
            e=len(nums)-1
            while s<=e:
                m=s+(e-s)//2
                if nums[m]==k:
                    ans=m
                    e=m-1
                elif nums[m]>k:
                    e=m-1
                else:
                    s=m+1
            return ans
        def right(nums,k):
            s=0
            ans=-1
            e=len(nums)-1
            while s<=e:
                m=s+(e-s)//2
                if nums[m]==k:
                    ans=m
                    s=m+1
                elif nums[m]>k:
                    e=m-1
                else:
                    s=m+1
            return ans
        r=[0]*2
        r[0]=left(nums,target)
        r[1]=right(nums,target)
        return r