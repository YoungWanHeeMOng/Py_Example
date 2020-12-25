import sys
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

plusUrl=str(input())
#baseUrl='https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
baseUrl='https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query='
#plusUrl=input("검색어를 입력하세요: ")
url=baseUrl + url.parse.quote_plus(plusUrl)

html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

title=soup.find_all(class_='sh_blog_title')

for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print()