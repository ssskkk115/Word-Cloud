import urllib.request
from bs4 import BeautifulSoup

url = "https://qiita.com/sksk_go"
res = urllib.request.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')
#タグ取得用に書き換え
name = soup.find_all("a",class_="u-link-unstyled TagList__label")
ret = []
for t in name:
    ret.append(t.text)

print(ret)