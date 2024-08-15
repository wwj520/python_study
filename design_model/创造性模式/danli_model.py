"""

 单例模式保证一个类只有一个实例，并提供一个访问它的全局访问点。优点是对唯一实例的受控访问（只有一个实例），
 单例相当于全局变量，但防止了命名空间被污染（变量命名不会有冲突）。写个例子来加深理解：

"""


class Singleton:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:  # 这里换成not hasattr(cls, "_instance") 会出错，因为 cls.__instance = None 也是有属性的
            cls._instance = super().__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, a):
        self.a = a


a = MyClass(1)
b = MyClass(2)
print(a.a)
print(b.a)
print(id(a), id(b))

