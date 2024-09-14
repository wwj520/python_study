#!usr/bin/env python
# -*- coding:utf-8 _*-
# __author__：lianhaifeng
# __time__：2024/2/14 18:51
from typing import Any


class Coordinate:
    def __init__(self, x: Any, y: Any) -> None:
        self.x = x  # 设置横坐标
        self.y = y  # 设置纵坐标

    def __repr__(self) -> str:
        return f"Coordinate(x={self.x}, y={self.y})"  # 返回对象的字符串表示形式

    def __eq__(self, other: Any) -> bool:
        # 检查另一个对象是否是相同类型的Coordinate
        if isinstance(other, self.__class__):
            # 比较两个对象的横纵坐标是否相等
            return (self.x, self.y) == (other.x, other.y)
        else:
            return NotImplemented

    def __ne__(self, other: Any) -> bool:
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            # 返回两个对象的相等性的否定
            return not result

    def __lt__(self, other: Any) -> bool:
        # 检查另一个对象是否是相同类型的Coordinate
        if isinstance(other, self.__class__):
            # 比较两个对象的横纵坐标的大小关系
            return (self.x, self.y) < (other.x, other.y)
        else:
            return NotImplemented

    def __le__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return (self.x, self.y) <= (other.x, other.y)
        else:
            return NotImplemented

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return (self.x, self.y) > (other.x, other.y)
        else:
            return NotImplemented

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return (self.x, self.y) >= (other.x, other.y)
        else:
            return NotImplemented

    def __hash__(self) -> int:
        # 返回对象的哈希值，用于将对象存储在散列数据结构中
        return hash((self.__class__, self.x, self.y))



if __name__ == '__main__':
# 创建坐标对象
    coord1 = Coordinate(3, 4)
    coord2 = Coordinate(5, 6)

    # 打印对象的字符串表示形式
    print(coord1)  # 输出: Coordinate(x=3, y=4)
    print(coord2)  # 输出: Coordinate(x=5, y=6)

    # 比较坐标对象是否相等
    print(coord1 == coord2)  # 输出: False
    print(coord1 != coord2)  # 输出: True
