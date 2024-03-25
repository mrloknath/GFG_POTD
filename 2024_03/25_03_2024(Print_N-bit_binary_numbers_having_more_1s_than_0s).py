class Solution:
	def NBitBinary(self, n):
		# code here
        result = []
        self.generate_valid_binaries(n, "", 0, 0, result)
        return result
    
    def generate_valid_binaries(self, n, prefix, ones, zeros, result):
        if len(prefix) == n:
            result.append(prefix)
            return
        
        if ones > zeros:
            self.generate_valid_binaries(n, prefix + "1", ones + 1, zeros, result)
            self.generate_valid_binaries(n, prefix + "0", ones, zeros + 1, result)
        else:
            self.generate_valid_binaries(n, prefix + "1", ones + 1, zeros, result)
