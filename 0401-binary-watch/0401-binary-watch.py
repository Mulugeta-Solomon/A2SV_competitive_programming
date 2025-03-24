class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for h in range(12):
            for m in range(60):
                hour = bin(h).count('1')
                minute = bin(m).count('1')
                if hour + minute == turnedOn:
                    if len(str(m)) < 2:
                        m = '0' + str(m)
                    result.append(f'{h}:{m}')
        
        return result