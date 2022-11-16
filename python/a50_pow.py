class Solution:
    def myPow(self, x, n):

        if n == 0:
            return 1

        elif n < 0:
            return self.myPow(1/x, -n)

        else:
            # MAIN LOOP
            if n % 2 == 0:
                return self.myPow(x, n/2)*self.myPow(x, n/2)
            else:
                return x*self.myPow(x, n-1)

if __name__ == "__main__":
    x = 2.00000
    n = 4
    ob1 = Solution()
    print(ob1.myPow(x,n))