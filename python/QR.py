import numpy as np
import time

class Solution:
    def QR(self, n, A):
        e = A[:, [0]] / np.linalg.norm(A[:, [0]])

        for j in range(1, n):
            u1 = A[:, [j]]
            for i in range(e.shape[1]):
                u1 -= np.dot( np.transpose( A[:, [j]] ), e[:, [i]] ) * e[:, [i]]
            uMag = np.linalg.norm( u1 )
            u = u1 / uMag
            e = np.append(e, u, axis = 1)
        print(e)
        return e

    def pyQR(self, A):
        q, r = np.linalg.qr(A)
        print(q)
        return q

if __name__ == "__main__":
    ob1 = Solution()
    n = 3
    A = np.random.random((n, n))

    start = time.time()
    jQ = ob1.QR(n, A)
    end = time.time()
    print ("Time elapsed:", end - start)

    start = time.time()
    pQ = ob1.pyQR(A)
    end = time.time()
    print ("Time elapsed:", end - start)


