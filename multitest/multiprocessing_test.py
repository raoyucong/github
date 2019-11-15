from multiprocessing import Process, Pool, Queue
import subprocess
import os, time, random, sys

def run_proc(name):
    print("run child process %s (%s)" % (name, os.getpid()))
    print("child process sleep: 5s")
    time.sleep(5)

def main_proc():
    print("parent process: %s begin" % os.getpid())
    p = Process(target=run_proc, args=('...',))
    print('Child process will start.')
    time.sleep(1)
    print('parent process')
    p.start()
    print('parent process')
    time.sleep(1)
    print('parent process')
    p.join()  # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print('Child process end.')

def long_time_task(name):
    print('run task %s process id is (%s)'%(name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print("Task %s runs %0.2f s."%(name, (end-start)))

def main_pool():
    print('parent process %s'%os.getpid())
    p = Pool(9) #默认为cpu核数
    for i in range(9):
        p.apply_async(long_time_task, args=(i,))
    print("waiting for all subprocess done...")
    p.close()   
    p.join() #对Pool对象调用join()方法会等待所有子进程执行完毕，
             #调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    print("all subprocess done")

def sub_proc():
    # print('$ nslookup www.python.org')
    # r = subprocess.call(['nslookup', 'www.baidu.com'])
    # print('Exit code:',r)
    # print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)

def write(q):
    print('Process to write: %s' % os.getpid())
    time.sleep(1)
    for value in ['1', '2', '3']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random()*3)
def read(q):
    print('Process to read: %s' % os.getpid())
    #time.sleep(1)
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)
def main_communication():
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    while True:
        value = q.get(True)
        print('parent process %s Get %s from queue.' % (os.getpid(), value))
        if not pw.join():
             # pr进程里是死循环，无法等待其结束，只能强行终止:
            pr.terminate()
            sys.exit()   
if __name__ == '__main__':
    # main_proc() 
    # main_pool()
    # sub_proc()
    main_communication()