def twoSum(nums,target):
	myDict = {}
	c = 0
	for x in nums:
		myDict[x] = c
		c+= 1
	for i in range(len(nums)):
		if (target-nums[i]) in myDict.keys() and myDict[target-nums[i]] != i:
			return [i,myDict[target-nums[i]]]

print(twoSum([2,7,11,15],9))