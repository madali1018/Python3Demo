# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素，-2获取倒数第二个元素，以此类推。
list1 = [1, 2, 3]
print(len(list1))

# 往list中追加元素到末尾
list1.append(4)
print(list1)

# 把元素插入到指定的位置，比如索引号为2的位置
list1.insert(2, 100)
print(list1)

# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
list1.pop(1)
print(list1)

# print("\n")
print("------------------")

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改。
# tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来。
tuple1 = [1, 2, 3]
print("tuple1:",tuple1)

tuple2 = [1]
print("tuple2:",tuple2)

tuple3 = (3)
print("tuple3:",tuple3)
