class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    case1 = abs(arr[i] - arr[j]) <= a
                    case2 = abs(arr[j] - arr[k]) <= b
                    case3 = abs(arr[i] - arr[k]) <= c
                    if case1 and case2 and case3:
                        count += 1
        
        return count