import socket
import ssl

# 创建socket
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
#s.connect(('www.sina.com.cn', 80))

s = ssl.wrap_socket(socket.socket())
s.connect(('www.sina.com.cn', 443))

'创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议'
'''作为服务器，提供什么样的服务，端口号就必须固定下来。新浪强制HTTPS协议访问 所以 80端口改443 socket 改 ssl
由于我们想要访问网页，因此新浪提供网页服务的服务器必须把端口号固定在80端口，因为80端口是Web服务的标准端口。
其他服务都有对应的标准端口号，例如SMTP服务是25端口，FTP服务是21端口，等等。
端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。'''

s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close()
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)