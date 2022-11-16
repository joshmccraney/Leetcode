class Solution:
    def mySqrt(self, x):
        left, right = 0,  x
        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
            else:
                return mid

        # left > right
        return right

if __name__ == "__main__":
    ob1 = Solution()
    x = 11
    print(ob1.mySqrt(x))