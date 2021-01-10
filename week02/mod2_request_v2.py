import requests
from pathlib import *
import sys

# Google Python Style

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gec)'
header = {'user-agent': ua}

myurl = 'https://movie.douban.com/top250'

response = None

try:
    response = requests.get(myurl, headers=header, timeout=0.5)
except requests.exceptions.ConnectTimeout as e:
    print(f'requests timeout {e}')

p = Path(__file__)
pyfile_path = p.resolve().parent

html_path = pyfile_path.joinpath('html')

if not html_path.is_dir():
    Path.mkdir(html_path)
page = html_path.joinpath('douban.html')

print(page)

try:
    with open(page, 'w', encoding='utf-8') as f:
        f.write(response.text)
except FileNotFoundError as e:
    print(f'File can not be open', {e})
except IOError as e:
    print(f'File can not be read, {e}')
except Exception as e:
    print(e)
