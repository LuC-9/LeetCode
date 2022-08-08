class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        def flip(a):
            return a[::-1]
        def invert(a): 
            return a^1     
        for i in range(len(image)):
            image[i]=flip(image[i])
            for j in range(len(image)):
                image[i][j]=invert(image[i][j])  
        return image
        
            
        
                
            
        