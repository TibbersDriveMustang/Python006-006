import requests
r = requests.get('https://github.com')
r.status_code
r.headers['content-type']
r.encoding

r = requests.post('http://httpbin.org/post', data={'key': 'value'})
r.json()
