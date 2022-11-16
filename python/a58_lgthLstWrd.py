class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()
        lstWrd = len(s.split()[-1]) if s else 0
        return lstWrd

if __name__ == "__main__":
    ob1 = Solution()
    s = "Hello World"
    print(ob1.lengthOfLastWord(s))