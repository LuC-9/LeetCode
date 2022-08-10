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
        return min(count_odd,count_even)  