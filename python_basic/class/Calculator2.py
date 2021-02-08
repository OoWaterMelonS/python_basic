class Calculator:
    name = 'Good Calculator'  # 该行为class的属性
    price = 18

    # 这里的下划线是双下划线
    def __init__(self, name, price, hight=10, width=14, weight=16):  # 后面三个属性设置默认值,查看运行
        self.name = name
        self.price = price
        self.h = hight
        self.wi = width
        self.we = weight

# 注意定义自变量cal等于Calculator要加括号“()” ,
# cal=Calculator()否则运行下面函数的时候会出现错误,导致无法调用.
cal = Calculator('bad calculator',18)
print(cal.name)
print(cal.price)
print(cal.h)