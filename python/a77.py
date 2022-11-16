class Solution:
    def combine(self, n, k):
        res = []

        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return

            for i in range(start, n+1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()

        backtrack(1, [])

        return res


if __name__ == "__main__":
    ob1 = Solution()
    n = 4
    k = 2
    print(ob1.combine(n, k))