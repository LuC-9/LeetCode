class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:   
        birth_years = sorted([i[0] for i in logs])
        max_pop = 0
        output = 0
        for year in birth_years:
            population= 0
            for dates in logs:
                if dates[0]<=year and dates[1]>year:
                    population+=1
            if population>max_pop:
                output = year
                max_pop = population
        return output