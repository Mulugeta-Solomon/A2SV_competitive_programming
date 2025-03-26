class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        people, result = [0] * 101, 0 # 1950 -> 2050

        for birth, death in logs:
            people[birth - 1950] += 1
            people[death - 1950] -= 1
        
        maxx = people[0]
        for i in range(1, 101):
            people[i] += people[i - 1]
            if people[i] > maxx:
                maxx = people[i]
                result = i
        
        return result + 1950