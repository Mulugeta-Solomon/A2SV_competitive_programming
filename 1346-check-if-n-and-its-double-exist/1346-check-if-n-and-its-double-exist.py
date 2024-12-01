class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        check = set()

        for num in arr:
            if num / 2 in check or num * 2 in check:
                print(num)
                return True
            check.add(num)
        
        return False