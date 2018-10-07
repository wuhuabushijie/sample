import threading,time
from threading import Lock,RLock

total = 0
def add(lock):
    global total
    for i in range(1000):
        # time.sleep(0)
        lock.acquire()
        print("add {} times".format(i+1))
        # total += 1
        lock.release()

def desc(lock):
    global total
    for i in range(1000):
        # time.sleep(0)
        lock.acquire()
        print("desc {} times".format(i + 1))
        # total -= 1
        lock.release()

lock = RLock()
thread_1 = threading.Thread(target=add,args=(lock,))
thread_2 = threading.Thread(target=desc,args=(lock,))
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()

# print(total)