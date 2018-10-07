import threading,time
from threading import Semaphore,Condition

class HtmlSpider(threading.Thread):
    def __init__(self,url,sem,times):
        super().__init__()
        self.url = url
        self.sem = sem
        self.times = times

    def run(self):
        time.sleep(3)
        print(str(self.times) + ". got html text successful")
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self,sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            htmlSpider=HtmlSpider("url {}".format(i),self.sem,i)
            htmlSpider.start()
            htmlSpider.join()

if __name__=="__main__":
    sem = Semaphore(3)
    urlProducer = UrlProducer(sem)
    urlProducer.start()