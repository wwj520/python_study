"""
观察者模式：发布-订阅模式

"""

# demo: 一个发布者多个订阅者
# 思考： 如何自动更新

from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):  # 抽象订阅者

    @abstractmethod
    def update(self, notice):...  # notice应该是Notice对象


class Notice:  # 抽象发布者

    def __init__(self):
        self.observers = []

    def attach(self, obs):  # 订阅
        self.observers.append(obs)

    def detach(self, obs):  # 接触绑定
        self.observers.remove(obs)

    def notify(self):
        for obs in self.observers:
            obs.update(self)   # self: Noticed对象本身


class StaffNotice(Notice):  # 具体发布者
    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter            # ****重点思考的位置
    def company_info(self, company_info):
        self.__company_info = company_info
        self.notify()


class Staff(Observer):  # 具体订阅者

    def __init__(self, company_info=None):
        self.company_info = company_info

    def update(self, notice):
        self.company_info = notice.company_info




notice = StaffNotice("test")
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
print(s1.company_info)
notice.company_info = "tesdt2"
print(s1.company_info)
print(s2.company_info)
notice.detach(s1)
notice.company_info = "tesdt3"
print(s1.company_info)
print(s2.company_info)
