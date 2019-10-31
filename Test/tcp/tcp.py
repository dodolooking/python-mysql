import socket
import time

# 创建 socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
#s.connect(("10.124.35.168", 6000))
s.connect(("58.215.3.61", 9999))
# 接收服务器消息

msg=s.recv(1024).decode()

print(msg)

for data in [b'BG,00002,202007032236,T0,27.1,0.0,0.0,U,63.8,0.0,0.0,P,1007.7,0.0,0.0,WS,0.1,0.0,0.0,WD,18.1,0.0,0.0,PM2.5,0.0,0.0,0.0,NO2,0.0000,0.0000,0.0000,SO2,0.0000,0.0000,0.0000,NH3,168.7,0.0,0.0,9367,ED']:
    # 发送数据
    s.send(data)
    time.sleep(2)
    # 打印接收到的数据
    print(s.recv(1024).decode('utf-8'))
    time.sleep(1)

time.sleep(3)
# 请求退出
s.send(b'exit')
time.sleep(2)
print(s.recv(1024).decode('utf-8'))

# 关闭连接
s.close()