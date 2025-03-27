class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        working = [0] * 1002
        for i in range(len(startTime)):
            working[startTime[i]] += 1
            working[endTime[i] + 1] -= 1
        
        for i in range(1, len(working)):
            working[i] = working[i] + working[i - 1]
        

        return working[queryTime]
        