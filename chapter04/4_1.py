'''鸭子类型，多态'''

class Cat:
    def say(self):
        print("I am a cat")

class Dog:
    def say(self):
        print("I am a dog")

    def __getitem__(self):
        return "bob8"

class Duck:
    def say(self):
        print("I am a duck")

animal_list = [Cat,Dog,Duck]
for animal in animal_list:
    animal().say()

a = ["bob1","bob2"]
b = ["bob2","bob3"]
name_tuple=("bob4","bob5")
name_set=set()
name_set.add("bob6")
name_set.add("bob7")
a.extend(name_tuple)
print(a)
