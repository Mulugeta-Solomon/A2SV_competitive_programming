class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        check = set(arr)

        for i in range(1, max(arr) + k + 1):
            if i not in check:
                k -= 1
            if k == 0:
                return i