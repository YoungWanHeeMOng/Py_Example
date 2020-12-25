
def num_func(x):
	return x**2/2

data = [1,2,3,4,5,6,7,8,9]
d=list(map(num_func, data))

print (data)
print ("Calculate data to x**2/2 : " ,d)