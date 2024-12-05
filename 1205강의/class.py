# class Car(object): #앞 부분을 대문자로 사용합니다.
# 	MaxSpeed = 300
# 	MaxPeople = 5
# 	def move(self, x):
# 		print(x, '의 스피드로 움직이고 있습니다.')
# 	def stop(self):
# 		print('멈췄습니다.')

# k5 = Car()
# k3 = Car()
# k5.move(10)
# k5.stop()
# k3.move(5)
# k3.stop()

# print(k5.MaxSpeed)
# print(k3.MaxSpeed)

# #########################????
# class Car(object):
# 	kinds = []
# 	speed = 300
# 	def add_kinds(self, name):
# 		self.kinds.append(name)
# 	def change_speed(self, speed):
# 		self.speed = speed

# k5 = Car()
# k3 = Car()
# k5.add_kinds('k5')
# k3.add_kinds('k3')
# k5.change_speed(500)
# k3.change_speed(250)

# print('k5.kinds:', k5.kinds)
# print('k3.kinds:', k3.kinds)
# print('k5.speed:', k5.speed)
# print('k3.speed:', k3.speed)

# #############################
# class Car(object):
# 	MaxSpeed = 300 # 공유하는 영역
# 	MaxPeoeple = 5 # 공유하는 영역

# 	def __init__(self, 이름): #self는 자신만의 영역
# 		self.name = 이름

# 	def move(self, x):
# 		print(self.name, x, '의 스피드로 움직이고 있습니다.')

# 	def stop(self):
# 		print('멈췄습니다.')

# k5 = Car('케이파이브')
# k3 = Car('케이쓰리')

# k5.move(100)
# k3.move(200)

# ###################################
# class Car(object):
#     kinds = []
#     MaxSpeed = 300
#     MaxPeoeple = 5

#     def __init__(self, 이름):
#         self.name = 이름

#         self.kinds.append(이름)
#     def move(self, x):
#         print(self.name, x, '의 스피드로 움직이고 있습니다.')
#         print(self.kinds)
#         self.stop()

#     def stop(self):
#         print('멈췄습니다.')

# k5 = Car('케이파이브')
# k5.move(100)
# k3 = Car('케이쓰리')
# k3.move(200)

# ###################################
# class Car(object):
#     kinds = []
#     MaxSpeed = 300
#     MaxPeoeple = 5
#     def __init__(self, 이름):
#         self.name = 이름
#         self.kinds.append(이름)
#     def __add__(self, obj):
#         return 'hello world', obj.name
#     def __str__(self): #제목을 알려줍니다.
#         return self.name
#     def move(self, x):
#         print(self.name, x, '의 스피드로 움직이고 있습니다.')
#         print(self.kinds)
#         self.stop()
#     def stop(self):
#         print('멈췄습니다.')

# k5 = Car('케이파이브')
# k3 = Car('케이쓰리')

# print(k5 + k3)
# print(k5)

###################################
class Car(object):
    kinds = []
    MaxSpeed = 300
    MaxPeoeple = 5
    def __init__(self, 이름):
        self.name = 이름
        self.kinds.append(이름)
    def __add__(self, obj):
        return 'hello world', obj.name
    def __str__(self): #제목을 알려줍니다.
        return self.name
    def move(self, x):
        print(self.name, x, '의 스피드로 움직이고 있습니다.')
        print(self.kinds)
        self.stop()
    def stop(self):
        print('멈췄습니다.')
    @staticmethod #decorator
    def 스피드배속(현재스피드, 배속할스피드):
        print(f'현재 {현재스피드 * 배속할스피드}의 스피드로 달리고 있습니다.')


k5 = Car('케이파이브')
k3 = Car('케이쓰리')

print(k5 + k3)
print(k5)

Car.스피드배속(100, 2)

########################################
# 상속
class Car(object):
    maxSpeed = 300
    maxPeople = 5
    def move(self, x):
        print(x, '의 스피드로 달리고 있습니다.')
    def stop(self):
        print('멈췄습니다.')

class HybridCar(Car):
    battery = 1000
    batteryKM = 300

class ElectricCar(HybridCar):
    battery = 2000
    batteryKM = 600


k5 = HybridCar()
electricCarK5 = ElectricCar()
k5.maxSpeed
print(electricCarK5.maxSpeed)
print(electricCarK5.battery)