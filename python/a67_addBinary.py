class Solution:
    def addBinary(self, a, b):
        if len(a) > len(b):
            b = b.zfill(len(a))
        else:
            a = a.zfill(len(b))

        res = ""
        count = 0
        for i in range(len(a)-1, -1, -1):
            s = int(a[i]) + int(b[i]) + count

            if s == 0:
                res = "0" + res
                count = 0

            elif s == 1:
                res = "1" + res
                count = 0

            elif s == 2:
                res = "0" + res
                count = 1

            elif s == 3:
                res = "1" + res
                count = 1

        if count == 1:
            res = "1" + res

        return res

if __name__ == "__main__":
    ob1 = Solution()
    a = "11"
    b = "11"
    print(ob1.addBinary(a,b))