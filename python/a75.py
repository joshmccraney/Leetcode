class Solution:
    def sortColors(self, nums):
        left = cur = 0
        right = len(nums) - 1
        
        while cur <= right:
            if nums[cur] == 0:
                nums[left], nums[cur] = nums[cur], nums[left]
                left += 1
                cur += 1
            elif nums[cur] == 2:
                nums[right], nums[cur] = nums[cur], nums[right]
                right -= 1
            else: cur += 1

if __name__ == "__main__":
    ob1 = Solution()
    nums = [2,0,2,1,1,0]
    print(ob1.sortColors(nums))