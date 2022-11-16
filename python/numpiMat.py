import numpy as np
import matplotlib.pyplot as plt

class Solution:
    def LSF(self, n):

        # DEFINE DATA
        x = np.random.rand(n)
        y = np.random.rand(n)

        # DEFINE LLS MATRICES
        o = np.ones(n)
        A = np.column_stack((x, o))
        
        # COMPUTE MINIMIZATION
        c1 = np.linalg.inv(np.matmul(np.transpose(A),A))
        c2 = np.matmul(np.transpose(A),y)
        c = np.matmul(c1, c2)
        
        # COMPUTE BEST CURVE
        yc = np.matmul(A, c)

        # PLOT RESULTS
        plt.plot(x, y, 'o')
        plt.plot(x, yc)
        plt.show()

if __name__ == "__main__":
    ob1 = Solution()
    n = 5
    ob1.LSF(n)