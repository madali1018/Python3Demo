sum = 0
# Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
list1 = range(10)
list2 = list(list1)

for x in list2:
    sum = sum + x

print(list1)
print(list2)
print(sum)
print("------------------------")

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

print("------------------------")

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)