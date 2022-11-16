class Solution:
    def search(self, nums, target):

        low = 0
        high = len(nums)
        while low < high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return True

            if nums[low] == nums[mid] and nums[high-1] == nums[mid]:
                low += 1
                high -= 1
                continue

            if nums[low] <= nums[mid]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid
                else:
                    low = mid+1
            else:
                if target <= nums[high-1] and target > nums[mid]:
                    low = mid+1
                else:
                    high = mid
                    
        return False


if __name__ == "__main__":
    ob1 = Solution()
    nums = [2,5,6,0,0,1,2]
    target = 0
    print(ob1.search(nums, target))