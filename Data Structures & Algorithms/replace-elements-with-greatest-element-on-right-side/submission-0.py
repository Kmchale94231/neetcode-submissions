class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr) - 1 
        
        
        for i in range(len(arr)):
            if i == n:
                arr[i] = -1
                break
            
            arr[i] = max(arr[i+1:])
            
        
        return arr



        