# 一个对象的id值在CPython解释器里就代表它在内存中的`地址
import copy
a=[1,2,3]
b=a
print(id(a))
print(id(b))
# 改变b的第一个值，也会导致a值改变
b[0]=0
print(a)