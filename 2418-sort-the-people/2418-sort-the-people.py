class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hei_name = dict(zip(heights, names))
        max_ele = max(heights)

        count = [0] * (max_ele + 1)

        for height in heights:
            count[height] += 1

        idx = 0
        for i in range(len(count) - 1, -1, -1):
            for _ in range(count[i]):
                heights[idx] = i
                idx += 1

        return [hei_name[height] for height in heights]