import requests
from bs4 import BeautifulSoup
#import csv

HOST = 'http://91.224.96.181/registration.html'
URL = 'http://91.224.96.181/registration.html'
HEADERS = {
    'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' ,

    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.396'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

#html = get_html(URL)
#print(html)

def get_content(html):
    soup = BeautifulSoup(html, 'hmtl.parser')
    items = soup.find_all('div', class='product-item')

