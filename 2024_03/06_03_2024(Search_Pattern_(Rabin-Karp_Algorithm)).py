class Solution:
    def search(self, pattern, text):
        n = len(text)
        m = len(pattern)
        ans = []
        
        for i in range(n - m + 1):
            if pattern[0] == text[i] and pattern[m - 1] == text[i + m - 1]:
                if pattern == text[i:i + m]:
                    ans.append(i + 1)
        
        return ans
