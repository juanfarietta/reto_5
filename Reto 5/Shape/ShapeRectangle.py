class Shape:
    def __init__(self, lines):
        self.lines = lines

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def compute_length(self):
        return ((self.point2.x - self.point1.x)**2 + (self.point2.y - self.point1.y)**2)**0.5
    
    def compute_slope(self):
        self.slope = (self.point2.y - self.point1.y) / (self.point2.x - self.point1.x)
    
    def compute_horizontal_cross(self):
        if self.point1.y <= 0 and self.point2.y >= 0:
            return True
        elif self.point1.y >= 0 and self.point2.y <= 0:
            return True
        else:
            return False
        
    def compute_vertical_cross(self):
        if self.point1.x <= 0 and self.point2.x >= 0:
            return True
        elif self.point1.x >= 0 and self.point2.x <= 0:
            return True
        else:
            return False
        
class Rectangle(Shape):
    def __init__(self, left_line, right_line, top_line, bottom_line):
        self.left_line = left_line
        self.right_line = right_line
        self.top_line = top_line
        self.bottom_line = bottom_line

    def compute_area(self):
        return (self.right_line.point2.x - self.left_line.point1.x) * (self.top_line.point2.y - self.bottom_line.point1.y)
    
    def compute_perimeter(self):
        return 2 * (self.right_line.compute_length() + self.top_line.compute_length())

class Square(Rectangle):
    def __init__(self, line):
        super().__init__()
        self.line = line

    def compute_area(self):
        return self.line()**2
    
    def compute_perimeter(self):
        return 4 * self.line()


first_point = Point(1, 1)
second_point = Point(7, 1)
third_point = Point(7, 5)
fourth_point = Point(1, 5)

bottom_line = Line(first_point, second_point)
right_line = Line(second_point, third_point)
top_line = Line(third_point, fourth_point)
left_line = Line(fourth_point, first_point)

rectangle = Rectangle(left_line, right_line, top_line, bottom_line)
print("Area: ", rectangle.compute_area())
print("Perimeter: ", rectangle.compute_perimeter())