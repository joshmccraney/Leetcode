from ast import Num


class Solution:
    def generateMatrix(self, n):
        mat = [[0 for _ in range(n)] for _ in range(n)]

        left = 0
        right = n-1
        top = 0
        bottom = n-1
        num = 1

        while left <= right and top <= bottom:

            # TOP: LEFT TO RIGHT
            for j in range(left, right+1):
                mat[top][j] = num
                num += 1

            # RIGHT: TOP TO BOTTOM
            for j in range(top + 1, bottom):
                mat[j][right] = num
                num += 1

            # BOTTOM: LEFT TO RIGHT
            for j in range(right, left-1, -1):
                if top < bottom:
                    mat[bottom][j] = num
                    num += 1

            # LEFT: BOTTOM TO TOP
            for j in range(bottom-1, top, -1):
                if left < right:
                    print(num)
                    mat[j][left] = num
                    num += 1

            left += 1
            top += 1
            right -= 1
            bottom -= 1

        return mat

if __name__ == "__main__":
    ob1 = Solution()
    n = 3
    print(ob1.generateMatrix(n))