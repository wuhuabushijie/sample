from chapter04.class_method import Date

class User:
    def __init__(self, birthday):
        self.__birthday=birthday

    def get_age(self):
        return 2018 - self.__birthday.year

if __name__ == "__main__":
    user=User(Date(1990,3,1))
    print(user.get_age())
    print(user._User__birthday)