class Solution:
    def firstMissingPositive(self, nums):
        nums.sort()
        res = 1
        for num in nums:
            if num == res:
                res += 1
        return res

if __name__ == "__main__":
    ob1 = Solution()
    nums = [1,2,5,0,-3]
    print(ob1.firstMissingPositive(nums))