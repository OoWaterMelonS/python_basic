class Calculator:
    name = 'Good Calculator'  # 该行为class的属性
    price = 18

    def add(self, x, y):
        print(self.name)
        result = x + y
        print(result)

    def minus(self, x, y):
        result = x - y
        print(result)

    def times(self, x, y):
        print(x * y)

    def divide(self, x, y):
        print(x / y)

# 注意定义自变量cal等于Calculator要加括号“()” ,
# cal=Calculator()否则运行下面函数的时候会出现错误,导致无法调用.
cal = Calculator()
cal.add(1,2)