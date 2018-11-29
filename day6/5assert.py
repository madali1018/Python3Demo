def foo(s):
    n = int(s)
    # 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代。如果断言失败，assert语句本身就会抛出AssertionError。
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

main()