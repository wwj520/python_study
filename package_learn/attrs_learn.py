import datetime

import attrs
import attr
from attr import define, field, Factory, s, ib
from loguru import logger


# ----------------------- define：自动生称类的属性：替换 __init__() -----------------------
# @attr.s 和 @attr.define 类似: 生成类属性
# field 和 ib  功能类似
# init=False:  强制使用默认值且保持不变
# kw_only=True: 强制使用关键字的名字来传入，否则会报错
@define
class Test:
    # init=False强制使用默认值且保持不变
    a = field(type=int, default=0, init=False)
    b = field(type=str, default="")
    g = field(type=str, default="", kw_only=True)
    # field 和 ib 功能类似
    e = ib(type=str, default="")
    dt: datetime.datetime = field(default=Factory(datetime.datetime.now))

    # 可变对象作为默认值
    # Factory: 创建默认值的工厂函数。它允许你为属性提供一个动态生成的默认值，而不是一个静态的默认值。
    # 这在需要每次实例化对象时都生成一个新的默认值时非常有用，尤其是对于可变对象（如列表、字典等）。
    c = field(type=list, default=Factory(list))
    d = field(type=list, default=Factory(lambda: [12]))


# -----------------------派生属性：如何拥有依赖于其他属性的属性-----------------------
# __attrs_post_init__:   是attrs库中特殊方法，在实例化对象后被调用，可以用来设置属性的默认值，或者执行其他初始化操作。
# @dt_30_later2.default: 修改属性设置默认值
# value.isoformat():
# attr.asdict :  序列化，在这个demo中将 Data 实例转换为字典，并使用 serialize 函数对值进行序列化。

@define
class Data:
    dt: datetime.datetime = field(default=Factory(datetime.datetime))
    dt_30_later: datetime.datetime = field(init=False)
    dt_30_later_2 = field(init=False)

    def __attrs_post_init__(self):
        self.dt_30_later = self.dt + datetime.timedelta(days=30)

    @dt_30_later_2.default
    def _dt_30_later2(self):
        return self.dt + datetime.timedelta(days=60)

def serialize_data(insert, attributes, value):
    if isinstance(value, datetime.datetime):
        return value.isoformat()
    return value

json_data = attrs.asdict(Data(datetime.datetime(2024, 2, 18, 21, 46)), value_serializer=serialize_data)
# logger.info(json_data)


# ----------------------元数据------------------------
# metadata:  是attrs 库中用于为属性添加额外信息的机制。它允许你在定义属性时附加一些元数据（即额外的键值对），这些元数据可以在后续处理中使用。
# 元数据可以用于多种目的，例如文档生成、序列化、验证、配置等。

# attrs.fields: 是一个用于获取类中所有属性对象的函数。它返回一个包含所有属性对象的命名元组 每个属性对象包含了属性的元数据、类型、默认值等信息。

@attrs.define
class Product:
    name: str = attrs.field(metadata={"description": "The name of the product."})
    price: float = attrs.field(metadata={"description": "The price of the product."})


print(attrs.fields(Product).name.metadata["description"])


# ----------------------构建不可变类------------------------
from attr import attrs, attrib

# 类装饰器 @attrs(frozen=True)，可以创建不可变的实例。
# attrib: 和field功能类似

@attrs(frozen=True)
class Color:

    a = attrib(type=int, default=0)
    b = attrib(type=int, default=0)
    c = attrib(type=int, default=0, kw_only=True)


if __name__ == '__main__':
    color = Color(1, 2, c=3)
    # logger.info(color)
    # 当使用 color.b=6 修改值时候会报错误。


# ----------------------验证数据------------------------

# attr.validators.instance_of(str): 设置类型为字符串
@define
class Books:

    title = ib(default="none", validator=attr.validators.instance_of(str))
    page = ib(default=0, validator=attr.validators.instance_of(int))

book = Books("111", 200)
# book2 = Books("111", "200")  # 报错：'page' must be <class 'int'>


# ----------------------转换器------------------------
# 场景：输入数据类型与属性类型不一致，需要转换

# converter: 强制转换格式，值是该函数名
@define
class Point:

    a = ib(default=0, converter=int)
    b = ib(default=0, converter=int)

point2 = Point("3", "4")
# print(point2)


# ----------------------序列转换------------------------
## 场景：在JSON等字符串序列和对象之间进行转换，特别是在编写REST API和数据库交互时。
## asdict、astuple 方法用于序列化
## filter: 过滤字段
##

@define
class UserInfo(object):
    users = attr.ib()


@define
class User(object):
    email = attr.ib()
    name = attr.ib()

json_data = attr.asdict(UserInfo([User("lee@har.invalid", "Lee"), User("rachel@har.invalid", "Rachel")]), # noqa
            # 这里：_attr： 表示当前正在处理的属性（attribute）。它是一个 attr.Attribute 对象，包含了属性的元数据，如属性的名称、类型等。
            # 这里：value： 表示当前属性的值。
            filter=lambda _attr, value: _attr.name != "email"
            )
logger.info(json_data)


@define
class UserInfo(object):
    name = field()
    password = field()
    age = field()

import attrs
## attrs.filters.exclude: 用于排除特定的字段
logger.info(attrs.asdict(UserInfo("Marco", "abc@123", 22), filter=attrs.filters.exclude(attrs.fields(UserInfo).password, int))) # noqa

