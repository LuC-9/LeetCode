class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minr = {min(r)for r in matrix}
        maxc = {max(c)for c in zip(*matrix)}
        #print(list( c for c in zip(*matrix))) #oo lala
        return list(minr&maxc)