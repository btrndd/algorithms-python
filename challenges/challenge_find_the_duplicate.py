def find_duplicate(nums):
    if (nums is None or len(nums) < 2):
        return False
    nums.sort()
    for index, num in enumerate(nums[1:], start=1):
        if (type(num) is not int or num < 0):
            return False
        if (nums[index - 1] == nums[index]):
            return num

    return False
