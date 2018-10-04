from datetime import date,datetime


class User:
    def __init__(self,name,birthday):
        self.name = name
        self.birthday=birthday
        self._age=None


    # 当外部调用类中没有定义的属性的时，__getattr__ 可以提供处理逻辑
    def __getattr__(self, item):
        return '"'+item+'" is not defined in ' + self.__class__.__name__

    # 外部对类中所有属性的访问，都将经过__getattribute__
    def __getattribute__(self, item):
        if item in User.__dict__:
            return self.item

if __name__ == "__main__":
    user = User("bob",date(1989,1,22))
