# 匿名函数lambda

L1 = list(map(lambda x: x * x, [1, 2, 3, 4]))
print(L1)


# 等价于
def f(x):
    return x * x


L2 = list(map(f, [1, 2, 3, 4]))
print(L2)
