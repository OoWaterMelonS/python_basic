# 如果说List是有顺序地输出输入的话，
# 那么字典的存档形式则是无需顺序的，


# 在字典中，有key和 value两种元素，每一个key对应一个value, key是名字, value是内容。
# 数字和字符串都可以当做key或者value，
# 在同一个字典中, 并不需要所有的key或value有相同的形式。




# 这样说, List 可以说是一种key为有序数列的字典。
a_list = [1,2,3,4,5,6,7,8]

d1 = {'apple':1, 'pear':2, 'orange':3}
d2 = {1:'a', 2:'b', 3:'c'}
d3 = {1:'a', 'b':2, 'c':3}

print(d1['apple'])  # 1
print(a_list[0])    # 1

#  此处使用了del  关键字
del d1['pear']
print(d1)   # {'orange': 3, 'apple': 1}

d1['b'] = 20
print(d1)   # {'orange': 3, 'b': 20, 'apple': 1}