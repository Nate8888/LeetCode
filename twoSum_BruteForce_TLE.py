def twoSum(nums,target):
	for x in range(len(nums)):
		for y in range(len(nums)):
			if x != y and nums[x]+nums[y] == target:
				return [x,y]

print(twoSum([1,2,3],4))