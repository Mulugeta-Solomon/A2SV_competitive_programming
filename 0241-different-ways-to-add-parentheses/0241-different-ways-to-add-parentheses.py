class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        operations = { '+': lambda x, y: x + y, 
                       '-': lambda x, y: x - y,
                       '*': lambda x, y: x * y}
        
        def backtrack(left, right):
            result = []

            for i in range(left, right + 1):
                if expression[i] in operations:
                    nums1 = backtrack(left, i - 1)
                    nums2 = backtrack(i + 1, right)

                    for x in nums1:
                        for y in nums2:
                            result.append(operations[expression[i]](x, y))
            if result == []:
                result.append(int(expression[left:right + 1]))
            
            return result
        
        return backtrack(0, len(expression) - 1)
        