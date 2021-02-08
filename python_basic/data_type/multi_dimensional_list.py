# 一个一维的List是线性的List，多维List是一个平面的List：
a = [1,2,3,4,5] # 一行五列

multi_dim_a = [[1,2,3],
               [2,3,4],
               [3,4,5]] # 三行三列

triple_a = [[[1,2],
             [3,4]],
            [[5,6],
             [7,8,]]]

# 在上面定义的List中进行搜索：
# print(multi_dim_a[0][1])
print(triple_a[0][0][1])