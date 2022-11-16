import numpy as np

class Solution:
    def stick(self, n):
        mid = 0
        for i in range(n):
            c1 = np.random.rand()
            c2 = np.random.rand()

            mid += abs(c2 - c1)

        return mid/n


if __name__ == "__main__":
    ob1 = Solution()
    n = 100000
    print(ob1.stick(n))