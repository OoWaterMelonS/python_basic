# map是把函数和参数绑定在一起。
# 此处需要区别dictionary
def fun(x, y):
    return (x + y)
print(list(map(fun,[1],[2])))