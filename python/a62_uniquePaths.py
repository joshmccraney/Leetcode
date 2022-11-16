class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         def fact(self, n):
#             f = 1
#             for i in range(1, n+1):
#                 f *= i
#             return f
#         return int(fact(self, m-1+n-1)/(fact(self, m-1)*fact(self, n-1)))

# if __name__ == "__main__":
#     ob1 = Solution()
#     m = 3
#     n = 7
#     print(ob1.uniquePaths(n, m))

    def numberOfPaths(self, m, n):
        if(m == 1 or n == 1):
            return 1

        # LAST SUM IS DIAGONAL MOVEMENTS
        return self.numberOfPaths(m-1, n) + self.numberOfPaths(m, n-1) + self.numberOfPaths(m-1, n-1)

if __name__ == "__main__":
    ob1 = Solution()
    m = 2
    n = 3
    print(ob1.numberOfPaths(m, n))