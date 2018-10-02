import numbers

class Group:
    def __init__(self,group_name,company_name,staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs=staffs

    # 实现可切片，返回Group对象
    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item,slice):
            return cls(self.group_name,self.company_name,staffs=self.staffs[item])
        elif isinstance(item,numbers.Integral):
            return cls(self.group_name,self.company_name,staffs=[self.staffs[item]])

    # 实现反转
    def __reversed__(self):
        self.staffs.reverse()

    # 获取长度
    def __len__(self):
        return len(self.staffs)

    # 实现迭代器
    def __iter__(self):
        iter(self.staffs)

    # 使类具备contains查询
    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False

if __name__=="__main__":
    #初始化
    staffs = ["s1","s2","s3","s4","s5","s6"]
    group = Group("IT","FKYD",staffs)

    # 对group进行切片
    print(group[::2].staffs)

    # 获取group的长度
    print(len(group))

    # 反转group
    reversed(group)
    print(group.staffs)

    # 查询某元素是否在group中
    if "s6" in group:
        print("Yes")