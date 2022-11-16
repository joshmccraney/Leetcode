class Solution:
    def spiralOrder(self, matrix):
        res = []
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix[0])

        while left < right and top < bottom:

            # SCAN LEFT TO RIGHT
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # SCAN TOP TO BOTTOM
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # SCAN RIGHT TO LEFT
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # SCAN BOTTOM TO TOP
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    ob1 = Solution()
    print(ob1.spiralOrder(matrix))