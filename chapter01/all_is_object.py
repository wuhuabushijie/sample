def ask(name='bobby'):
    print(name)

class Person():
    def __init__(self):
        print('bobby1')

def decorator_func():
    print('dec start')
    return ask

my_ask = decorator_func()
my_ask()

# obj_list = []
# obj_list.append(ask)
# obj_list.append(Person)
# for item in obj_list:
#     print(item())

# 函数是一个对象
# my_func = ask
# my_func('jessy')

# 实例化一个类
# my_class = Person()
