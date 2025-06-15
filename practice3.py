# 3. 멜론 차트 크롤링

import requests
from bs4 import BeautifulSoup

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
request = requests.get("https://www.melon.com/chart/index.htm",headers=header)
soup = BeautifulSoup(request.text)

titles = soup.findAll("div",{"class":"rank01"})
artists = soup.findAll("span",{"class":"checkEllipsis"})

for i,(t,a) in enumerate(zip(titles,artists), 1):
    title = t.text.strip()
    artist = a.text.strip()
    print(f"{i} : {title} - {artist}")

    