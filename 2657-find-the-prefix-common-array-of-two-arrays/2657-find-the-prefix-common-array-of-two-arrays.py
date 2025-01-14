class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        look_upA, look_upB = set(), set()
        result = [0] * (len(A) + 1)

        for i in range(len(A)):
            curr = 0
            if A[i] == B[i]:
                result[i + 1] = result[i] + 1
                look_upA.add(A[i])
                look_upB.add(B[i])
                continue
            if A[i] in look_upB:
                curr += 1
            if B[i] in look_upA:
                curr += 1
            result[i + 1] = result[i] + curr
            look_upA.add(A[i])
            look_upB.add(B[i])

        return result[1:] 