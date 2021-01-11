import requests
from lxml import etree
from time import sleep


def get_url_name(myurl):
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like)'

    header = {'user-agent': ua}
    response = requests.get(myurl, headers=header)

    selector = etree.HTML(response.text)

    film_name = selector.xpath('//div[@class="hd"]/a/span[1]/text()')

    film_link = selector.xpath('//div[@class="hd"]/a/@href')

    film_info = dict(zip(film_name, film_link))

    for i in film_info:
        print(f'Film Name: {i} \t\t Film Link: {film_info[i]}')


if __name__ == '__main__':
    urls = tuple(f'https://movie.douban.com/top250?start={ page * 25 }&filter=' for page in range(10))

    print(urls)

    for page in urls:
        get_url_name(page)
        sleep(5)