import math

def circle_area(radius):
    """
    Calculate the area of a circle.
    
    :param radius: The radius of the circle.
    :return: The area of the circle.
    """
    return math.pi * radius ** 2

def rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    
    :param length: The length of the rectangle.
    :param width: The width of the rectangle.
    :return: The area of the rectangle.
    """
    return length * width

def triangle_area(base, height):
    """
    Calculate the area of a triangle.
    
    :param base: The base of the triangle.
    :param height: The height of the triangle.
    :return: The area of the triangle.
    """
    return 0.5 * base * height