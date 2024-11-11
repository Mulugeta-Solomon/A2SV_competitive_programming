class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        
        def sieve(n):
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
            
            return prime

        prime = sieve(1001)

        for i in range(len(nums) - 1):                        
            if i > 0:
                n = nums[i] - nums[i - 1]
            else:
                n = nums[i]
            curr = 0
            for p, val in enumerate(prime[:n]):
                if val:
                    curr = p

            nums[i] -= curr

            if nums[i] >= nums[i + 1]:
                return False

        return True

        
