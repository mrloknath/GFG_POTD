class Solution:
    def search(self,arr,key):
        # Complete this function
        if key in arr:
            return arr.index(key)
        return -1
