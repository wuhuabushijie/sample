# 斐波拉契
def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index - 1)+ fib(index - 2)

def fib2(index):
    result_list =[]
    n,a,b = 0,0,1
    while n<index:
        result_list.append(b)
        a,b = b,a+b
        n += 1
    return result_list

def gen_fib(index):
    n,a,b = 0,0,1
    while n<index:
        yield b
        a,b = b,a+b
        n += 1

if __name__=="__main__":
    # print(fib2(80))
    gen = gen_fib(80)
    print(type(gen))
    pass
    # for data in gen_fib(80):
    #     print(data)