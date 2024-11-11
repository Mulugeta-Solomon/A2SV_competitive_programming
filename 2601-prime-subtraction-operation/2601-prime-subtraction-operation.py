class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        
        def prime(n):
            if n <= 2:
                return 0
            prime = [1] * n 
            prime[0] = prime[1] = 0
            i = 2
            while i * i <= n - 1:
                if prime[i] == 1:
                    j = i*i
                    while j < n:
                        prime[j] = 0
                        j += i
                i += 1

            for i in range(n - 1, -1, -1):
                if prime[i]:
                    return i

        
        for i in range(len(nums) - 1):                        
            if i > 0:
                n = nums[i] - nums[i - 1]
            else:
                n = nums[i]
            
            curr = prime(n)
            nums[i] -= curr

            if nums[i] >= nums[i + 1]:
                return False

        return True

        
