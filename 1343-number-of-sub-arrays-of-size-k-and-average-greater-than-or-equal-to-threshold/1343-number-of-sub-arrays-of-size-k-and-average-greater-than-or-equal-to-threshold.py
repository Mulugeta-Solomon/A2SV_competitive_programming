class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        left, right, subarr_count = 0, k, 0
        curr_wind_sum = sum(arr[0:right])

        while right < len(arr):
            curr_avg = curr_wind_sum / k
            if curr_avg >= threshold:
               subarr_count += 1
            
            curr_wind_sum += arr[right] - arr[left]
            right += 1
            left += 1
        
        if curr_wind_sum / k >= threshold:
            subarr_count += 1
            
        return subarr_count
