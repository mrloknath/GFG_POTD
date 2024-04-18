class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, arr , n):
        #Your code here
        unique = set()
        result = []
        
        for i in range(n+2):
            if arr[i] in unique:
                result.append(arr[i])
            else:
                unique.add(arr[i])
        
        return result
