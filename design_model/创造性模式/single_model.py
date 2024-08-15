""""
单例模式的多种写法。主要看是继承了元类

"""

# ..........................1. 不继承元类
class Singleton():

    _instances = None

    def __new__(cls, *args, **kwargs):
        if not cls._instances:
            cls._instances = super(Singleton, cls).__new__(cls)

        return cls._instances


class MyClass(Singleton):
    def __init__(self, a):
        self.a = a

a = MyClass(1)
b = MyClass(2)


# ..........................2. 继承元类type
# 元类通过重写 __call__ 方法，从而实现各种高级功能如单例和缓存等.

class Singleton2(type):
    # _instances 是一个字典，用于存储不同类的实例。
    _instances = {}

    # 元类使用 __call__ 方法来控制实例的创建。
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton2, cls).__call__(*args, **kwargs)

        # 打印会有两个不同的实例对象
        print(cls._instances)  #
        return cls._instances[cls]


# 注意写法： metaclass=Singleton2
class MyClass3(metaclass=Singleton2):
    def __init__(self, a):
        self.a = a


class MyClass4(metaclass=Singleton2):
    def __init__(self, a):
        self.a = a


a = MyClass3(1)
b = MyClass3(2)


# ..........................3. 通过弱引用变相的实现
import  weakref

class Cached(type):

    def __init__(self, *args, **kwds):
        super(Cached, self).__init__(*args, **kwds)
        self._cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self._cache:
            return self._cache[args]
        else:
            obj = super(Cached, self).__call__(*args)
            self._cache[args] = obj

            # 容易出错，这里要返回对象的引用，容易写成return self._cache[args]
            return obj
class Span(metaclass=Cached):
    def __init__(self, num):
        print(f"数字 {num}")


x1 = Span(1)
x2 = Span(2)
x3 = Span(2)
print(x1 is x2)
print(x2 is x3)










