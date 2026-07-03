def majorityelement(nums):
    nums.sort()
    majorityelement = nums[0]
    count = 0
    for i in range(len(nums)):
        if nums[i] == majorityelement:
            count += 1
        else:
            majorityelement = nums[i]
            count = 1
        if count > len(nums) // 2:
            return majorityelement
        
nums = [3, 2, 3, 2, 2, 1, 1,2, 2, 2]
print(majorityelement(nums))