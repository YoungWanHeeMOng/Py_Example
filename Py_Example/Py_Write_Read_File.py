
f=open("d:/NewPy.txt",'w')
f.write("I'm test write file\n")
f.writelines("I'm test write file , It's second lines")
f.close()

f=open("d:/NewPy01.txt",'w')
for i in range(10):
	data="%d 번째 줄입니다. \n" % i
	f.write(data)
	print(data)
f.close()

# reading file
r=open("d:/NewPy01.txt",'r')
print("reading file from this\n")
while True:
	line=r.readline()
	if not line : break
	print(line)
r.close()

r=open("d:/NewPy01.txt",'r')
print("reading file from this, come in second\n")
while True:
	line=r.readlines()
	if not line : break
	print(line)
	
	print("seperate lines")
	for li in line:
		print(li)
r.close()

r=open("d:/NewPy01.txt",'r')
print("reading file from this, It's only read function\n")
while True:
	line=r.read()
	if not line : break
	print(line)
r.close()


print("write file from this, It's only append function\n")

f=open("d:/NewPy01.txt",'a')
for i in range(10,20):
	data="%d 번째 줄입니다. \n" % i
	f.write(data)
	print(data)
with open("d:/foo.txt", "w") as f:
    f.write("Life is too short, you need python")
f.close()