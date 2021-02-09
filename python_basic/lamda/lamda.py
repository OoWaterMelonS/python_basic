# lambda定义一个简单的函数，实现简化代码的功能，看代码会更好理解。
# fun = lambda x,y : x+y, 冒号前的x,y为自变量，冒号后x+y为具体运算。
fun= lambda x,y:x+y
x=int(input('x='))    #这里要定义int整数，否则会默认为字符串
y=int(input('y='))
print(fun(x,y))