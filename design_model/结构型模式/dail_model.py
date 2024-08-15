"""
代理模式：
    需代理：根据需要保护增真实的对象， 在需代理；类中实现需要的实例
    保护代理：控制对原始对象的访问，用于对象有不同的访问权限。下面是不使用虚代理的例子：
"""
from abc import ABCMeta, abstractmethod

# ************************* 需代理的实例 ***************
class Subject(metaclass=ABCMeta):

    @abstractmethod
    def get_content(self): ...

    @abstractmethod
    def set_content(self, content): ...


class RealSubject(Subject):

    def __init__(self, file_name):
        self.filename = file_name
        with open(self.filename, 'r', encoding='utf-8') as f:
            self.content = f.read()

    def get_content(self):
        return self.content

    def set_content(self, content):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(content)


class ViralSubject(Subject):
    def __init__(self, file_name):
         self.file_name = file_name
         self.sub = None

    def get_content(self):
        if not self.sub:
            # 需要时调用
            self.sub = RealSubject(self.file_name)
        return self.sub.get_content()

    def set_content(self, content):
        if not self.sub:
            self.sub = RealSubject(self.file_name)
        return self.sub.set_content(content)

x = ViralSubject('test.txt')
print(x.get_content())


#  ************************* 保护代理的实例 ***************
from abc import ABCMeta, abstractmethod

class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass

class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        print('读取文件内容！')
        with open(self.filename, 'r', encoding='utf-8') as f:
            self.content = f.read()

    def get_content(self):
        return self.content

    def set_content(self, content):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(content)

class ProtectedSubject(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        raise PermissionError('无写入权限！')
