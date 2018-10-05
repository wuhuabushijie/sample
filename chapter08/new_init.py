class User:

    # __new__用来在对象生成之前控制其的生成过程
    # __init__是用来完善对象的
    # 如果__new__不返回对象，__init__将不会执行
    def __new__(cls, *args, **kwargs):
        print("in new")
        return super().__new__(cls)
    def __init__(self,name):
        self.name=name
        print(self.name)



if __name__=="__main__":
    user = User("bob")