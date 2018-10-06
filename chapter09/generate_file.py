import os
import random

class TextFile:

    def write_file(self,filename):
        self.filename = filename
        seed = "abcdefghijklmnopqrstuvwxwz1234567890"
        file = open(filename, "a")
        for a in range(0,1000):
            random2 = random.randint(0, 100)
            file.write(str(a+1)+". ")
            for i in range(0,random2):
                file.write(random.choice(seed))
            file.write("{|}")
        file.close()


textfile = TextFile()
textfile.write_file("test1.txt")

