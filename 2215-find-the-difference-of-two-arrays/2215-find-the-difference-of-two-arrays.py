class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        answer = [[], []]
        look_up1 = {}
        look_up2 = {}

        for num in nums1:
            look_up1[num] = look_up1.get(num, 0) + 1
        for num in nums2:
            look_up2[num] = look_up2.get(num, 0) + 1
        
        for num in nums1:
            if num not in look_up2:
                answer[0].append(num)
        
        for num in nums2:
            if num not in look_up1:
                answer[1].append(num)
                
        answer1 = list(set(answer[0]))
        answer2 = list(set(answer[1]))
        
        return [answer1, answer2]


        