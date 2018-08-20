def twoSum(nums, target):
    answer = []
    for num1 in nums:
        for num2 in nums:
            if num1 + num2 == target:
                answer.append(nums.index(num1))
                nums[nums.index(num1)] = num1 - 1
                answer.append(nums.index(num2))
                return answer

print(twoSum([3,5,3], 6))