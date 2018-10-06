class Company:
    def  __init__(self,employees):
        self.employees = employees

    def __iter__(self):
        return EmIterator(self.employees)

    def __getitem__(self, item):
        return self.employees[item]

    def __len__(self):
        return len(self.employees)

class EmIterator:
    def __init__(self,items):
        self.items = items
        self.index = 0

    def __next__(self):
        try:
            item=self.items[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return item


if __name__=="__main__":
    company = Company(["bob","jack","garfield","leo"])
    # for em in company:
    #     print(em)
    com = iter(company)
    print(next(com))
    print(next(com))
    print(next(com))
