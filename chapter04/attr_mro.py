# 类属性的查找顺序 C3算法
# 在菱形继承关系中，优先查找同级类，广度优先
# 平行继承关系中，深度优先，优先查找父类的父类

class D:
    pass

# class E:
#     pass

class B(D):
    pass

# class C(E):
class C(D):
    pass

class A(B,C):
    pass

# 打印A类中缺失属性的查找顺序
print(A.__mro__)