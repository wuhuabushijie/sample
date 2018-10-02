import bisect

# 用来处理和维持已排序的序列
# insort 将参数插入序列中
# bisect 查询参数将要插入的位置
aList = []
bisect.insort(aList,3)
bisect.insort(aList,4)
bisect.insort(aList,7)
bisect.insort(aList,4)
bisect.insort(aList,3)
bisect.insort(aList,6)
bisect.insort(aList,5)
bisect.insort(aList,9)
print(bisect.bisect(aList,8))

print(aList)