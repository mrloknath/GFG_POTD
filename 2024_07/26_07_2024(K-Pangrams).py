from collections import Counter
class Solution:
    def kPangram(self,string, k):
        string = string.replace(' ', '')
        mp = Counter(string)
        cnt, total = len(mp.keys()), sum(mp.values())
        return k + cnt >= 26 and total >= 26
