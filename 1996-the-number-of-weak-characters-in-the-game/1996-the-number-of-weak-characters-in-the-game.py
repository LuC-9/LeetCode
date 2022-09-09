class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        lookup = collections.defaultdict(list)
        for a, d in properties:
            lookup[a].append(d)
        result = max_d = 0
        for a in sorted(lookup.iterkeys(), reverse=True):
            result += sum(d < max_d for d in lookup[a])
            max_d = max(max_d, max(lookup[a]))
        return result
        