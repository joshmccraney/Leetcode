class Solution:
    def grayCode(self, n):
        res = []
        for i in range(1 << n):
            res.append(i ^ (i >> 1))
        return res

if __name__ == "__main__":
    ob1 = Solution()
    n = 2
    print(ob1.grayCode(n))