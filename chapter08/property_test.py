from datetime import date,datetime

class User:
    def __init__(self,name,birthday):
        self.name = name
        self.birthday=birthday
        self._age=None

    @property
    def age(self):
        if self._age:
            return self._age
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self,value):
        self._age=value

if __name__ == "__main__":
    user = User("bob",date(1989,11,21))
    print(user.age)
    user._age=45
    print(user._age)
    print(user.age)
