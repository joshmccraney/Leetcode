import itertools
class Solution:
    def searchMatrix(self, matrix, target):

        merged = list(itertools.chain(*matrix))

        low = 0
        high = len(merged) - 1

        while low <= high:
            middle = low + (high - low) // 2
            if merged[middle] == target:
                return True
            elif merged[middle] < target:
                low = middle + 1
            else:
                high = middle - 1
        return False


if __name__ == "__main__":
    ob1 = Solution()
    matrix = [[1]]
    target = 5
    print(ob1.searchMatrix(matrix, target))