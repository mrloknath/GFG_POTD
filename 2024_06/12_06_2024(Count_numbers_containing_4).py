class Solution:
    def countNumberswith4(self, n : int) -> int:
        # code here
        c = 0
        for i in range(4, n + 1):
            a = i
            while a > 0:
                if a % 10 == 4:
                    c += 1
                    break
                a //= 10
        return c
