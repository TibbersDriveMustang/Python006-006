from urllib import request

resp = request.urlopen('http://httpbin.org/get')
print(resp.read().decode())

resp = request.urlopen('http://httpbin.org/post', data=b'key=value', timeout=10)
print(resp.read().decode())

from http import cookiejar

cookie = cookiejar.CookieJar

handler = request.HTTPCookieProcessor(cookie)

opener = request.build_opener(handler)
