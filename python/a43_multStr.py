class Solution:
    def str2int(self, str):
        num = 0
        for s in str:
            num = num*10 + ord(s) - ord('0')
        return num

    def mult(self, num1, num2):
        ans = self.str2int(num1)*self.str2int(num2)
        return str(ans)
        
if __name__ == "__main__":
    ob1 = Solution()
    num1 = "123"
    num2 = "456"
    print(ob1.mult(num1, num2))