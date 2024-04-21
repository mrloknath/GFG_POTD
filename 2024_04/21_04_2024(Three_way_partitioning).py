class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]
        
	def threeWayPartition(self, array, a, b):
	    # code here 
	    left, right = 0, len(array) - 1
        i = 0
        while i <= right:
            if array[i] < a:
                self.swap(array, i, left)
                left += 1
                i += 1
            elif a <= array[i] <= b:
                i += 1
            elif array[i] > b:
                self.swap(array, i, right)
                right -= 1
