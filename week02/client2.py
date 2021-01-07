import socket

# AF_INET: IPv4 address
# SOCK_STREAM: TCP Protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f's1: {s}')

s.connect(('www.httpbin.org', 80))

print(f's2: {s}')

s.send(b'GET / HTTP/1.1\r\nHOST:time.geekbang.org\r\nConnection: close\n\r\n')

buffer = []

# classic template for receiving
while True:
    data = s.recv(1024)
    if data:
        buffer.append(data)
    else:
        break

s.close()

response = b''.join(buffer)

header, html = response.split(b'\r\n\r\n', 1)

print(header.decode('utf-8'))

with open('index2.html', 'wb') as f:
    f.write(html)

