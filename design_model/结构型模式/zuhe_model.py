"""
组合模式：[不常用]
    组合模式使得用户对单个对象和组合对象的使用具有一致性。优点是定义了包含基本对象和组合对象的层次结构；简化客户端代码，
    客户端可以一致地使用组合对象和单个对象；更加容易增加新类型的组件。

"""

from abc import ABCMeta, abstractmethod

# 抽象组件
class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass

# 叶子组件
class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '点(%s,%s)' % (self.x, self.y)

    def draw(self):
        print(self)

# 叶子组件
class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        # 这里 self.p1 和 self.p2 是 Point 对象。当 %s 格式化字符串时，Python 会自动调用 self.p1 和 self.p2 的 __str__ 方法来获取它们的字符串表示。
        return '线段[(%s,%s)]' % (self.p1, self.p2)

    def draw(self):
        print(self)

# 复合组件
class Picture(Graphic):
    def __init__(self, iterable):
        self.children = []
        for g in iterable:
            self.add(g)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        for g in self.children:
            g.draw()

# 简单图形
print('------简单图形------')
p = Point(1, 2)
l1 = Line(Point(1, 2), Point(3, 4))
l2 = Line(Point(5, 6), Point(7, 8))
print(p)
print(l1)
print(l2)
print('------复合图形(p,l1,l2)------')
# 复合图形
pic = Picture([p, l1, l2])
pic.draw()

