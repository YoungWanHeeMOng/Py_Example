


class cal:

	def setdata(self, f, s):
		self.f=f
		self.s=s

	def add(self):
		result=self.f + self.s	
		return result

	def sub(self):
		result=self.f - self.s
		return result
	def mul(self):
		result=self.f * self.s	
		return result
		
	def div(self):
		result=self.f / self.s
		return result

a=cal()

a.setdata(23,12)
print (a.add())
print (a.sub())
print (a.mul())
print (a.div())

class cal1:
	def __init__(self, f, s):
			self.f=f
			self.s=s
	def setdata(self, f, s):
		self.f=f
		self.s=s

	def add(self):
		result=self.f + self.s	
		return result

	def sub(self):
		result=self.f - self.s
		return result
	def mul(self):
		result=self.f * self.s	
		return result
		
	def div(self):
		result=self.f / self.s
		return result

PI = 3.141592

class Math: 
    def solv(self, r): 
        return PI * (r ** 2) 


b=cal1(33,11)

print (b.add())
print (b.sub())
print (b.mul())
print (b.div())

b=cal1(100,40)

# class 상속 기능
class ModeCal(cal1):
	def pow(self):
		result=self.f ** self.s	
		return result

c=ModeCal(4,3)
print("pow 상속 :",c.pow())

class SafeCal(cal1):
	def div(self):
		if self.s == 0 : return 0
		else: return self.f / self.s

d= SafeCal(5,0)
print("div: it's override",d.div())