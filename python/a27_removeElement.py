class Solution(object):
    def removeEl(self, nums, val):
        count = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        nums = nums[:-(len(nums) - count)]
        return nums

if __name__ == "__main__":
    nums = [3,2,2,3,1,2]
    val = 3
    ob1 = Solution()
    print(ob1.removeEl(nums,val))