# 列表推导式

odd_list = [i for i in range(21) if i % 2 == 0]
print(odd_list)

def handle_item(item):
    return item**2

item_list = [handle_item(i) for i in range(21) if i % 2 == 1]
print(item_list)

# 列表推导式效率高于列表操作

# 生成器表达式
iter_gen = (i for i in range(21) if i % 2 == 0)
print(type(iter_gen))
for i in iter_gen:
    print(i,end=" ")
print()

# 字典推导式
my_dict = {"bob1":12,"bob2":13,"bob3":76}
reverse_dict = {value:key for key,value in my_dict.items()}
my_dict1 = {key:value for key,value in [[1,2],[3,4]]}
print(reverse_dict)
print(my_dict1)

# 集合推导式
my_set = set(my_dict.keys())
my_set1 = {key for key,value in my_dict.items()}
my_set2 = {key for key in my_dict}
print(my_set)
print(my_set1)
print(my_set2)