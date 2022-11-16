class Solution(object):
   def rev(self, nums):
      isNegative = nums < 0
      nums = abs(nums)
      rem = 0

      while nums > 0:
         rem = rem*10 + (nums % 10)
         nums //= 10
      if isNegative:
         return -rem
      return rem


# DRIVER CODE
if __name__ == "__main__":
   nums = -284
   ob1 = Solution()
   print(ob1.rev(nums))