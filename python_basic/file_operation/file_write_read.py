text='This is my first test. This is the second line. This the third '
print(text)  # 无换行命令

text='This is my first test.\n \tThis is the second line.\nThis the third line'
print(text)   # 输入换行命令\n，要注意斜杆的方向。注意换行的格式和c++一样

my_file = open('my file.txt', 'w')
my_file.write(text)
my_file.close()

my_file = open('my file.txt', 'w')
my_file.append