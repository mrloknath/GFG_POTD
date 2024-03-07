class Solution:
    def longestSubstring(self, S, N):
        max_length = 0
        ans = "-1"
        i = 0

        while i < N:
            j = i + max_length + 1
            while j <= N:
                sub_string = S[i:j]
                if S.find(sub_string, j) != -1:
                    length = len(sub_string)
                    if length > max_length:
                        ans = sub_string
                        max_length = length
                else:
                    break
                j += 1
            i += 1

        return ans
