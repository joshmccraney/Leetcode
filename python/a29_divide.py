class Solution(object):
    def divide(self, dividend, divisor):

        sign = -1
        if ( dividend < 0 and divisor < 0) or ( dividend > 0 and divisor > 0):
            sign = 1

        dividend = abs(dividend)
        divisor = abs(divisor)
        
        shift = 0
        while dividend > (divisor << shift):
            shift += 1
        if shift > 0: shift -= 1

        dividend -= divisor << shift
        count = 2**shift

        while dividend >= divisor:
            dividend -= divisor
            count += 1
        
        count = count*sign

        if count > 2**31 - 1:
            return 2**31 - 1
        elif count < -2**31:
            return -2**31
        return count

if __name__ == "__main__":
    dividend = 7
    divisor = -3
    ob1 = Solution()
    print(ob1.divide(dividend, divisor))