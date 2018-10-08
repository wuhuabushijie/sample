from concurrent.futures import ThreadPoolExecutor,as_completed
import  time

def get_html(times):
    # time.sleep(times)
    # print("get page {} success".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=3)
# 通过submit函数提交执行的函数到线程中，submit是非阻塞的，立即返回
# task1 = executor.submit(get_html,(3))
# task2 = executor.submit(get_html,(2))

# 要获取已经成功的任务的返回值
urls =[2,3,4,5,6,7,8]
# all_task = [executor.submit(get_html,(url)) for url in urls]
# for future in as_completed(all_task):
#     data = future.result()
#     print("get {} page success".format(data))

#通过executor获取已经完成的task
for data in executor.map(get_html,urls):
    print("get {} page success".format(data))

# #done()方法用于判定某个任务是否完成
# print(task1.done())
# #cancel用于取消尚未开始执行的线程
# print(task2.cancel())
# time.sleep(4)
# print(task1.done())
# # result()为阻塞方法，可以获取task的结果
# print(task1.result())