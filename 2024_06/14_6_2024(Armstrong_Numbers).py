class Solution:
    def armstrongNumber(self, n: int) -> str:
        n1 = n
        digits = len(str(n))
        ans = sum(int(digit) ** digits for digit in str(n))
        if ans == n1:
            return "Yes"
        return "No"
