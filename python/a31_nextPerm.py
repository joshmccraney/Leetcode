class Solution(object):
    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


    def nextPermutation(self, nums):
        # Length of the array
        n = len(nums)

        # Index of the first element that is smaller than
        # the element to its right.
        index = -1

        # Loop from right to left
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                index = i - 1
                break

        # Base condition
        if index == -1:
            return self.reverse(nums, 0, n - 1)

        j = n - 1
        # Scan right to left to find first element
        # greater than the above find element
        for i in range(n - 1, index, -1):
            if nums[i] > nums[index]:
                j = i
                break

        # Swap the elements
        nums[index], nums[j] = nums[j], nums[index]

        # Reverse the elements from index + 1 to the nums.length
        newNum = self.reverse(nums, index + 1, n - 1)
        return newNum

if __name__ == "__main__":
    nums = [1,3,2]
    ob1 = Solution()
    print(ob1.nextPermutation(nums))