# https://v.daum.net/v/20250609143253430
# https://v.daum.net/v/20250609073120483
# https://v.daum.net/v/20250609190710378

# 2. 다음 뉴스기사 제목 크롤링

import requests # 원하는 서버에 접속하여 거기 있는 html 페이지 가져오는 모듈
from bs4 import BeautifulSoup # html 페이지안에 코드들을 가공하거나 자를수 있는 모듈

def daum_news_title_crawling(news_id):
    url = f"https://v.daum.net/v/{news_id}"
    request = requests.get(url)
    soup = BeautifulSoup(request.text,"html.parser")
    title = soup.find("h3", {"class":"tit_view"})
    if title:
        return title.text.strip()
    return "제목없음"

print(daum_news_title_crawling("20250609143253430"))

