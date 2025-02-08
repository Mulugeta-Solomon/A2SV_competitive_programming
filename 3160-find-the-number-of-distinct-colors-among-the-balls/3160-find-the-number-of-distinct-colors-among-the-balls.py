class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_map, ball_map = {}, {}
        result = [0] * len(queries)

        for i, (ball, color) in enumerate(queries):
            if ball in ball_map:
                prev = ball_map[ball]
                color_map[prev] -= 1

                if not color_map[prev]:
                    del color_map[prev]

            ball_map[ball] = color
            color_map[color] = color_map.get(color, 0) + 1
            result[i] = len(color_map)

        return result

