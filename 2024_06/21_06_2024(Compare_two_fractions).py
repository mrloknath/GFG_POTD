class Solution:
    def compareFrac (self, str):
        # code here
        lst = str.split(', ')

        numerator1, denominator1 = lst[0].split('/')
        numerator2, denominator2 = lst[1].split('/')
        
        if int(numerator1) * int(denominator2) > int(numerator2) * int(denominator1):
            return lst[0]
        elif int(numerator1) * int(denominator2) < int(numerator2) * int(denominator1):
            return lst[1]
        else:
            return "equal"
