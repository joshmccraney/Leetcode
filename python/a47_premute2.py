class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums):
        self.backtrack(nums, [])
        duplicates = self.res
        singles = []
        for x in duplicates:
            if x not in singles:
                singles.append(x)
        return singles

    def backtrack(self, nums, path):
        if not nums:
            self.res.append(path)
            
        for x in range(len(nums)):
            self.backtrack(nums[:x]+nums[x+1:], path + [nums[x]])

if __name__ == "__main__":
    ob1 = Solution()
    nums = [1,1,3]
    print(ob1.permute(nums))