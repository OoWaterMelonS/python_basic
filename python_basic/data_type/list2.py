a = [1,2,3,4,1,1,-1]
print(a[0])  # 显示列表a的第0位的值
# 1


print(a[-1]) # 显示列表a的最末位的值
# -1

print(a[0:3]) # 显示列表a的从第0位 到 第2位(第3位之前) 的所有项的值
# [1, 2, 3]

print(a[5:])  # 显示列表a的第5位及以后的所有项的值
# [1, -1]

print(a[-3:]) # 显示列表a的倒数第3位及以后的所有项的值
# [1, 1, -1]
# 打印列表中的某个值的索引(index):
a = [1,2,3,4,1,1,-1]
print(a.index(2)) # 显示列表a中第一次出现的值为2的项的索引
# 1
# 统计列表中某值出现的次数：
print(a.count(-1))