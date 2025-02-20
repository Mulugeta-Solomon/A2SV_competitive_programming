class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        lookup, n = set(nums), len(nums[0])

        def backtrack(curr):
            if len(curr) == n:
                if ''.join(curr) not in lookup:
                    return True
                return False

            for i in range(2):
                curr.append(str(i))
                if backtrack(curr):
                    return ''.join(curr)
                curr.pop()

        return backtrack([])