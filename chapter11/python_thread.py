import threading, time

def get_detail_html():
    print("Start getting html details")
    time.sleep(4)
    print("Getting html details ended")

def get_detail_url():
    print("Start getting url details")
    time.sleep(2)
    print("Getting Url details ended")

def run1():
    sub_thread_1 = threading.Thread(target=get_detail_url)
    sub_thread_2 = threading.Thread(target=get_detail_html)
    sub_thread_1.start()
    sub_thread_2.start()
    start_time = time.time()
    sub_thread_1.join()
    sub_thread_2.join()
    last_time = time.time()-start_time
    print(last_time)


class GetHtmlDetails(threading.Thread):
    def __init__(self,name):
        super().__init__(name=name)

    def run(self):
        print("Start getting html details")
        time.sleep(4)
        print("Getting html details ended")


class GetUrlDetails(threading.Thread):
    def __init__(self,name):
        super().__init__(name=name)

    def run(self):
        print("Start getting url details")
        time.sleep(2)
        print("Getting Url details ended")


def run2(html,url):
    html.start()
    url.start()
    start_time = time.time()
    html.join()
    url.join()
    last_time = time.time()-start_time
    print(last_time)


if __name__=="__main__":
    # run1()
    getHtmlDetails = GetHtmlDetails("get_html_details")
    getUrlDetails = GetUrlDetails("get_url_details")
    run2(getHtmlDetails,getUrlDetails)