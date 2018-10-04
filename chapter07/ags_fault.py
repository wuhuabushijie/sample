class Company:
    def __init__(self, name, staffs=[]):
        self.name=name
        self.staffs=staffs

    def add(self,staff):
        self.staffs.append(staff)


com1 = Company("com1")
com2 = Company("com2")

com1.add("bob1")
com2.add("bob2")

print(com1.staffs)
print(com2.staffs)
print(com1.staffs is com2.staffs)

# 不要将函数默认参数设置为可变数据类型
# 如果在调用方法时，不对可变类型的默认参数赋值，那么所有的调用都是用同一个参数，一处更改就会影响到其他调用

def add(a,b=[]):
    b.append(a)
    return b

c = add(2)
d = add(3)

print(c)
print(d)


# def add(a, b):
#     c = a + b
#     return c
#
#
# d = [1, 2]
# e = [3, 4]
#
# c1 = add(d, e)
#
# print(c1)
# print(d)
# print(e)