# zip函数接受任意多个（包括0个和1个）序列作为参数，合并后返回一个
# tupleu组成的列表
a=[1,2,3]
b=[4,5,6]
ab=zip(a,b)
print(ab)
print(list(ab))  #需要加list来可视化这个功能
for i,j in zip(a,b):
    print(i/2,j/2)
