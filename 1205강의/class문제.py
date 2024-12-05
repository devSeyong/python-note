# 1. car 클래스에서 함수를 만든다. 함수 이름은 change_brand, 함수는 brand 값을 변경해야한다.
# 2. 멤버 변수에는 brand가 있어야한다. 그 변수는 기본적으로 값이 없다.
# 3. 외부에서 change_brand 호출해서 값을 바꾼다.

class Car(object):
		kinds = []
		speed = 300
		brand = None
		def add_kinds(self, name):
				self.kinds.append(name)
		def change_speed(self, speed):
				self.speed = speed
		def change_brand(self, input_brand):
				self.brand = input_brand
k5 = Car()
k3 = Car()
k5.add_kinds('k5')
k3.add_kinds('k3')
k5.change_speed(500)
k3.change_speed(250)

print('k5.kinds:', k5.kinds)
print('k3.kinds:', k3.kinds)
print('k5.speed:', k5.speed)
print('k3.speed:', k3.speed)

# 1. Human 이라는 클래스를 만들고
# 2. 인스턴스 변수는 name, gender(성별), 나이(age) 를 가지고 있어야한다. 각각
# 3. __init__ 메서드를 통해 각 위 인스턴스 변수를 초기화한다.
# 4. 각 인스턴스 변수를 출력할 함수를 만든다. ( 출력형태는 자유)
# 5. 인스턴스를 만들어 함수를 호출해본다.

내가 푼 정답
class Human:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

seyong = Human("세용","남",33)
misuk = Human("미숙","여",60)

print(seyong.name, seyong.gender, seyong.age)

#강사님 정답
class Human:

    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def print_name(self):
        print(self.name)

    def print_gender(self):
        print(self.gender)

    def print_age(self):
        print(self.age)


man = Human("뀨","남자",11)
woman = Human("뀨2","여",10)

man.print_name()
woman.print_name()

man.print_gender()
woman.print_gender()

man.print_age()
woman.print_age()