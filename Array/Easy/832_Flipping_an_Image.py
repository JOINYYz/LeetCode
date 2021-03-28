class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i,img in enumerate(image):
            image[i] = img[::-1]
            #注意不要写enumerate(img)，要读取最新赋值后的
            for j,num in enumerate(image[i]):
                if num == 1:                    
                    image[i][j] = 0
                elif num == 0:
                    image[i][j] = 1
        return image
