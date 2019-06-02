def avg(L):
	if not L:
		return none
	return sum(L)/len(L)

# to run a test on pytest you need to create a function like this
def test_avg():
	assert 3.0 == avg([1,2,3,4,5])
	assert 4.0 == avg([4,4,4,4])