def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
    
# 如果想定义一个什么事也不做的函数，可以用pass语句
def nop():
    # 缺少了pass，代码运行就会有语法错误
    pass

# 参数检查
def my_abs2(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-99))

print('加上类型检查：',my_abs2('as'))