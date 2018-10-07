from queue import Queue
import threading, time

def get_detail_html(queue):
    while True:
        url = queue.get()
        print("Start getting page {} details".format(url))
        time.sleep(1)
        print("page {} has been got.".format(url))
        if queue.empty():
            break

def get_detail_url(queue):
    print("Start getting url details")
    time.sleep(1)
    for i in range(100):
        queue.put("http://{}.com".format(i))
        # if queue.full():
        #     queue.task_done()
    print("Getting Url details ended")


def run1():
    url_queue = Queue(maxsize=1000)
    sub_thread_1 = threading.Thread(target=get_detail_url,args=(url_queue,))
    sub_thread_1.start()
    tt=[]
    for i in range(5):
        sub_thread = threading.Thread(target=get_detail_html, args=(url_queue,))
        tt.append(sub_thread)
        sub_thread.start()

    start_time = time.time()

    # url_queue.join()
    sub_thread_1.join()
    for i in tt:
        i.join()

    last_time = time.time()-start_time
    print(last_time)

if __name__=="__main__":
    run1()