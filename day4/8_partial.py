import functools

# 偏函数
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数。
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
int2 = functools.partial(int, base=2)

# 二进制转十进制
print('1000000 =', int2('1000000'))
print('1010101 =', int2('1010101'))
# 二进制转十六进制
print('101 =', int2('101', base=16))
