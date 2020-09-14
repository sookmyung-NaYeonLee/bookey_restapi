from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookey_restapi.settings")
import django
django.setup()
from .api_book.models import Book

bestSeller = pd.read_csv("kyobo_08best.csv", encoding="CP949")
before_url = 'http://www.kyobobook.co.kr/product/productSimpleReviewSort.laf?gb=klover&barcode=9788901243665&ejkGb=KOR&mallGb=&sortType=like'
barcodes = bestSeller['ISBN']
url = 'http://www.kyobobook.co.kr/product/productSimpleReviewSort.laf?gb=klover&barcode='

chrome_path = r'/usr/local/bin/chromedriver' #path from 'which chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)



def parse_book():
    books = []
    for rank, j in enumerate(barcodes):
        url2 = 'http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=' + str(j)
        url = 'http://www.kyobobook.co.kr/product/productSimpleReviewSort.laf?gb=klover&barcode=' + str(
            j) + '&ejkGb=KOR&mallGb=&sortType=like'
        webtotal = driver.get(
            url2 + '#review')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        bid = str(j)
        title = soup.find('h1', {'class': 'title'}).find('strong').getText()
        title = title.replace('\n', '')
        title = title.strip()
        author = soup.select('span.name a')[0].text
        publisher = soup.find('span', {'title': '출판사'}).getText()
        publisher = publisher.strip()
        publisher = publisher.replace('\n', '')
        price = soup.find('span', {'class': 'org_price'}).getText()
        price = price.replace('\n', '')
        price = price.strip()
        page = soup.select('table.table_simple2 > tbody > tr > td')[1].text
        description = soup.select('div.box_detail_article')[0].text
        description = description.replace('\n\n', '\n')
        description = description.strip()
        img_url = soup.find('div', {'class': 'box_detail_cover'}).find('img').get('src')
        print(title)
        book_obj = {'bid' : bid, 'title': title, 'author': author, 'publisher' : publisher, 'price' : price, 'pages' : page, 'description' : description, 'img_url' : img_url}
        books.append(book_obj)

    return books

if __name__=='__main__':
    book_data_dict = parse_book()
    for book in book_data_dict:
        print('new item : '+book['title'])
        Book(bid=book['bid'], title=book['title'], author=book['author'], publisher=book['publisher'], price=book['price'], pages=book['pages'], description=book['description'], img_url=book['img_url']).save()
