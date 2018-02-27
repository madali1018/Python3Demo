# 切片操作：取list或tuple的指定索引范围的值。Python中正数切片和倒数切片都支持，经常使用切片代替循环操作。

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1)
# list1[0:5]表示，从索引0开始取，直到索引5为止，但不包括索引5。
print(list1[0:5])
# 如果第一个索引是0，还可以省略。
print(list1[:5])

# list1[-1]取倒数第一个元素
print(list1[-1])
print(list1[-5:-1])
print(list1[-5:])
