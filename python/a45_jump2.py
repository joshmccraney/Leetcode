class Solution:
    def jump(self, nums):
        L = 0
        R = 0
        res = 0
        while R < len(nums) - 1:
            far = 0
            for i in range(L, R+1):
                far = max( far, i + nums[i] )
            L = R + 1
            R = far
            res += 1
        return res
        
if __name__ == "__main__":
    ob1 = Solution()
    nums = [2,3,1,1,4]
    print(ob1.jump(nums))