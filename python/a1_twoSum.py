def twoSum(nums, target):
    val_to_index = {}
    for i in range(len(nums)):
        if target - nums[i] in val_to_index:
            return val_to_index[target - nums[i]], i
        val_to_index[nums[i]] = i
    return [-1, -1]

# DRIVER CODE
if __name__ == "__main__":
    nums = [3, 2, -4, 8, 11]
    target = 7
    print(twoSum(nums,target))