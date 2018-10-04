from datetime import date
import numbers

class IntField:
    def __get__(self, instance, owner):
        return self.item
    def __set__(self, instance, value):
        if not isinstance(value,numbers.Integral):
            raise ValueError("int value needed")
        self.item = value

    def __delete__(self, instance):
        pass


class User:
    age = IntField()
    def __init__(self,name,birthday):
        self.name = name
        self.birthday=birthday
        self.age = 65


    # 当外部调用类中没有定义的属性的时，__getattr__ 可以提供处理逻辑
    def __getattr__(self, item):
        return '"'+item+'" is not defined in ' + self.__class__.__name__

    # 外部对类中所有属性的访问，都将经过__getattribute__
    # def __getattribute__(self, item):
    #     if item in User.__dict__:
    #         return self.item

if __name__ == "__main__":
    user = User("bob",date(1989,1,22))
    user.age="aaa"
    print(user.age)
