class Solution:
    def minimumSteps(self, s: str) -> int:

        left, right, count = 0, 1, 0
        balls = [int(s[i]) for i in range(len(s))]

        while right <= len(balls) - 1:

            if balls[right] == 0 and balls[left] == 1:
                balls[left], balls[right] = balls[right], balls[left]
                count += 1

            left += 1
            right += 1
        
        return count

        