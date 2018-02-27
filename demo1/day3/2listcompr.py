# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

# 常规写法
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

# 简写：用列表生成式代替循环生成上面的list
L2 = [x * x for x in range(1, 11)]
print(L2)

# 两层及多层循环
L3 = [m + n for m in 'ABC' for n in 'XYZ']
print(L3)

# 迭代dict的key和values
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

print([k for k in d.keys()])
print([v for v in d.values()])
print([k + '=' + v for k, v in d.items()])
