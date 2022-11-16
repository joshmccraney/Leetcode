class Solution:
    def climbStairs(self, n):
        if n == 1: return 1
        ways = [1, 2]
        for i in range(2,n):
            temp = ways[1] + ways[0]
            ways[0] = ways[1]
            ways[1] = temp
        return ways[1]

if __name__ == "__main__":
    ob1 = Solution()
    n = 5
    print(ob1.climbStairs(n))