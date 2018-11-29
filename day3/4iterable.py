from collections import Iterable
from collections import Iterator

# 可以直接作用于for循环的数据类型有以下几种：
#       一类是集合数据类型，如list、tuple、dict、set、str等；
#       一类是generator，包括生成器和带yield的generator function。

# 凡是可作用于for循环的对象都是Iterable类型，
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列。

# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# Python的for循环本质上就是通过不断调用next()函数实现的。

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance(100, Iterator))

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数。
print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
