class Solution:
    def maxSubArray(self, nums):

        sum = nums[0]
        curSum = 0
 
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            sum = max(sum,curSum)
                
        return sum

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    ob1 = Solution()
    print(ob1.maxSubArray(nums))