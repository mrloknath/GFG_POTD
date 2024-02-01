class Solution:
    def checkPangram(self, s):
        present = [False] * 26
        for x in s:
            if x.isalpha():
                if x.islower():
                    index = ord(x) - ord('a')
                    present[index] = True
                else:
                    index = ord(x) - ord('A')
                    present[index] = True
        for x in present:
            if not x:
                return False
        return True
