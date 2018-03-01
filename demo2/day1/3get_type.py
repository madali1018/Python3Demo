# 判断对象类型，使用type()。
print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))
print('type(abs) =', type(abs))
print('type(\'abc\')==str?', type('abc') == str)

# 能用type()判断的基本类型也可以用isinstance()判断。
print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

print(isinstance([1, 2, 3], list))
print(isinstance([1, 2, 3], tuple))
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
print(isinstance([1, 2, 3], (list, tuple)))

# 获得一个对象的所有属性和方法。
print(dir("ab"))
