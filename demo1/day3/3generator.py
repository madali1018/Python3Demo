# 创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator。
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。

# generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。
# 对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。

L = [x for x in range(0, 10)]
# 普通函数调用直接返回结果
print(L)

G = (x for x in range(0, 10))
# generator函数的“调用”实际返回一个generator对象。
print(G)
