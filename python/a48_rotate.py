class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        zeroArray = [0] * n
        newmat = [zeroArray[:] for i in range(n)]

        for o in range(n):
            for i in range(n):
                newmat[o][n-i-1] = matrix[i][o]
        return newmat

if __name__ == "__main__":
    ob1 = Solution()
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    print(ob1.rotate(matrix))