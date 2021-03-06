# 对外围和内部元素都进行了拷贝对象本身，而不是对象的引用
import copy

# copy.copy
a=[1,2,[3,4]]  #第三个值为列表[3,4],即内部元素
d=copy.copy(a) #浅拷贝a中的[3，4]内部元素的引用，非内部元素对象的本身

print(id(a)==id(d))
print(id(a[2])==id(d[2]))

a[2][0]=3333  #改变a中内部原属列表中的第一个值
print(d)          #这时d中的列表元素也会被改变

#copy.deepcopy()

e=copy.deepcopy(a) #e为深拷贝了a
a[2][0]=333 #改变a中内部元素列表第一个的值
print(e) #因为时深拷贝，这时e中内部元素[]列表的值不会因为a中的值改变而改变
