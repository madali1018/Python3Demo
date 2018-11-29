import logging
logging.basicConfig(level=logging.INFO)

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
        logging.info("1111")
    except Exception as e:
        # 日志记录异常
        logging.exception(e)
        logging.info("2222")

main()
print('END')
