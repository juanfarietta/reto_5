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
