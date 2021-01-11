import time
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
headers = {
    'User-Agent': ua.random,
    'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony'
}

s = requests.Session()
# used urlib3, connection pooling

login_url = 'https://accounts.douban.com/j/mobile/login/basic'
form_data = {
    'ck': '',
    'name': '15055495@qq.com',
    'password': 'test123test456',
    'remember': 'false',
    'ticket': ''
}

response = s.post(login_url, data = form_data, headers = headers)

# After login
# url2 = 'https://accounts.douban.com/passport/setting'
#
# response2 = s.get(url2, headers = headers)
# response3 = newsession.get(url3, headers = headers, cookies = s.cookies)
#
# with open('profile.html', 'w+') as f:
#     f.write(response2.text)