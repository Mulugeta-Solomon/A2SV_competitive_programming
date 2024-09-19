class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        operations = {'+', '-', '*'}
        
        def backtrack(left, right):
            result = []

            for i in range(left, right + 1):
                if expression[i] in operations:
                    nums1 = backtrack(left, i - 1)
                    nums2 = backtrack(i + 1, right)

                    for x in nums1:
                        for y in nums2:
                            if expression[i] == '+':
                                result.append(x + y)
                            if expression[i] == '-':
                                result.append(x - y)
                            if expression[i] == '*':
                                result.append(x * y)
                            
            if result == []:
                result.append(int(expression[left:right + 1]))
            
            return result
        
        return backtrack(0, len(expression) - 1)
        