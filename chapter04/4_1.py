'''鸭子类型，多态'''

class Cat:
    def say(self):
        print("I am a cat")

class Dog:
    def say(self):
        print("I am a dog")

class Duck:
    def say(self):
        print("I am a duck")

animal_list = [Cat,Dog,Duck]
for animal in animal_list:
    animal().say()

