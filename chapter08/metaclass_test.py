from collections.abc import *
from _collections_abc import __all__


class Base:
    def answer(self):
        print("This is base class")

def say(self):
    print("hello " + self.name)

class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        print("This is MetaClass")
        return super().__new__(cls,*args,**kwargs)

class User2(metaclass=MetaClass):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "User2"

if __name__ == "__main__":
    # type 也可以创建类
    User = type("User",(Base,),{"name":"bob","say":say})
    user = User()
    print(user.name)
    user.say()
    user.answer()

    user2=User2("bob")
    print(user2)
