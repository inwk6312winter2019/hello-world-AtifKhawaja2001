def sum_all(*args):
	sum = 0
	for i in args:
		sum = sum + i
	return sum

print(sum_all(2,4,5,6,7))

