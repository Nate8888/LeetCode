def numJewelsInStones(J,S):
	amt = 0
	for x in J:
		amt += S.count(x)
	return amt

print(numJewelsInStones('aA','aaaAbb'))