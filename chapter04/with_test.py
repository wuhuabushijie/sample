# try except finally
# 如果finally中有return语句，优先return finally语句
def exe_try():
    try:
        print("try")
        # raise KeyError
        # return 1
    except KeyError as e:
        print("KeyError")
        return 2
    else:
        print("Else")
        return 3
    finally:
        print("Finally")
        return 4

#上下文管理器协议
class Sample:
    def __enter__(self):
        # 获取资源
        print("Enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print("Exit")

    def do_something(self):
        print("Do Something")

# 先执行with后面的Sample(),并调用其__enter__方法，
# 将返回的对象赋给as后面的变量sample,然后执行后面的语句，
# 执行完毕后，调用__exit__释放资源
with Sample() as sample:
    sample.do_something()

# if __name__=="__main__":
#     print(exe_try())