import threading
from threading import Condition

num = 0
max_num = 5


class Producer(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="producer")
        self.cond = cond

    def run(self):
        global num
        global max_num
        with self.cond:
            print("鱼丸来咯！")
            while True:
                num += 1
                print("加 {} 个".format(num))
                if num >= max_num:
                    print("鱼丸加满了，请慢用！")
                    self.cond.notify()
                    self.cond.wait()


class Consumer(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="consumer")
        self.cond = cond

    def run(self):
        global num
        global max_num
        with self.cond:
            self.cond.wait()
            while True:
                print("吃了 {} 一个".format(num))
                num -= 1
                if num <= 0:
                    print("我吃完了，再来一锅！")
                    self.cond.notify()
                    self.cond.wait()


if __name__ == "__main__":
    cond = Condition()
    consumer = Consumer(cond)
    producer = Producer(cond)
    consumer.start()
    producer.start()
