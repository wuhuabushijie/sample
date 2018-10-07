from threading import Condition
import threading


class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond
        self.words = []
        for i in range(10):
            self.words.append("第 {} 句话".format(i + 1))

    def run(self):
        for i in range(len(self.words)):
            with self.cond:
                self.cond.wait()
                print("{name}说：{words}".format(name=self.name, words=self.words[i]))
                self.cond.notify()


class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫精灵")
        self.cond = cond
        self.words = []
        for i in range(10):
            self.words.append("第 {} 句话".format(i + 1))

    def run(self):
        for i in range(len(self.words)):
            with self.cond:
                print("{name}说：{words}".format(name=self.name, words=self.words[i]))
                self.cond.notify()
                self.cond.wait()


if __name__ == "__main__":
    cond = Condition()
    tianmao = TianMao(cond)
    xiaoai = XiaoAi(cond)

    xiaoai.start()
    tianmao.start()
