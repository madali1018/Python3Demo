def count():
    fs = []
    for i in range(1, 4):
        def f():
            # 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
# f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9
# 返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
print(f1())
print(f2())
print(f3())