class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums):
        self.backtrack(nums, [])
        return self.res

    def backtrack(self, nums, path):
        if not nums:
            self.res.append(path)
            
        for x in range(len(nums)):
            self.backtrack(nums[:x]+nums[x+1:], path + [nums[x]])
        
if __name__ == "__main__":
    ob1 = Solution()
    nums = [1,2,3]
    print(ob1.permute(nums))