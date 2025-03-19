# 字典

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])


# 通过in来判断key值是否存在
print('Tomas' in d)

print(d.get('Michael'))

print(d.get('Thomas'))

# 和list比较，dict有以下几个特点：

# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。


# 而list相反：

# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。