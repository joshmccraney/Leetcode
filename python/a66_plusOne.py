class Solution:
    def plusOne(self, digits):
        newNum = 0
        for i in range(len(digits)):
            newNum = 10*newNum + digits[i]
        newNum += 1
        numStr = list(str(newNum))
        return numStr

if __name__ == "__main__":
    ob1 = Solution()
    digits = [4,3,2,1]
    print(ob1.plusOne(digits))