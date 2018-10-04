from datetime import date,datetime

class User:
    def __init__(self,name,birthday):
        self.name = name
        self.birthday=birthday

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

if __name__ == "__main__":
    user = User("bob",date(1989,11,21))
    print(user.age)