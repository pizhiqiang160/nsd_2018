import socket

host = ''
port = 12345
addr = (host, port)
s = socket.socket(type=socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)

while True:
    data, cli_addr = s.recvfrom(1024)  # 接收数据，返回值是元组(数据，客户机地址)
    print(data.decode())
    sdata = input('> ') + '\r\n'
    s.sendto(sdata.encode(), cli_addr)  # 将数据发送给客户端

s.close()
