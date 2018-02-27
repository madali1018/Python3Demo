# 返回函数
def lazy_sum(*args):
    # 在函数lazy_sum中定义了函数sum，并且内部函数sum可以引用外部函数lazy_sum的参数和局部变量。
    # 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中。闭包
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        # 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
        return ax
    return sum


f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
# 调用lazy_sum()时，返回的并不是求和结果，而是求和函数。
print(f)
# 调用函数f时，才真正计算求和的结果。
print(f())

f1 = lazy_sum(1,2,3,4)
f2 = lazy_sum(1,2,3,4)
# 调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数。
print(f1 == f2)