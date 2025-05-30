class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            image[i] = image[i][::-1]

        for i in range(n):
            for j in range(n):
                image[i][j] = 1 if image[i][j] == 0 else 0
        
        return image