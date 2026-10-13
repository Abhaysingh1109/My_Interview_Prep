def missing_numbers(nums):
    for i in range(min(nums), max(nums) + 1):
        if i not in nums:
            print(i)

nums = [1, 2, 4, 6, 7, 9]
missing_numbers(nums)