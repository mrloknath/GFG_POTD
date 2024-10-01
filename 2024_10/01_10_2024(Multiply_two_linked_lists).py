class Solution:
    def multiply_two_lists(self, first, second):
        tmp1 = first
        tmp2 = second
        num1 = 0
        num2 = 0
        while tmp1:
            num1 = (num1 * 10 + tmp1.data)% (1000000007)
            tmp1 = tmp1.next
        while tmp2:
            num2 = (num2 * 10 + tmp2.data)% (1000000007)
            tmp2 = tmp2.next
        return (num1*num2) % (1000000007)
