class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minrow = {min(r) for r in matrix}
        maxcol = {max(c) for c in zip(*matrix)}
        print(list( c for c in zip(*matrix))) #oo lala
        return list(minrow & maxcol)