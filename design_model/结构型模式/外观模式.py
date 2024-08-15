"""
外观模式：
    我理解为：如果有多个子类有某些方法需要一起组合调用，将他们重新封装在一个新类中使用
"""

# 子系统类
class CPU:
    def run(self):
        print('CPU start to run...')

    def stop(self):
        print('CPU stop to run...')

# 子系统类
class Disk:
    def run(self):
        print('Disk start to run...')

    def stop(self):
        print('Disk stop to run...')

# 子系统类
class Memory:
    def run(self):
        print('Memory start to run...')

    def stop(self):
        print('Memory stop to run...')

# 外观
class Computer():
    def __init__(self):
        self.CPU = CPU()
        self.Disc = Disk()
        self.Member = Memory()

    def run(self):
        self.CPU.run()
        self.Disc.run()
        self.Member.run()

    def stop(self):
        self.CPU.stop()
        self.Disc.stop()
        self.Member.stop()

# 客户端，高层代码
c = Computer()
c.run()
c.stop()
