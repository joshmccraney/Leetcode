class Solution:
    def search(self, nums, target):
        
        # Special case
        if nums is None or len(nums) == 0:
            return -1

        # Left and right pointers for the array
        left, right = 0, len(nums) - 1

        # FIND PIVOT
        while left < right:
            # Middle index
            middle = left + (right - left) // 2
            # If the element at the mid is greater than
            # the element at the right then we can say that
            # the array is rotated after middle index
            if nums[middle] > nums[right]:
                left = middle + 1
            # Else, the pivot is in the left part
            else:
                right = middle

        # LOCATE SECTION TARGET IS IN
        pivot = left
        left, right = 0, len(nums) - 1
        # Now we will find in which half of the array,
        # our targetValue is present
        if nums[pivot] <= target <= nums[right]:
            left = pivot
        else:
            right = pivot

        # BINARY SEARCH SECTION FOR TARGET
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1

# DRIVER CODE
if __name__ == "__main__":
   nums = [3,4,5,6,7,0,1,2]
   target = 0
   ob1 = Solution()
   print(ob1.search(nums, target))




