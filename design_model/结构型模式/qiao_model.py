"""

桥模式:
    桥模式是将一个事物的【两个维度分离】，使其都可以独立地变化。当事物有两个维度的表现，两个维度都可能扩展时使用。
    优点是：抽象和实现相分离，扩展能力强。
"""

from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass

class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass


class Rectangle(Shape):
    name = "长方形"
    def draw(self):
        self.color.paint(self)

class Circle(Shape):
    def draw(self):
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        print("红色的%s" % shape.name)


Rectangle(Red()).draw()