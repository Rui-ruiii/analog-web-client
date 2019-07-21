"""
1.导入模块
2.创建套接字
3.建立连接
4.拼接请求协议
5.发送请求协议
6.接收服务器返回的内容
7.保存内容
8.关闭连接
"""
import socket

TCP_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#连接地址可以写域名，也可以写IP地址，端口号是80（怎么确定任意网页服务器端口号的？）
TCP_client_socket.connect(("www.icoderi.com",80))

#拼接请求协议
#1.请求行
request_line = "GET / HTTP/1.1\r\n"
#2.请求头
request_head = "Host:www.icoderi.com\r\n"
#3.请求空行
request_blank = "\r\n"
#4.请求报文
request_data = request_line + request_head + request_blank

#发送请求协议（就是刚刚写的request_data，但它是字符串，只能发二进制数，故需要转换）
TCP_client_socket.send(request_data.encode())

#接收服务器返回的内容
#socket的recv和accept的区别？
receve_data = TCP_client_socket.recv(4096)
receve_txt = receve_data.decode()
print(receve_txt)

#保存内容
# 1.查询/r/n/r/n的位置
location = receve_txt.find("\r\n\r\n")
# 2.截取字符串(切片)
html_data = receve_txt[location + 4:]
print(html_data)
# 3.保存文件
with open("index.html","w")as file:
    file.write(html_data)

#关闭连接
TCP_client_socket.close()
