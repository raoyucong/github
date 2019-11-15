import asyncio
import threading

#以下是asyncio版的协程
'''
@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print("Hello again!")

@asyncio.coroutine
def hellothread():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(2)
    print('Hello again! (%s)' % threading.currentThread())

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()
'''
#以下是async/await版的协程
async def hello():
    print('Hello world!')
    await asyncio.sleep(1)
    print('Hello again!')

async def hellothread():
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

tasks_web = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
tasks = [hellothread(), hellothread()]
#获取EventLoop
loop = asyncio.get_event_loop()
#执行coroutine
# loop.run_until_complete(asyncio.wait([hello()] + tasks))
loop.run_until_complete(asyncio.wait(tasks_web))
loop.close()
