from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor,wait,ALL_COMPLETED,as_completed
import time

def fib(num):
    if num <= 2:
        return 1
    return fib(num-1)+fib(num-2)

if __name__ == "__main__":
    # with ThreadPoolExecutor(8) as executor:
    #     start_time = time.time()
    #     all_task = [executor.submit(fib,num) for num in range(20,40)]
    #     wait(all_task,return_when=ALL_COMPLETED)
    #     for future in as_completed(all_task):
    #         data=future.result()
    #         print(data)
    #     print(time.time() - start_time)

    with ProcessPoolExecutor(8) as executor:
        start_time = time.time()
        for data in executor.map(fib,[i for i in range(20,40)]):
            print(data)

        # all_task = [executor.submit(fib,num) for num in range(20,40)]
        # wait(all_task,return_when=ALL_COMPLETED)
        # for future in as_completed(all_task):
        #     data=future.result()
        #     print(data)
        print(time.time()-start_time)
