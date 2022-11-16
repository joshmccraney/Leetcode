class Solution:
    def setZeroes(self, matrix):
        # Empty matrix
        if len(matrix) == 0 or len(matrix[0]) == 0: return

        row = [False] * len(matrix)
        column = [False] * len(matrix[0])

        # Record the rows and columns with element(s) being zero.
        for rowIndex in range(len(matrix)):
            for colIndex in range(len(matrix[0])):
                if matrix[rowIndex][colIndex] == 0:
                    row[rowIndex] = True
                    column[colIndex] = True

        # Set the qualified entire row(s) and column(s) to zero.
        for rowIndex in range(len(matrix)):
            for colIndex in range(len(matrix[0])):
                if row[rowIndex] == True or column[colIndex] == True:
                    matrix[rowIndex][colIndex] = 0

        return matrix

if __name__ == "__main__":
    ob1 = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print(ob1.setZeroes(matrix))