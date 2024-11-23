class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        row, col = len(box), len(box[0])
        result = [[0] * row for _ in range(col)]
        
        def helper(curr):
            result = [0] * len(curr)
            prefix, walls, total = [0] * (len(curr) + 1), [0] * (len(curr) + 1), 0
            last = -1

            for i in range(len(curr)):
                if curr[i] == '#':
                    total += 1
                    if prefix[i] != -1:
                        prefix[i + 1] = 1 + prefix[i]
                    else:
                        prefix[i + 1] = 1
                elif curr[i] == '.':
                    if prefix[i] != -1:
                        prefix[i + 1] = prefix[i]
                    else:
                        prefix[i + 1] = 0
                else:
                    prefix[i + 1] = -1
                    walls[i + 1] = prefix[i]
                    last = i + 1

            for i in range(len(curr) - 1, -1, -1):
                if prefix[i + 1] != -1 and prefix[i + 1] != 0 and total > 0:
                    if last != -1 and walls[last] > 0:
                        result[i] = '#'
                        total -= 1
                        walls[last] -= 1
                    else:
                        if last == -1:
                            result[i] = '#'
                            total -= 1
                        else:
                            result[i] = '.'

                elif prefix[i + 1] == -1:
                    last = i + 1
                    result[i] = '*'
                
                else:
                    result[i] = '.'
                    
            return result

        for i in range(row):
            box[i] = helper(box[i])
        
        for i in range(col):
            for j in range(row):
                result[i][j] = box[row - 1 - j][i]


        return result