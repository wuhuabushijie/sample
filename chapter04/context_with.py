#上下文管理器简化版

import contextlib

@contextlib.contextmanager
def func():
    print("enter")
    yield {1}
    print("exit")

if __name__ =="__main__":
    with func() as func:
        print(func)