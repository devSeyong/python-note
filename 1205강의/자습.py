class Shape:
    def __init__(self, color):
        self.color = color
    
    def get_area(self):
        pass
    
    def display_info(self):
        print(f"도형 색상: {self.color}")
        print(f"도형 면적: {self.get_area()}")

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(self, color)
        self.base = base
        self.height = height
    
    def get_area(self):
        return (self.base * self.height) / 2
rect = Rectangle("빨강", 3, 5)
rect.display_info()
