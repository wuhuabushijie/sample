import time,multiprocessing

def func(n):
    time.sleep(n)
    print("This is sub progress {}".format(n))
    return n

if __name__ == "__main__":
    # progress = multiprocessing.Process(target=func,args=(2,))
    # print(progress.pid)
    # progress.start()
    # print(progress.pid)
    # progress.join()
    # print("main progress end")

    # # 使用线程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(func,args=(3,))
    #
    # # 等待线程结束
    # pool.close()
    # pool.join()
    # print(result.get())

    # for result in pool.imap(func,[1,5,3]):
    #     print(result)

    for result in pool.imap_unordered(func,[1,5,3]):
        print(result)