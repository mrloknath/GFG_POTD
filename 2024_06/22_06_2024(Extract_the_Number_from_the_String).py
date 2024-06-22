import re

class Solution:
    def ExtractNumber(self,sentence):
        #code here
        res = re.findall(r"\d+", sentence)
        reslt = [i for i in res if '9' not in i]
        if not reslt:
            return -1
        else:
            return max(list(map(int, reslt)))
