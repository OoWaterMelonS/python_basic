def func():
    return 0

d4 = {'apple':[1,2,3], 'pear':{1:3, 3:'a'}, 'orange':func}
print(d4['pear'][3])    # a
# 字典还可以以更多样的形式出现，
# 例如字典的元素可以是一个List，
# 或者再放一个字典，再或者是一个function。
# 索引需要的项目时，只需要正确指定对应的key就可以了。

