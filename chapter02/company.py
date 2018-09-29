class Company:
    def __init__(self, employee):
        self.employee = employee

    # 使用__getitem__方法，使得类可迭代，可切片
    def __getitem__(self, item):
        return self.employee[item]

    # 使用__len__方法，使得类可以调用len()
    def __len__(self):
        return len(self.employee)

    # 将类转换为字符串
    def __str__(self):
        return "Company"
        # return ",".join(self.employee)

    # 开发模式下使用，解释器调用
    def __repr__(self):
        return "Company"
        # return ",".join(self.employee)


company= Company(["tom","bob","jane"])
company1=company[:2]


# print(company)

# print(len(company))

# for em in company:
#     print(em)

# for em in company1:
#     print(em)

# print(company[1])

