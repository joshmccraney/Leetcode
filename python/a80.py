class Solution:
    def removeDuplicates(self, nums):
        if len(nums) < 3: return len(nums)
        loc = 2
        for i in range(2, len(nums)):
            if nums[loc - 2] != nums[i]:
                nums[loc] = nums[i]
                loc += 1

        for delete_index in range(len(nums) - 1, loc-1, -1):
            del nums[delete_index]
        return loc

if __name__ == "__main__":
    ob1 = Solution()
    nums = [1,1,1,2,2,2,2,3]
    print(ob1.removeDuplicates(nums))