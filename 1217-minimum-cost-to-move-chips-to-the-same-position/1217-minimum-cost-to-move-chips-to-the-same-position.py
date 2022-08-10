class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        even = 0
        for i in chips:
            if(i%2==0):
                even+=1
        return min(even,len(chips)-even);
        