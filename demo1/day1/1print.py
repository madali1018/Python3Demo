# Python程序是大小写敏感的

# 输入函数
# name = input()
# print('Hello,', name)

# 输出函数
print(111)
# print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出：
# print()会依次打印每个字符串，遇到逗号“,”会输出一个空格
print('The quick brown fox', 'jumps over', 'the lazy dog')
print("The quick brown fox", 'jumps over', 'the lazy dog')
print("The quick brown fox", "jumps over", "the lazy dog")
print("日薪百万")
print("100 + 200 =", 100 + 200)

# 布尔值和布尔代数的表示完全一致，一个布尔值只有True、False，两种值要么是True，要么是False。
# 在Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来，也可以用and、or和not运算。
print(3 > 2)
print(3 > 2 and 2 > 1)
print(not 1 > 2)

# 字符串编码解码
s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

print('Hello, {0}, 成绩提升了 {1:.2f}%'.format('小明', 17.125))