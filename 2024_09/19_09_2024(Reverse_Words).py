class Solution:
    def reverseWords(self, str):
        return '.'.join(str.split('.')[::-1])
