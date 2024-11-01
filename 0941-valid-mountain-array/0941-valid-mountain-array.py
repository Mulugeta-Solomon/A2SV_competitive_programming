class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak_found = False

        if len(arr) < 3:
            return False

        for i in range(len(arr) - 1):
            if not peak_found and arr[i + 1] > arr[i]:
                continue
            if peak_found:
                if arr[i+1] < arr[i]:
                    continue
                else:
                    return False
            
            if i > 0 and arr[i + 1] < arr[i]:
                peak_found = True
            else:
                return False
        
        return peak_found
