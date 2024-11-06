class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        buckets, curr = [], [] # using a bucket sort
        currSetbit = None

        for num in nums:
            if not currSetbit:
                currSetbit = bin(num).count('1')
                curr.append(num)
                continue
            if currSetbit == bin(num).count('1'):
                curr.append(num)
            else:
                currSetbit = bin(num).count('1')
                buckets.append(curr)
                curr = [num]
    
        if curr:
            buckets.append(curr)
            
        ordered = []
        for curr in buckets:
            ordered += sorted(curr)

        return ordered == sorted(nums)