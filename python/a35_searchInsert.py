class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 2
    ob1 = Solution()
    print(ob1.searchInsert(nums, target))