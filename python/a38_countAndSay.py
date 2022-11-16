class Solution:
    def countAndSay(self, n):
        s = '1'

        # SWEEP THROUGH CASE n
        for _ in range(n-1):
            prev = s[0]
            temp = ''
            count = 0

            # SWEEP THROUGH s
            for curr in s:
                if curr == prev:
                    count += 1
                else:
                    temp += str(count)+prev
                    prev = curr
                    count = 1
            temp += str(count)+prev
            s = temp
        return s

if __name__ == "__main__":
    ob1 = Solution()
    n = 4
    print('solution is ' + ob1.countAndSay(n))