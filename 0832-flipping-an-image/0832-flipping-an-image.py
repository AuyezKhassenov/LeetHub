class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i, row in enumerate(image):
            image[i] = row[::-1]
            for j, num in enumerate(image[i]):
                image[i][j] = 0 if num == 1 else 1
        return image
        
        