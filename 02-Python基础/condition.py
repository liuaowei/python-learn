# 条件判断

# 根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。
age = 20
if age >= 18:
    print('your age is:', age)
    print('adult')

# 可以利用 elif 做更细致的判断

age2 = 3
if age2 >= 18:
    print('adult')
elif age2 >= 6:
    print('teenager')
else:
    print('kid')

# input

# 最后看一个有问题的条件判断。很多同学会用input()读取用户的输入，这样可以自己输入，程序运行得更有意思：

s = input('birth:')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')