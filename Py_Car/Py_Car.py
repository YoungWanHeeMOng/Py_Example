
class Car:
	def __init__(self, speed, color):
		print(speed)
		print(color)
		self.speed=speed		
		self.color=color
		print('the __Init__ is called')

ford=Car(200, 'red')
hyundai=Car(250, 'blue')
kia=Car(300,'black')

#ford=Car()
#Hyundai=Car()
#Kia=Car()
