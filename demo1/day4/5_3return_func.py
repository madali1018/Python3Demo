def count():
    fs = []
    def f(n):
        # 如果一定要引用循环变量怎么办？
        # 方法是再创建一个函数，用该函数的参数绑定循环变量当前的值。
        # 无论该循环变量后续如何更改，已绑定到函数参数的值不变。
        def j():
            return n * n
        return j
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())