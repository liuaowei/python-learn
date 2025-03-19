s = {1,2,3}
print(s)


s = set([1,2,3])
print(s)


s.add(4)
print(s)


# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：

s1 = {1, 2, 3}
s2 = {2, 3, 4}

print(s1 & s2)

# 不可变对象

# list可变对象,可以直接改变a的值
a = ['c','b','a']
# print(a.sort())

# str是不可变对象
# 当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：
b = 'abc'
b.replace('a','A')
print(b)
c = b.replace('a','A')
print(c)