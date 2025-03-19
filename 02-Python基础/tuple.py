teammates = ('詹姆斯', '库里', '杜兰特')

# 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
print(teammates[1])

# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：
t = (1,2)

print(t)

# 如果要定义一个元素的tuple必须要加一个逗号
one = (1,)
print(one)


# tuple的指向永远不变，这里举个例子
# 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
# 理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。
t2 = (1,2,['a','b'])
t2[2][0] = 'X'
t2[2][1] = 'Y'
print(t2)

# 如果要定义一个空的tuple
tnull = ()
print(tnull)