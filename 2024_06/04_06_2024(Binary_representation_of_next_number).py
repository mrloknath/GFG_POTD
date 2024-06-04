class Solution:
	def binaryNextNumber(self, s):
		# code here
		number = int(s, 2)
		next_number = number+1
		return bin(next_number)[2:]
