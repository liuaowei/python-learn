classmates = ['Michael', 'Bob', 'Tracy']

print(classmates)

# 用len()函数可以输出list的长度
print(len(classmates))

# 用索引可以访问列表中的每一个元素
print(classmates[0], classmates[1], classmates[2])

# 如果要取这个列表的最后一个元素,可以用-1索引
print(classmates[-1])


# list是一个有序列表，可以往list中追加元素到末尾
classmates.append('Adam')

print(classmates)

# 也可以把元素察隅到指定的位置，例如索引为1的位置
classmates.insert(1,'Jack')

print(classmates)

# 删除list末尾的元素，用pop方法

print(classmates.pop(),classmates)

# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置

classmates.pop(1)

print(classmates)
