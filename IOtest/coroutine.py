# 协程测试coroutine

# 所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。
# 子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。
# 协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。

# Python对协程的支持是通过generator实现的。

def consumer():
    r = ''
    while True:
        n = yield r  # Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。
        if not n:
            return
        print("[CONSUMER] consuming %s" % n)
        r = '200 OK'

def produce(c):
    a = c.send(None)
    print(type(a))
    n = 0
    while n < 5:
        n = n + 1
        print("[PRODUCER] Producing %s" % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
