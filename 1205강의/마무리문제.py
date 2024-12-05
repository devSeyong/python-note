# 문제 2
"""
도서관 관리 시스템을 만드세요.
Book 클래스를 만들고 다음 기능을 구현하세요:
- 책의 제목, 저자, 출판연도를 초기화하는 생성자
- 책 정보를 출력하는 메서드
- 책의 대여 상태를 관리하는 메서드 (대여/반납)

테스트 코드:
book1 = Book("Python Programming", "John Smith", 2023)
book1.display_info()
book1.borrow()
book1.return_book()
"""
class Book:
    def __init__(self,name1,human1,since1):
        self.name = name1
        self.human = human1
        self.since = since1
    def __str__(self):
        return f"책 제목: {self.name}\n저자: {self.human}\n출판연도:{self.since}"

book1 = Book("Python Programming", "John Smith", 2023)
print(book1)

"""
도형을 나타내는 클래스 시스템을 만드세요.
Shape 클래스: 기본 도형 클래스 (색상 속성)
Rectangle 클래스: Shape 상속, 가로/세로 길이로 면적 계산
Triangle 클래스: Shape 상속, 밑변/높이로 면적 계산

각 도형의 면적을 계산하고 색상과 함께 정보를 출력하세요.

테스트 코드:
rect = Rectangle("빨강", 5, 3)
tri = Triangle("파랑", 4, 6)
rect.display_info()
tri.display_info()
"""
class Shape:
    def color(self,color:str):
        self.color = color
class Rectangle(Shape):
    def len_1(self,가로:int,세로:int):
        self.가로.세로 = 가로 * 세로
class Triangle(Shape):
    def len_2(self,밑변:int,높이:int):
        self.밑변.높이 = 밑변 * 높이
rect = Rectangle("빨강", 5, 3)
tri = Triangle("파랑", 4, 6)
print(rect)
