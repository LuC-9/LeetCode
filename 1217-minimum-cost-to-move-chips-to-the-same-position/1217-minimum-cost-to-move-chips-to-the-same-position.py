class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # """
        # count_even is the number of coins in even pos
        # count_odd is the number of coins in odd pos
        # """
        count_odd = count_even = 0
        for pos in position:
            if(pos%2==0):
                count_even += 1
            else:
                count_odd += 1
        # """
        # Directly Jump to step 4 as cost of step 1- step 3 is 0
        # """
        return min(count_odd,count_even)
        