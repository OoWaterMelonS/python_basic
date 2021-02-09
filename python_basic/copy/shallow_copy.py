# 当使用浅拷贝时，python只是拷贝了最外围的对象本身，内部的元素都只是拷贝了一个引用而已
import copy
a=[1,2,3]
c=copy.copy(a)
print(id(a))
print(id(c))
print(id(a)==id(c))
# 改变c的第二个值时，a不会被改变
c[1]=22222
# a值不变,c的第二个值变了，这就是copy和‘==’的不同
#  id(a)==id(b)
print(a,c)