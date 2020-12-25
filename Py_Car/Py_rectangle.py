
class Rectangle:
	def __init__ (self, height, width):
		self.height=height
		self.width=width
		print("This is Rectangle Area")
		print(height, width, height*width)

rect1=Rectangle(100, 200)
rect2=Rectangle(123, 456)

######################################
class Hello:
	def __init__(self): 
		print('have not data')
	def __init__(self, name) : 
		self.name=name
		print(name)

print ("")		
print (" It's Hello logic")
hello=Hello('Seoul')
