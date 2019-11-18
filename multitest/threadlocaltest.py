import threading

# 创建全局的ThreadLocal对象
local_thread_object = threading.local()


def process_student():
    # 获取当前线程相关联的student
    std = local_thread_object.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    #绑定当前线程相关联的student
    local_thread_object.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()