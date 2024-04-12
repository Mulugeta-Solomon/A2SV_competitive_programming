class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        longest_mountain = 0

        for i in range(len(arr)):

            if i+1 < len(arr) and arr[i+1] > arr[i]:
                left, right = 0, 0

                while i+1 < len(arr) and arr[i+1] > arr[i]:
                    left += 1
                    i += 1
                while i+1 < len(arr) and arr[i+1] < arr[i]:
                    right += 1
                    i += 1
                
                if right != 0:
                    longest_mountain = max(longest_mountain, right + left + 1)
                    i -= 1
        return longest_mountain

