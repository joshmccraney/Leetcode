class Solution(object):
    def strstr(self, haystack, needle):
        n = len(haystack)
        m = len(needle)
        count = 0

        for i in range(n - m):
            if haystack[i:i+m] == needle:
                count += m
                i += m

        if count == 0:
            count = -1

        return count

if __name__ == "__main__":
    haystack = "hellollll"
    needle = "ll"
    ob1 = Solution()
    print(ob1.strstr(haystack, needle))