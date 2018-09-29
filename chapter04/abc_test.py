class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)

com = Company(["bob1","bob2"])
print(hasattr(com,"__len__"))

from collections.abc import Sized
isinstance(com,Company)