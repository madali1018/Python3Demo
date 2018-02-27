# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以在set中没有重复的key。
s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
s1.add(4)
print(s1)
s1.remove(2)
print(s1)
s2 = set([2, 3, 4])
print(s2)
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作。
print(s1 & s2)
print(s1 | s2)

# set和dict的唯一区别仅在于没有存储对应的value，但是set的原理和dict一样，所以同样不可以放入可变对象，
# 因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。

print("-------------------")
# 可变对象作为key放入到dict或者set中会报错
s3 = set(1,2,3)
print(s3)
s4 = set(1,[2,3])
print(s4)
