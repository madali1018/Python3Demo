# 编写高阶函数，就是让函数的参数能够接收别的函数。
def f(x):
    return x * x


# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
r = map(f, [1, 2, 3, 4])
print(r)
print(list(r))
