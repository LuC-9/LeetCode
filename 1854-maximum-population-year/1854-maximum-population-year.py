class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:   
        d = defaultdict(int)
        res = [2051, 0]
        for YOB, YOD in logs:
            for year in range(YOB, YOD):
                d[year] += 1
                if d[year] >= res[1]:
                    if d[year] > res[1]:
                        res = [year, d[year]]
                    else:
                        res = [min(year, res[0]), res[1]]
        #print(d)
        #print(res)
        return res[0]