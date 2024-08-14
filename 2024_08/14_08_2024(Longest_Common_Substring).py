class Solution:
    def longestCommonSubstr(self,str1, str2):
        m = len(str1)
        n = len(str2)
        LCSuff = [[0 for _ in range(n+1)] for _ in range(m+1)]
        result = 0  
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
                    result = max(result, LCSuff[i][j])
                else:
                    LCSuff[i][j] = 0
                    
        return result
