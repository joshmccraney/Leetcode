class Solution(object):
   def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        rtype: int
        """
        if len(nums) == 0:
            return 0

        previous = nums[0]
        index = 1

        for i in range(1,len(nums)):
            if nums[i] != previous:
                previous = nums[i]      # previous IS CURRENT NUMBER
                nums[index] = nums[i]   # overwrite the nums array
                index +=1
        nums = nums[:-(len(nums) - index)]
        return index, nums

if __name__ == "__main__":
    input_list = [1,1,1,2,2,3]
    ob1 = Solution()
    print(ob1.removeDuplicates(input_list))