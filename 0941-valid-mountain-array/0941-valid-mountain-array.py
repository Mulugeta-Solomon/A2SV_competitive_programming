class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        flag = True

        for i in range(1, len(arr)):
            if flag and arr[i] > arr[i - 1]:
                continue
            if i == 1:
                return False
            if not flag:
                if arr[i] < arr[i - 1]:
                    continue
                else:
                    return False
            if arr[i] < arr[i - 1]:
                flag = False
            else:
                return False
        
        return True if not flag else False
