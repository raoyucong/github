__author__ = 'Yucong Rao'

'测试参数'
# def aa(a,b,c=0,*arg,name,gender,**kw):
#     print(a,b,c,arg,name,gender,kw,sep=',')
#     print(len(arg),len(kw),kw.get('city'))

# aa(1,2,3,name=12,gender=13, city = 14, country = 'China')

# from email import encoders
# from email.header import Header
# from email.mime.text import MIMEText
# from email.utils import parseaddr, formataddr

# import smtplib
    
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))

# from_addr = '18362923070@163.com'
# password = 'ryc19951221'
# to_addr = 'njuraoyucong@163.com'
# smtp_server = 'smtp.163.com'

# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
    
# server = smtplib.SMTP(smtp_server, 25)
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

'由域名解析得到ip'
import socket
def getIP(domain):
    myaddr = socket.getaddrinfo(domain, 'http')
    for i in myaddr:
        print(myaddr[3][0])
getIP('www.baidu.com')

def get_ip_list(domain):  # 获取域名解析出的IP列表
            ip_list = []
            try:
                addrs = socket.getaddrinfo(domain, None)
                for item in addrs:
                    if item[4][0] not in ip_list:
                        ip_list.append(item[4][0])
            except Exception as e:
                print(str(e))
            return ip_list
print(get_ip_list('www.baidu.com'))

'测试闭包'
# total = 0 # 这是一个全局变量
# def sum( arg1, arg2 ):
#     def a():
#         nonlocal arg1
#         arg1 = arg1 - arg2
#         print(arg1)
#     total = arg1 + arg2# total在这里是局部变量.
#     print ("函数内是局部变量 : ", total)
#     a()
#     return total
# sum( 10, 20 )
# print ("函数外是全局变量 : ", total)

# c = 1
# def createCounter():
#     global c  #要修改外部作用域的变量需要使用global和nonlocal来定义，不然会视为重新定义一个局部变量
#     c = c + 1
#     print(c)
#     i = 0
#     def counter():
#         nonlocal i
#         i = i+1
#         return i
#     return counter
# # 测试:
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')

'测试装饰器'
# import time
# import functools
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args,**kw):
#             a = time.time()
#             f = fn(*args,**kw)
#             b = time.time()
#             print('%s executed in %s ms' % (fn.__name__,b-a))
#             return f
#     return wrapper

# def log(*arg):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             if len(arg) == 0:
#                 print('%s %s():' % ('call', func.__name__))
#             else:
#                 print('%s %s():' % (arg[0], func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y

# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z
# @log('executed')
# def master():
#     print(time.strftime("%Y-%m-%d %X"))
# f = fast(11, 22)
# s = slow(11, 22, 33)
# master()
# print(fast.__name__,slow.__name__)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')



'测试类的访问限制'
'''和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，
虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同。'''
# class Student(object):

#     def __init__(self, name, score, age):
#         self.__name = name
#         self.__score = score
#         self._age = age

#     def get_name(self):
#         return self.__name

#     def get_score(self):
#         return self.__score

#     def set_score(self, score):
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError('bad score')

#     def get_grade(self):
#         if self.__score >= 90:
#             return 'A'
#         elif self.__score >= 60:
#             return 'B'
#         else:
#             return 'C'

#     def get_age(self):
#         return self._age

# bart = Student('Bart Simpson', 59, 15)
# try:
#     print(bart.__name)
# except:
#     print("无法打印bart.__name")
# print(bart._age)

# bart._age = 18
# bart.__name = 'bob'
# print(bart.get_age(), bart.get_name(), bart.__name)


#测试type(),isinstance()与dir()
'''type()用于获取对象类型  isinstance()用来判断是否是对象类型 如果要获得一个对象的所有属性和方法，可以使用dir()函数'''
'''dir()配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态'''
# print('type(123) =', type(123))
# print('type(\'123\') =', type('123'))
# print('type(None) =', type(None))
# print('type(abs) =', type(abs))
# print('type(\'abc\')==str?', type('abc')==str)
'''@property用于对属性的赋值做约束'''
# class Student(object):
#     __slots__ = ('name', '_score') # 用tuple定义允许绑定的属性名称

#     @property
#     def score(self):
#         return self._score

#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value

# s = Student()
# s.age=9 #ValueError: 'score' in __slots__ conflicts with class variable
# s.score = 60
# print('s.score =', s.score)
# # ValueError: score must between 0 ~ 100!
# s.score = 9999


