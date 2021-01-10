# fetch douban top 50

import requests

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) ApplWebKit/537.36'

header = {'user-agent': user_agent}

myurl = 'https://movie.douban.com/top250'

response = requests.get(myurl, headers=header)

print(response.text)
print(f'return code: {response.status_code}')
