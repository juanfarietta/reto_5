# Reto 5
```
Reto 5/
├── Shape/
│   ├── __init__.py
│   ├── ShapeRectangle.py
│   └── ShapeTriangle.py
└── main.py
```
## Class Shape 1
```python
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
```
## Class Shape 2
```python
class Shape:
    def __init__(self, regular:bool, vertices:list, edges:list, inner_angles:list):
        self.regular = regular
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = inner_angles

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass

    def compute_inner_angles(self):
        pass

    def get_regular(self):
        return self.regular

    def set_regular(self, regular):
        self.regular = regular

    def get_vertices(self):
        return self._vertices

    def set_vertices(self, vertices):
        self._vertices = vertices

    def get_edges(self):
        return self._edges

    def set_edges(self, edges):
        self._edges = edges

    def get_inner_angles(self):
        return self._inner_angles

    def set_inner_angles(self, inner_angles):
        self._inner_angles = inner_angles

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def compute_distance(self, other_point):
        pass

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y


class Line:
    def __init__(self, start_point, end_point):
        self._start_point = start_point
        self._end_point = end_point
        self._length = self.compute_length()

    def compute_length(self):
        pass

    def get_start_point(self):
        return self._start_point

    def set_start_point(self, start_point):
        self._start_point = start_point

    def get_end_point(self):
        return self._end_point

    def set_end_point(self, end_point):
        self._end_point = end_point

    def get_length(self):
        return self._length

    def set_length(self, length):
        self._length = length

class Triangle(Shape):
    def __init__(self, regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(regular, vertices, edges, inner_angles)

    def compute_perimeter(self):
        if len(self._edges) == 3:
            self._perimeter = sum(self._edges)
        return self._perimeter
    
    def compute_area(self):
        if len(self._edges) == 3:
            s = self.compute_perimeter() / 2
            self._area = (s * (s - self._edges[0]) * (s - self._edges[1]) * (s - self._edges[2]))**0.5
        return self._area

    def compute_inner_angles(self):
        if len(self._inner_angles) == 3:
            self._inner_angles = sum(self._inner_angles)
        return self._inner_angles

class Isosceles(Triangle):
    def __init__(self, regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(regular, vertices, edges, inner_angles)

    def is_isosceles(self):
        if self._edges[0] == self._edges[1] or self._edges[0] == self._edges[2] or self._edges[1] == self._edges[2]:
            return True
        return False
    
    def compute_perimeter(self):
        return super().compute_perimeter()
    
    def compute_area(self):
        return super().compute_area()
    
    def compute_inner_angles(self):
        return super().compute_inner_angles()

class Equilateral(Triangle):
    def __init__(self, regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(regular, vertices, edges, inner_angles)

    def is_equilateral(self):
        if self._edges[0] == self._edges[1] and self._edges[0] == self._edges[2]:
            return True
        return False
    
    def compute_perimeter(self):
        return super().compute_perimeter()
    
    def compute_area(self):
        return super().compute_area()
    
    def compute_inner_angles(self):
        return super().compute_inner_angles()


class Scalene(Triangle):
    def __init__(self, regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(regular, vertices, edges, inner_angles)

    def is_scalene(self):
        if self._edges[0] != self._edges[1] and self._edges[0] != self._edges[2] and self._edges[1] != self._edges[2]:
            return True
        return False
        
    def compute_perimeter(self):
        return super().compute_perimeter()
    
    def compute_area(self):
        return super().compute_area()
    
    def compute_inner_angles(self):
        return super().compute_inner_angles()


class TriangleRectangle(Triangle):
    def __init__(self, regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(regular, vertices, edges, inner_angles)

    def is_triangle_rectangle(self):
        if 90 in self._inner_angles:
            return True
        return False
        
    def compute_perimeter(self):
        return super().compute_perimeter()
    
    def compute_area(self):
        return super().compute_area()
    
    def compute_inner_angles(self):
        return super().compute_inner_angles()
```
```python
#main.py
from Shape.ShapeRectangle import Line
from Shape.ShapeRectangle import Point
from Shape.ShapeRectangle import Rectangle

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
```
