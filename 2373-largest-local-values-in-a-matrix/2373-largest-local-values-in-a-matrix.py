class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        list1=[] 
        for i in range(len(grid)-2):
            list2=[] 
            for j in range(len(grid)-2):
                list2.append(max(max(grid[i][j:j+3]),max(grid[i+1][j:j+3]),max(grid[i+2][j:j+3])))
            list1.append(list2)     
        return list1 
        