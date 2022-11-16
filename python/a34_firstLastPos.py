class Solution:
    def search(self, nums, target):
        
        # BASE CASE
        if nums is None or len(nums) == 0 or target not in nums:
            return [-1,-1]

        left = 0
        right = len(nums)-1

        # 1ST OCCURENCE
        while left < right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                first = middle
                right = middle - 1
            elif nums[middle] > target:
                right = middle
            else:
                left = middle

        left = 0
        right = len(nums)-1

        # LAST OCCURENCE
        while left < right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                last = middle
                left = middle + 1
            elif nums[middle] > target:
                right = middle
            else:
                left = middle

        return [first, last]

# DRIVER CODE
if __name__ == "__main__":
   nums = [5,7,7,7,7,8,10]
   target = 7
   ob1 = Solution()
   print(ob1.search(nums, target))




