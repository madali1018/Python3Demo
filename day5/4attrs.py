# 仅仅使用dir()把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态。
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

# 有属性'x'吗？
print('hasattr(obj, \'x\') =', hasattr(obj, 'x'))

# 有属性'y'吗？
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))
# 设置一个属性'y'
setattr(obj, 'y', 19)
# 有属性'y'吗？
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))
# 获取属性'y'
print('getattr(obj, \'y\') =', getattr(obj, 'y'))
# 获取属性'y'
print('obj.y =', obj.y)

# 获取属性'z'，如果不存在，返回默认值404
print('getattr(obj, \'z\') =', getattr(obj, 'z', 404))

# 获取属性'power'
f = getattr(obj, 'power')
print(f)
print(f())

# 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性。
# 但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

# 实例属性属于各个实例所有，互不干扰；
# 类属性属于类所有，所有实例共享一个属性；
# 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
