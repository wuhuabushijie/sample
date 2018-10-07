import threading, time

detail_url_list=[]

def get_detail_html():
    global detail_url_list
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()
            print("Start getting page {} details".format(url))
            time.sleep(1)
            print("page {} has been got.".format(url))
            if not len(detail_url_list):
                break

def get_detail_url():
    global detail_url_list
    print("Start getting url details")
    time.sleep(1)
    for i in range(20):
        detail_url_list.append("http://{}.com".format(i))
    print("Getting Url details ended")

def run1():
    sub_thread_1 = threading.Thread(target=get_detail_url)

    sub_thread_1.start()
    tt=[]
    for i in range(5):
        sub_thread = threading.Thread(target=get_detail_html)
        tt.append(sub_thread)
        sub_thread.start()

    sub_thread_1.join()
    start_time = time.time()
    for i in tt:
        i.join()


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
    run1()
    # getHtmlDetails = GetHtmlDetails("get_html_details")
    # getUrlDetails = GetUrlDetails("get_url_details")
    # run2(getHtmlDetails,getUrlDetails)