# 用sorted()排序的关键在于实现一个映射函数。
from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
# 接收一个key函数来实现自定义的排序，此处key函数的功能是字符串转小写。
print(sorted(L, key=str.lower))

# 用一组tuple表示学生名字和成绩。
students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 按名字排序
print(sorted(students, key=itemgetter(0)))
# 按分数排序
print(sorted(students, key=lambda t: t[1]))
# 按分数倒叙排序。进行反向排序，不必改动key函数，可以传入第三个参数reverse=True。
print(sorted(students, key=itemgetter(1), reverse=True))
