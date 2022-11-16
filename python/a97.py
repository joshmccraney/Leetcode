class Solution:
    def isInterleave(self, s1, s2, s3):

        dp = {}

        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in dp:
                return dp[(i, j)]

            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True
            dp[(i, j)] == False
            return False

        return dfs(0, 0)


        

if __name__ == "__main__":
    ob1 = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(ob1.isInterleave(s1, s2, s3))