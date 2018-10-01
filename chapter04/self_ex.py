# 自省是通过一种机制查询对象内部结构
class User:
    name = "user"
    def __init__(self,school_name):
        self.school_name = school_name

if __name__ == "__main__":
    user = User("慕课网")
    print(user.__dict__)
    print(User.__dict__)
    print(user.__dir__())
    print(dir(user))
    print(dir(User))
    a = [1,2]
    print(dir(a))
    # print(a.__dict__)