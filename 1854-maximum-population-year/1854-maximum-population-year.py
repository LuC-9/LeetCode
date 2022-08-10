class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:   
        dates = []
        for birth, death in logs:
            dates.append((birth, 1))
            dates.append((death, -1))
        # har birth pe +1 and hr death pe -1
        dates.sort()
        #sort kr lo
        #ab maximum running sum kahan aa rha nikal lo
        population = max_population = max_year = 0
        for year, change in dates:
            population += change
            if population > max_population: #change tbhi krna h jb jyada ho qki same hone pe chhota wala year return krna h
                max_population = population
                max_year = year
        
        return max_year